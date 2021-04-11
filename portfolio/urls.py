from django.urls import path
from .views import HomePageView, ProjectDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('projects/<uuid:pk>', ProjectDetailView.as_view(), name='project_detail'),
]
