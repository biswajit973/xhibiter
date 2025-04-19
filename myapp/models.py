from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin



class ExpertUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    

class ExpertUser(AbstractBaseUser,PermissionsMixin):
    
    
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)
    youtubelink = models.URLField(max_length=300,null=True, blank=True)
    instagramlink = models.URLField(max_length=300,null=True, blank=True)
    subscribersCount = models.BigIntegerField(null=True, blank=True) 
    followersCount = models.BigIntegerField(null=True, blank=True)  
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_expert = models.BooleanField(default=False)
    delete1 = models.IntegerField(default=0)
    yourusername = models.CharField(max_length=100,null=True,blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    displayname = models.CharField(max_length=100,null=True,blank=True)
    introduction = models.CharField(max_length=500,null=True,blank=True)
    aboutyourself = models.CharField(max_length=500,null=True,blank=True)
    dob = models.DateField(null=True,blank=True)
    state = models.CharField(max_length=50,null=True,blank=True)
    city = models.CharField(max_length=50,null=True,blank=True)
    personalAddress = models.CharField(max_length=500,null=True,blank=True)
    officeAddress = models.CharField(max_length=500,null=True,blank=True)
    alternateContactNumber = models.CharField(max_length=11,null=True,blank=True)
    alternateEmail = models.CharField(max_length=50,null=True,blank=True)


    objects = ExpertUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['contact_number']

    def __str__(self):
        return self.firstname

    
class ServiceVideoForm(models.Model):
    expert = models.ForeignKey(ExpertUser, on_delete=models.CASCADE) 
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True,default="")
    duration = models.CharField(max_length=2,null=True,blank=True)
    amount = models.CharField(max_length=7,null=True,blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.title} - {self.expert}" 
    
class ServicePriorityDmForm(models.Model):
    expert = models.ForeignKey(ExpertUser, on_delete=models.CASCADE) 
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True,default="")

    amount = models.CharField(max_length=7,null=True,blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.title} - {self.expert}" 
    
    
class ServiceWebinarForm(models.Model):
    expert = models.ForeignKey(ExpertUser, on_delete=models.CASCADE) 
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True,default="")
    duration = models.CharField(max_length=2,null=True,blank=True)
    session_time = models.TimeField(null=True,blank=True)
    session_date = models.DateField(null=True,blank=True)
    amount = models.CharField(max_length=7,null=True,blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.title} - {self.expert}"             
    
    
 
class BookingStatus(models.Model):
    session_id = models.IntegerField(max_length=100,null=True,blank=True)  
    session_name = models.CharField(max_length=7,null=True,blank=True)
    selectedTime = models.TimeField(null=True,blank=True)
    selectedDate = models.DateField(null=True,blank=True)  
    status = models.CharField(max_length=7,null=True,blank=True)   
    user_id = models.IntegerField(max_length=100,null=True,blank=True)
    expert_id  = models.IntegerField(max_length=100,null=True,blank=True)