from django.shortcuts import render
from .models import Project

# Create your views here.

def index(request):

    # get all the model data
    projects = Project.objects.all()
    print(projects)

    return render(request,'portfolio/home.html', {'projects' : projects})