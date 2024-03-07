from rest_framework import serializers
from parent.models import Parent
from pet.models import Pet
from medicalhistory.models import MedicalHistory
from pet.serializers import PetSerializer

        

class ParentSerializer(serializers.ModelSerializer):
    pet = PetSerializer(many= True, required = False)
    class Meta:
        model = Parent
        exclude = ['created', 'modified']
    def create(self, validated_data):
        parent_data = validated_data.pop('nested', [])
        instance = Parent.objects.create(**validated_data)

        for pet_data in parent_data:
            medical_history_data = pet_data.pop('super_nested', [])
            nested_model = Pet.objects.create(parent=instance, **pet_data)

            for history in medical_history_data:
                MedicalHistory.objects.create(nested_model=nested_model, **history)

        return instance
 
   
class ListParentSerializers(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%m-%d-%Y %H:%M:%S%f")
    pet = PetSerializer(many= True, required = False)
    number_of_pets = serializers.SerializerMethodField()
    class Meta:
        model = Parent
        fields = ['id','full_name','pet','occupation', 'contact_number', 'number_of_pets','created']
        depth = 1
    def get_number_of_pets(self, obj):
        return obj.pets.count()

class CreateParentSerializers(serializers.ModelSerializer):
    # created = serializers.DateTimeField(format="%m-%d-%Y %H:%M:%S.%f", read_only = True)
    # modified = serializers.DateTimeField(format="%m-%d-%Y %H:%M:%S.%f", read_only = True)
    
    
    class Meta:
        model = Parent
        fields = ['id','full_name','occupation', 'contact_number', 'created', 'modified']
class DisplayParentDetailsSerializers(serializers.ModelSerializer):
    number_of_pets = serializers.SerializerMethodField(read_only = True)
    pets = PetSerializer(many= True, required = False)
    class Meta:
        model = Parent
        fields = ['id','full_name','occupation', 'contact_number', 'pets', 'number_of_pets','created']
        depth = 1
    def get_number_of_pets(self, obj):
        return obj.pets.count()



class EditParentSerializer(serializers.ModelSerializer):
    pets = serializers.PrimaryKeyRelatedField(queryset=Pet.objects.all(), many=True)
    number_of_pets = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Parent
        fields = ['full_name', 'pets', 'occupation', 'contact_number','number_of_pets' ]
        partial = True
        depth = 1
