# hospital_project/urls.py
from django.contrib import admin
from django.urls import path, include
#from hospitals.views import map_view

#from hospitals import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hospitals.urls')),  # This line includes app-level URLs
    #path('map/', map_view, name='map_view'),  # Project-level URL pattern
]
