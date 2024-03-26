from django.urls import path
from .views import ExternalStakeholdersList,ExternalStakeholderDetail


urlpatterns = [
    path("",ExternalStakeholdersList.as_view(),name="list"),
    path("<int:pk>/",ExternalStakeholderDetail.as_view(),name="detail"),
]
