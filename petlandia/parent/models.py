from django.db import models

class Parent(models.Model):
    full_name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    contact_number =models.CharField(max_length = 11)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return f"Parent {self.full_name}"

    @property
    def get_total_parent(self):
        queryset = Parent.objects.count()
        return queryset