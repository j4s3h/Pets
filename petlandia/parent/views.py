from rest_framework import generics, status
from .models import Parent
from .serializers import DisplayParentDetailsSerializers, ListParentSerializers, CreateParentSerializers, EditParentSerializer, ParentSerializer

class DisplayParentViews(generics.ListAPIView):
    queryset = Parent.objects.all()
    serializer_class = ListParentSerializers
class ParentDetailViews( generics.RetrieveUpdateDestroyAPIView):
    queryset = Parent.objects.all()
    serializer_class = DisplayParentDetailsSerializers
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return EditParentSerializer
        elif self.request.method == 'GET':
            return DisplayParentDetailsSerializers
        return super().get_serializer_class()
        
class CreateParentViews(generics.CreateAPIView):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    
