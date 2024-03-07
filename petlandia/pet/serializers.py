from rest_framework import serializers
from pet.models import Pet
from medicalhistory.serializers import MedicalHistorySerializers
class PetSerializer(serializers.ModelSerializer):
    medical_histories = MedicalHistorySerializers(many= True, required = False)
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Pet
        exclude = ['created', 'modified']
class ListPetsSerializers(serializers.ModelSerializer):
    medical_histories = MedicalHistorySerializers(many= True, required = False)
    class Meta:
        model = Pet
        fields = '__all__'
class DetailPetSerializers(serializers.ModelSerializer):
    medical_histories = MedicalHistorySerializers(many= True, required = False)
    
    class Meta: 
        model = Pet
        fields = ['id','name', 'species', 'breed', 'color_or_markings', 'birthday', 'parent', 'sex', 'created', 'modified', 'medical_histories' ]

        

# class DisplayParentDetailsSerializers(serializers.ModelSerializer):
#     number_of_pets = serializers.SerializerMethodField(read_only = True)
#     pets = PetSerializer(many= True, required = False)
#     class Meta:
#         model = Parent
#         fields = ['id','full_name','occupation', 'contact_number', 'pets', 'number_of_pets','created']
#         depth = 1
#     def get_number_of_pets(self, obj):
#         return obj.pets.count()