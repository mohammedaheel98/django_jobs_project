from django.shortcuts import render
from testapp.models import *
# Create your views here.

def home_index(request):
    return render(request,'testapp/index.html')

def che_jobs(request):
    jobs_list = CheJobs.objects.all().order_by('company')
    return render(request,'testapp/chejobs.html',{'jobs_list':jobs_list})

def ban_jobs(request):
    jobs_list = BanJobs.objects.all().order_by('company')
    return render(request,'testapp/banjobs.html',{'jobs_list':jobs_list})

def hyd_jobs(request):
    jobs_list = HydJobs.objects.all().order_by('company')
    return render(request,'testapp/hydjobs.html',{'jobs_list':jobs_list})

def pune_jobs(request):
    jobs_list = PuneJobs.objects.all().order_by('company')
    return render(request,'testapp/punejobs.html',{'jobs_list':jobs_list})
