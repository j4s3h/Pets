from rest_framework import generics
from .models import MedicalHistory
from .serializers import MedicalHistorySerializers, DetailMedicalHistorySerializer, LandingPageSerializer
from django.shortcuts import get_object_or_404
from pet.models import Pet
from rest_framework.response import Response
from rest_framework import status
class ListMedicalHistoryViews(generics.ListAPIView):
    queryset = MedicalHistory.objects.all()
    serializer_class = MedicalHistorySerializers
    
class DetailMedicalHistoryViews(generics.RetrieveUpdateDestroyAPIView):
    queryset = MedicalHistory.objects.all()
    serializer_class = DetailMedicalHistorySerializer
    
class CreateMedicalHistoryViews(generics.CreateAPIView):
    queryset = MedicalHistory.objects.all()
    serializer_class = DetailMedicalHistorySerializer

    def post(self, request, pet_id):
        pet_instance = get_object_or_404(Pet, id=pet_id)
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save(pet=pet_instance)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LandingPage(generics.RetrieveAPIView):
    serializer_class = LandingPageSerializer

    def get_object(self):
        return MedicalHistory.objects.latest('followup_checkup_date')
    
class MedicalHistoryByPetIDViews(generics.ListAPIView):
    
    def list(self, request,pet_id):
        pet_instance = get_object_or_404(Pet, id=pet_id)
        queryset = MedicalHistory.objects.filter(pet=pet_instance)
        serializer = DetailMedicalHistorySerializer(queryset, many = True)
        return Response(serializer.data)
    
# class C(generics.ListAPIView):
#     queryset = MedicalHistory.objects.all()
#     serializer = DetailMedicalHistorySerializer(queryset, many = True)s
    
    
     
#         "parent_id": 1,
#         "full_name": "John Doe",
#         "occupation": "Software Developer",
#         "contact_number": "12345678901",
#      "medical_history_records": [
#         {
#             "id": 1,
#             "pet": 1,
#             "total_medical_history": "2",
#             "chief_complaint": null,
#             "medication_given_prior_to_check_up": null,
#             "last_vaccination_given": null,
#             "last_vaccination_date": null,
#             "last_vaccination_brand": null,
#             "last_deworming_given": null,
#             "last_deworming_date": null,
#             "last_deworming_brand": null,
#             "is_transferred_from_other_clinic": false,
#             "name_of_clinic": null,
#             "case": null,
#             "date_hospitalized": null,
#             "diet": null,
#             "weight": null,
#             "initial_temp": null,
#             "heart_rate": null,
#             "respiratory_rate": null,
#             "abnormal_findings": null,
#             "is_cbc": false,
#             "is_skin_scrape": false,
#             "is_xray": false,
#             "is_dfs": false,
#             "is_urinalysis": false,
#             "is_vaginal_smear": false,
#             "tentative_diagnosis": null,
#             "prognosis": null,
#             "treatment_given": null,
#             "take_home_meds": null,
#             "recommendations": null,
#             "followup_checkup_date": null,
#             "created": "2024-03-07T03:25:11.433233Z",
#             "modified": "2024-03-07T03:25:11.433233Z"
#         },