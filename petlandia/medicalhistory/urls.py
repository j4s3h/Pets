from django.urls import path
from .views import DetailMedicalHistoryViews, ListMedicalHistoryViews, CreateMedicalHistoryViews, LandingPage, MedicalHistoryByPetIDViews
urlpatterns = [
    path('', ListMedicalHistoryViews.as_view(), name = 'display_all_medical_history'),
    path('<int:pk>/',DetailMedicalHistoryViews.as_view(), name = 'display_detail_medical_history'), 
    path('create/',CreateMedicalHistoryViews.as_view(), name = 'create_medical_history'),
    path('pet/<pet_id>/', MedicalHistoryByPetIDViews.as_view(), name ='medical_history_by_pet_id'),
    path('landing_page/', LandingPage.as_view())
] 