from django.contrib import admin
from django.urls import path
from myproject.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',registerPage,name="registerPage"),
    path("loginPage/", loginPage, name="loginPage"),
    path("homePage/", homePage, name="homePage"),
    path("logoutPage/", logoutPage, name="logoutPage"),
    path("ProfilePage/", profilePage, name="profilePage"),
    path("editProfile/", editProfile, name="editProfile"),
    path("addjob/", addjob, name="addjob"),

    path('addSkill/',addSkill, name="addSkill"),
    path('editSkill/',editSkill, name="editSkill"),
    
    path("createjob/", createjob, name="createjob"),
    path("jobfeed/", jobfeed, name="jobfeed"),
    path("deletejob/<int:id>", deletejob, name="deletejob"),
    path("viewjob/<int:id>", viewjob, name="viewjob"),
    path("editjob/<int:id>", editjob, name="editjob"),
    path("apply_now/<int:id>", apply_now, name="apply_now"),
    path('searchJob/', searchJob, name='searchJob'),

    path('skill_matchingPage/', skill_matchingPage, name='skill_matchingPage'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
