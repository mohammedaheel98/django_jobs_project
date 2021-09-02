from django.contrib import admin
from testapp.models import *
# Register your models here.
@admin.register(CheJobs)
class CheJobsAdmin(admin.ModelAdmin):
    list_display = ('date','company','tittle','eligbility','address','email','phoneno')

@admin.register(BanJobs)
class BanJobsAdmin(admin.ModelAdmin):
    list_display = ('date','company','tittle','eligbility','address','email','phoneno')

@admin.register(HydJobs)
class HydJobsAdmin(admin.ModelAdmin):
    list_display = ('date','company','tittle','eligbility','address','email','phoneno')

@admin.register(PuneJobs)
class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ('date','company','tittle','eligbility','address','email','phoneno')

