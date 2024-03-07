from django.contrib import admin
from parent.models import Parent

@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'pet_name', 'pet_color_or_markings', 'occupation', 'contact_number', 'created', 'modified', )
    
    def pet_name(self, obj):
        return ", ".join([pet.name for pet in obj.pets.all()])

    pet_name.short_description = 'Pets Name'
    
    def pet_color_or_markings(self, obj):
        return ", ".join([pet.color_or_markings for pet in obj.pets.all()])

    pet_color_or_markings.short_description = 'Pets Color or Markings'
    
    
    
    