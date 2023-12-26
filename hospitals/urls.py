# hospitals/urls.py
from django.urls import path
from .views import hospital_map, hospital_detail , hospital_list , add_hospital

urlpatterns = [
    path('', hospital_map, name='hospital-map'),
    path('hospital/<int:pk>/', hospital_detail, name='hospital-detail'),
    path('hospital_list/', hospital_list, name='hospital-list'),
    path('hospital-detail/<int:hospital_id>/', hospital_detail, name='hospital-detail'),
    path('add/', add_hospital, name='add-hospital'),
    # ... other URL patterns ...
]
