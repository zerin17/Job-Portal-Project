from django.db import models
from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):
    
    USER=[
        ('recruiter','Recruiter'),
        ('seeker','Seeker'),
    ]
    user_type=models.CharField(choices=USER,max_length=100,null=True)
    Profile_Pic=models.ImageField(upload_to='Media/Profile_Pic',null=True)
    contact_no=models.CharField(max_length=100,null=True)
    
    def __str__(self):   
        
        return f"{self.username}"
    
class seekerProfileModel(models.Model):
    SKILLS = [
        ('programming', 'Programming'),
        ('networking', 'Networking'),
        ('hardware', 'Hardware'),
    ]
    
    user=models.OneToOneField(customUser,on_delete=models.CASCADE,related_name='seekerProfile')
    skills = models.CharField(choices=SKILLS, max_length=100, null=True)
   
    def __str__(self):
        return f"{self.user.username}"
    
    
class recruiterProfileModel(models.Model):
    
    user = models.OneToOneField(customUser, on_delete=models.CASCADE,related_name='recruiterProfile')
    company_name = models.CharField(max_length=100, null=True)
   
    def __str__(self):
        return f"{self.user.username}--{self.company_name}"
    
class JobModel(models.Model):
    SKILLS = [
        ('programming', 'Programming'),
        ('networking', 'Networking'),
        ('hardware', 'Hardware'),
    ]


    JOB_TYPE_CHOICES=[
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('internship', 'Internship'),
    ]
    user=models.ForeignKey(customUser,null=True,blank=True,on_delete=models.CASCADE)

    job_title = models.CharField(max_length=200, null=True)  
    number_of_openings = models.PositiveIntegerField( null=True) 
    skills = models.CharField(choices=SKILLS, max_length=100, null=True)
    category = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES, null=True) 
    description = models.TextField(null=True, blank=True)  
    job_Pic=models.ImageField(upload_to='Media/job_Pic',null=True)

    def __str__(self):
        return f"{self.job_title} at {self.category}"
    

class jobApplyModel(models.Model):

    user=models.ForeignKey(customUser,on_delete=models.CASCADE,null=True)
    job_title=models.ForeignKey(JobModel,on_delete=models.CASCADE,null=True)
    Resume = models.FileField(upload_to="Media/Resume",max_length=200, null=True, blank=True) 
    Cover = models.TextField(null=True, blank=True) 
    Skills = models.CharField(max_length=200, null=True, blank=True) 
    job_Pic=models.ImageField(upload_to='Media/job_Pic',null=True)
    
    def __str__(self) -> str:
        return self.user.username