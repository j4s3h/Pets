from django.urls import path
from .views import DisplayPetViews, PetsDetailViews, CreatePetsViews
urlpatterns = [
    path('', DisplayPetViews.as_view(), name = 'display_pet'),
    path('create/', CreatePetsViews.as_view(), name = 'create_pet'),
    path("<int:pk>/", PetsDetailViews.as_view(), name = 'pets_detail_views')
]
