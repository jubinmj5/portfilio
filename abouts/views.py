from django.shortcuts import render
from django.http import HttpResponse
from .models import Resume,Project
# Create your views here.

def index(request):
   # return HttpResponse("<h1>Index page</h1>")
    #return render(request,'index.html')
    return render(request,'index.html')


def project(request):
    projects = Project.objects.all()
    #return HttpResponse("<h1>Project page</h1>")
    return render(request,'project.html',{'projects':projects})

def resume(request):
    resumes = Resume.objects.all()
    #return HttpResponse("<h1>Project page</h1>")
    return render(request,'resume.html',{'images':resumes})