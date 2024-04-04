from django.urls import path, include
from msme_app.api.views import formViewSet, formDetailViewSet
# from rest_framework.routers import DefaultRouter
# router = DefaultRouter()
# router.register('form', formViewSet, basename='msmereg')


urlpatterns = [
    
     path("", formViewSet.as_view({'get': 'list', 'post': 'create'}                                ), name="formview"),
       path("<int:pk>/", formDetailViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name="external-stakeholder-detail"),
    
    # path('register/', formcr.as_view(), name='form-fill'),
    # path('edit/', formrud.as_view(), name='form-alter'),
    # path('', include(router.urls)),
]