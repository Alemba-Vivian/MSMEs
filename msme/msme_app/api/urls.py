from django.urls import path, include
from msme_app.api.views import formcr,formrud

urlpatterns = [
    
    path('register/', formcr.as_view(), name='form-fill'),
    path('edit/', formrud.as_view(), name='form-alter'),
]