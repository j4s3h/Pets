from rest_framework import serializers
from parent.models import Parent
from pet.models import Pet
from medicalhistory.models import MedicalHistory
from pet.serializers import PetSerializer
from rest_framework.response import Response



class ParentSerializer(serializers.ModelSerializer):
    pet = PetSerializer(many= True, required = False)
    class Meta:
        model = Parent
        exclude = ['created', 'modified']
    def create(self, validated_data):
        parents_data = validated_data.pop('pets', [])
        full_name = validated_data.pop('full_name')
        occupation = validated_data.pop('occupation')
        contact_number = validated_data.pop('contact_number')
        existing_parent_contact = Parent.objects.filter(contact_number=contact_number).first()
        if existing_parent_contact:
            raise serializers.ValidationError({"message": "A parent with the same contact number already exists", "existing_parent": existing_parent_contact})

        existing_parent_name_occupation = Parent.objects.filter(full_name=full_name, occupation=occupation).first()
        if existing_parent_name_occupation:
            raise serializers.ValidationError({"message": "A parent with the same full name and occupation already exists", "existing_parent": existing_parent_name_occupation})
        instance = Parent.objects.create(full_name=full_name, occupation=occupation, contact_number=contact_number, **validated_data)
        for pet_data in parents_data:
            
            medical_histories_data = pet_data.pop('medical_histories', [])
            pet_instance = Pet.objects.create(parent=instance, **pet_data)
            for history_data in medical_histories_data:
                MedicalHistory.objects.create(pet=pet_instance, **history_data)
        return instance

    def update(self, instance, validated_data):
        nested_data = validated_data.pop('pets', [])
        instance = super().update(instance, validated_data)

        existing_nested_models = Parent.objects.filter(parent=instance)
        # Deleting existing nested models that is not part of the validated_data
        for existing_nested_model in existing_nested_models:
            if not any(item.get('id') == existing_nested_model.id for item in nested_data):
                MedicalHistory.objects.filter(nested_model=existing_nested_model).delete()
                existing_nested_model.delete()

        # Update or create nested models
        for nested_item in nested_data:
            super_nested_data = nested_item.pop('pets', [])
            nested_instance, created = Parent.objects.update_or_create(
                parent=instance,
                id=nested_item.get('id'),
                defaults={'pets': nested_item.get('pets')}
            )

            # Deleting existing super nested models that is not part of the validated_data
            existing_super_nested_models = MedicalHistory.objects.filter(nested_model=nested_item.get('id'))

            for existing_super_nested_model in existing_super_nested_models:
                if not any(item.get('id') == existing_super_nested_model.id for item in super_nested_data):
                    existing_super_nested_model.delete()

            for super_nested_item in super_nested_data:
                MedicalHistory.objects.update_or_create(
                    nested_model=nested_instance,
                    id=super_nested_item.get('id'),
                    defaults={'medical_histories': super_nested_item.get('medical_histories')}
                )


        return instance

 
   
class ListParentSerializers(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%m-%d-%Y %H:%M:%S%f")
    pets = PetSerializer(many= True, required = False)
    number_of_pets = serializers.SerializerMethodField()    
    class Meta:
        model = Parent
        fields = ['id','full_name','pets','occupation', 'contact_number', 'number_of_pets','created', 'pets']
        depth = 1
    def get_number_of_pets(self, obj):
        return obj.pets.count()

class CreateParentSerializers(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%m-%d-%Y %H:%M:%S.%f", read_only = True)
    modified = serializers.DateTimeField(format="%m-%d-%Y %H:%M:%S.%f", read_only = True)
    
    
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
