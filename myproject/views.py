from django.shortcuts import render,redirect,get_object_or_404

from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def registerPage(request):
    
    if request.method=='POST':
        
        username=request.POST.get("username")
        email=request.POST.get("email")
        password=request.POST.get("password")
        Confirm_password=request.POST.get("confirm_password")
        user_type=request.POST.get("user_type")
        Profile_Pic=request.FILES.get("profile_pic")
        contact_no=request.POST.get("contact_no")
    
        
        if password==Confirm_password:
            user=customUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                user_type=user_type,
                Profile_Pic=Profile_Pic,
                contact_no=contact_no,
            )
            if user_type=='seeker':
                seekerProfileModel.objects.create(user=user)
                
            elif user_type=='recruiter':
                recruiterProfileModel.objects.create(user=user)
            
            return redirect("loginPage")
            
    return render(request,"registerPage.html")


def loginPage(request):
    if request.method == 'POST':
        
        user_name=request.POST.get("username")
        pass_word=request.POST.get("password")

        try:
            user = authenticate(request, username=user_name, password=pass_word)

            if user is not None:
                login(request, user)
                return redirect('homePage') 
            else:
                return redirect('signInPage')

        except customUser.DoesNotExist:
            return redirect('loginPage')

    return render(request, 'loginPage.html')

@login_required
def homePage(request):
    
    
    return render(request,"homePage.html")


def logoutPage(request):
    
    logout(request)
    
    return redirect('loginPage')

@login_required
def profilePage(request):
    
    
    
    return render(request,"profilePage.html")

def addjob(request):
    current_user=request.user
    if current_user.user_type == "recruiter":
        if request.method=="POST":
            jobs=JobModel()
            jobs.user=current_user
            jobs.job_title=request.POST.get("job_title")
            jobs.category=request.POST.get("category")
            jobs.skills=request.POST.get("skills")
            jobs.number_of_openings=request.POST.get("vacancy")
            jobs.description=request.POST.get("description")
            jobs.job_Pic=request.FILES.get("job_Pic")
            
            jobs.save()
            
            
            return redirect("jobfeed")
        return render(request,'addjob.html')
 

def createjob(request):
    current_user=request.user
    jobs=JobModel.objects.filter(user=current_user)

    text={
        "jobs":jobs
    }
    
    return render(request,"createjob.html",text)

def jobfeed(request):
    jobs=JobModel.objects.all()

    text={
        "jobs":jobs
    }
    
    return render(request,"jobfeed.html",text)


def deletejob(request,id):
    jobs=JobModel.objects.filter(id=id)
    jobs.delete()


    
    return redirect("createjob")


def editjob(request,id):
    
    
    jobs=JobModel.objects.get(id=id)
    job_instance=jobs
    current_user=request.user
    if current_user.user_type == "recruiter":
        if request.method=="POST":
            jobs=JobModel()
            jobs.id=request.POST.get("id")
            jobs.user=current_user
            jobs.job_title=request.POST.get("job_title")
            jobs.number_of_openings=request.POST.get("vacancy")
            jobs.skills=request.POST.get("skills")
            jobs.category=request.POST.get("category")
            jobs.description=request.POST.get("description")
            if request.FILES.get('job_Pic'):
                jobs.job_Pic=request.FILES.get("job_Pic")
            else:
                jobs.job_Pic=job_instance.job_Pic
            jobs.save()
            return redirect("createjob")
     
    
    context={
        "jobs":jobs
    }
    
    return render(request,"editjob.html",context)



def viewjob(request,id):
    jobs=JobModel.objects.filter(id=id)
    text={
        "jobs":jobs
    }
    return render(request,"viewjob.html",text)


def apply_now(request,id):
    current_user=request.user
    if current_user.user_type == 'seeker':
        jobs=JobModel.objects.get(id=id)
        context= {

            'jobs': jobs
        }

      
        if request.method == 'POST':
            job_title=request.POST.get('job_title')
            Resume=request.FILES.get('Resume')
            Cover=request.POST.get('Cover')
            Skills=request.POST.get('Skills')
            job_Pic=request.FILES.get('job_Pic')

            apply=jobApplyModel(
                user=current_user,
                job_title=jobs,
                Skills=Skills,
                Resume=Resume,
                Cover=Cover,
                job_Pic=job_Pic,

               
            )
            apply.save()
            
            return redirect('jobfeed')

        return render(request,'apply_now.html',context)
    

def searchJob(request):
    
    query = request.GET.get('query')
    
    if query:
        
        jobs = JobModel.objects.filter(Q(job_title=query) 
                                       |Q(category=query)) 
                                       
    
    else:
        jobs = JobModel.objects.none()
        
    context={
        'jobs':jobs,
        'query':query
    }
    
    return render(request,"searchJob.html",context)

def editProfile(request): 
    current_user = request.user 
 
    if request.method == 'POST': 

        if request.FILES.get('Profile_Pic'):
            current_user.Profile_Pic = request.FILES.get('Profile_Pic')
             
        current_user.username = request.POST.get('username', current_user.username)
        current_user.email = request.POST.get('email', current_user.email)
        current_user.first_name = request.POST.get('first_name', current_user.first_name)
        current_user.last_name = request.POST.get('last_name', current_user.last_name)
        current_user.save() 
        return redirect('profilePage')
 
    return render(request,"editProfile.html")

def addSkill(req):

    current_user = req.user
    
    if req.method == 'POST':

        skills = seekerProfileModel.objects.get(user = current_user)
        skills.skills = req.POST.get('skills')
        skills.save()
        return redirect('profilePage')
    
    
    return render(req,'addSkill.html')


@login_required
def editSkill(req,):

    current_user = req.user

    
    seeker_profile = seekerProfileModel.objects.get(user=current_user)
    if req.method == 'POST':
        seeker_profile = seekerProfileModel.objects.get(user=current_user)
        seeker_profile.skills = req.POST.get('skills')
        seeker_profile.id=req.POST.get("skill_id")
        seeker_profile.save()
        
        return redirect('profilePage')
    context = {
        'seeker_data':seeker_profile, 
    }
    return render(req, 'edit_skill.html',context)

def skill_matchingPage(request):
    
    user=request.user
    
    mySkill=user.seekerProfile.skills
    jobs=JobModel.objects.filter(skills=mySkill)
    context={
        'jobs':jobs
    }
    print(mySkill)
    
    return render(request,"skill_matchingPage.html",context)




    
    
    
    