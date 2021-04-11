from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Project

class HomePageView(ListView):
    model = Project
    template_name = 'home.html'

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'details.html'
