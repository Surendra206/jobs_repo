from django.shortcuts import render
from testapp.models import Hydjobs, Bangjobs, Chennaijobs, Kolkatajobs


# Create your views here.
def home_page(request):
    return render(request,'testapp/index.html')
def Hydjobs_view(request):
    job_list=Hydjobs.objects.all()
    return render(request,'testapp/hyd.html',{'job_list':job_list})
def Bangjobs_view(request):
    job_list=Hydjobs.objects.all()
    return render(request,'testapp/bang.html',{'job_list':job_list})
def Chennaijobs_view(request):
    job_list=Hydjobs.objects.all()
    return render(request,'testapp/chennai.html',{'job_list':job_list})
def Kolkatajobs_view(request):
    job_list=Hydjobs.objects.all()
    return render(request,'testapp/kolkata.html',{'job_list':job_list})