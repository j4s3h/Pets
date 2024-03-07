from django.urls import path
from .views import DisplayParentViews, ParentDetailViews, CreateParentViews

urlpatterns = [
    #localhost:8000/parent/
    path('', DisplayParentViews.as_view(), name = 'list_parent') ,
    path('create/', CreateParentViews.as_view(), name = 'create_parent_view'),    
    path('<int:pk>/', ParentDetailViews.as_view(), name = 'detail_parent'),
    
        
]
