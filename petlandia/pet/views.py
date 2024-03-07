from rest_framework import generics
from pet.models import Pet
from .serializers import ListPetsSerializers, DetailPetSerializers
class DisplayPetViews(generics.ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = ListPetsSerializers
class PetsDetailViews( generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = DetailPetSerializers


class CreatePetsViews(generics.CreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = DetailPetSerializers
    

    
