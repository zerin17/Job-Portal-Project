from django.contrib import admin

from myapp.models import *


admin.site.register(customUser)
admin.site.register(recruiterProfileModel) 
admin.site.register(seekerProfileModel) 
admin.site.register(JobModel) 
admin.site.register(jobApplyModel) 