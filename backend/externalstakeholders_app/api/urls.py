from django.urls import path
# from .views import ExternalStakeholdersList,ExternalStakeholderDetail
from .views import ExternalStakeholdersViewSet, ExStakeholdersDetailViewSet

urlpatterns = [
    path("", ExternalStakeholdersViewSet.as_view({'get': 'list', 'post': 'create'}), name="formview"),
       path("<int:pk>/", ExStakeholdersDetailViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name="external-stakeholder-detail"),
]
