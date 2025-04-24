from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin

from django.utils.text import slugify
from django.urls import reverse

class UserProfileManager(BaseUserManager):
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
    

class UserProfile(AbstractBaseUser,PermissionsMixin):
    
    
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
    is_creator = models.BooleanField(default=False)
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
    slug = models.SlugField(unique=True, blank=True, null=True)  # NEW


    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['contact_number']

    def __str__(self):
        return self.firstname
    
    def save(self, *args, **kwargs):
        if self.is_creator and not self.slug:
            base_slug = slugify(self.yourusername or self.displayname or self.firstname)
            self.slug = base_slug
            counter = 1
            while UserProfile.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
                self.slug = f"{base_slug}-{counter}"
                counter += 1
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        if self.is_creator:
            return reverse('creator_profile', kwargs={'slug': self.slug})
        return "#"

    
class ServiceVideoForm(models.Model):
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE) 
    slug = models.SlugField(unique=True, blank=True)
    bufferTime = models.CharField(max_length=20,null=True,blank=True)
    maxBookings = models.CharField(max_length=20,null=True,blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True,default="")
    duration = models.CharField(max_length=2,null=True,blank=True)
    amount = models.CharField(max_length=7,null=True,blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)  
    selectedDates = models.CharField(max_length=255,null=True,blank=True)
    selectedTime = models.CharField(max_length=255,null=True,blank=True)

    def save(self, *args, **kwargs):
        old_slug = None
        old_title = None

        if self.pk:
            old_instance = ServiceVideoForm.objects.get(pk=self.pk)
            old_slug = old_instance.slug
            old_title = old_instance.title

        if self.title and (not self.slug or self.title != old_title):
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while ServiceSlugRouter.objects.filter(slug=slug).exclude(object_id=self.id).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        super().save(*args, **kwargs)

        ServiceSlugRouter.objects.update_or_create(
            slug=self.slug,
            defaults={'model_type': 'video', 'object_id': self.id}
        )

        if old_slug and old_slug != self.slug:
            ServiceSlugRouter.objects.filter(slug=old_slug, object_id=self.id).delete()

    def get_absolute_url(self):
        return reverse('item', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title} - {self.creator}"

    
    
class ServicePriorityDmForm(models.Model):
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True) 
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True,default="")
    amount = models.CharField(max_length=7,null=True,blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)  

    def save(self, *args, **kwargs):
        old_slug = None
        old_title = None

        if self.pk:
            old_instance = ServicePriorityDmForm.objects.get(pk=self.pk)
            old_slug = old_instance.slug
            old_title = old_instance.title

       
        if self.title and (not self.slug or self.title != old_title):
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while ServiceSlugRouter.objects.filter(slug=slug).exclude(object_id=self.id).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        super().save(*args, **kwargs)

        ServiceSlugRouter.objects.update_or_create(
            slug=self.slug,
            defaults={'model_type': 'priority', 'object_id': self.id}
        )

        if old_slug and old_slug != self.slug:
            ServiceSlugRouter.objects.filter(slug=old_slug, object_id=self.id).delete()

    def get_absolute_url(self):
        return reverse('item', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title} - {self.creator}"
    
    
class ServiceWebinarForm(models.Model):
    creator = models.ForeignKey(UserProfile, on_delete=models.CASCADE) 
    slug = models.SlugField(unique=True, blank=True)
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.TextField(null=True,blank=True,default="")
    duration = models.CharField(max_length=2,null=True,blank=True)
    session_time = models.TimeField(null=True,blank=True)
    session_date = models.DateField(null=True,blank=True)
    amount = models.CharField(max_length=7,null=True,blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)  

    def save(self, *args, **kwargs):
        old_slug = None
        old_title = None

        if self.pk:
            old_instance = ServiceWebinarForm.objects.get(pk=self.pk)
            old_slug = old_instance.slug
            old_title = old_instance.title

       
        if self.title and (not self.slug or self.title != old_title):
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            while ServiceSlugRouter.objects.filter(slug=slug).exclude(object_id=self.id).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug

        super().save(*args, **kwargs)

        ServiceSlugRouter.objects.update_or_create(
            slug=self.slug,
            defaults={'model_type': 'webinar', 'object_id': self.id}
        )

        if old_slug and old_slug != self.slug:
            ServiceSlugRouter.objects.filter(slug=old_slug, object_id=self.id).delete()

    def get_absolute_url(self):
        return reverse('item', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.title} - {self.creator}"             
    
    
 
class BookingStatus(models.Model):
    session_id = models.IntegerField(null=True,blank=True)  
    session_title =  models.CharField(max_length=255,null=True,blank=True)
    session_name = models.CharField(max_length=7,null=True,blank=True)
    selectedTime = models.TimeField(null=True,blank=True)
    selectedDate = models.DateField(null=True,blank=True)  
    additionalDetails = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=7,null=True,blank=True)   
    user_id = models.IntegerField(null=True,blank=True)
    creator_id  = models.IntegerField(null=True,blank=True)
    
    
# models.py
from django.db import models

class ServiceSlugRouter(models.Model):
    slug = models.SlugField(unique=True)
    model_type = models.CharField(max_length=50)
    object_id = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.slug} ({self.model_type})"
    
    