from django.db import models
from parent.models import Parent

class Pet(models.Model):
    name = models.CharField(max_length= 100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    color_or_markings = models.CharField(max_length=100)
    birthday = models.DateField()
    parent = models.ForeignKey(Parent, on_delete = models.CASCADE, related_name = 'pets')
    
    SEX_CHOICES = [
        ('F', 'Female'),
        ('M', 'Male'),
    ]
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name = "Pet"
        verbose_name_plural = "Pets"
    @property
    def get_total_pets(self):
        queryset = Pet.objects.count()
        return queryset
    
    