from django.shortcuts import render

from .models import *
from django.contrib.auth.decorators import login_required
from datetime import datetime


# Create your views here.

def index(request):
  return render(request, 'index.html')

def error_404(request):
  return render(request, '404.html')

def activity(request):
  return render(request, 'activity.html')

def about(request):
  return render(request, 'about.html')

def blog(request):
  return render(request, 'blog.html')

def careers(request):
  return render(request, 'careers.html')

def case_studies(request):
  return render(request, 'case-studies.html')


def collection(request,id):
  
  expertvideodetails = []
  expertwebinardetails = []
  expertpriorityDmdetails = []

  formatted_followers = "0"
  formatted_subscribers = "0"

  expert = ExpertUser.objects.get(id=id)
  
  if expert.followersCount is not None:
        try:
            followers_count = int(float(expert.followersCount))  
            if followers_count >= 1000000:
                formatted_followers = f"{followers_count / 1000000:.1f}".rstrip('0').rstrip('.') + "M"
            elif followers_count >= 1000:
                formatted_followers = f"{followers_count / 1000:.1f}".rstrip('0').rstrip('.') + "K"
            else:
                formatted_followers = str(followers_count)
        except ValueError:
            formatted_followers = "0"  

  if expert.subscribersCount is not None:
      try:
          subscribers_count = int(float(expert.subscribersCount))  
          if subscribers_count >= 1000000:
              formatted_subscribers = f"{subscribers_count / 1000000:.1f}".rstrip('0').rstrip('.') + "M"
          elif subscribers_count >= 1000:
              formatted_subscribers = f"{subscribers_count / 1000:.1f}".rstrip('0').rstrip('.') + "K"
          else:
              formatted_subscribers = str(subscribers_count)
      except ValueError:
          formatted_subscribers = "0"    

  
  expertvideosessiondetails =  ServiceVideoForm.objects.filter(expert=id)
  
  for expertvideosession in expertvideosessiondetails:
    expertvideodetails.append(expertvideosession)
    
  expertwebinarsessiondetails =  ServiceWebinarForm.objects.filter(expert=id)
  
  for expertwebinarsession in expertwebinarsessiondetails:
    expertwebinardetails.append(expertwebinarsession) 
      
  expertprioritydmsessiondetails =  ServicePriorityDmForm.objects.filter(expert=id)
  
  for expertprioritydmsession in expertprioritydmsessiondetails:
    expertpriorityDmdetails.append(expertprioritydmsession)   
    
  context = {
      "expert": expert,
      "formatted_followers": formatted_followers,
      "formatted_subscribers": formatted_subscribers,
      "expertvideosessiondetails": expertvideodetails,
      "expertwebinarsessiondetails": expertwebinardetails,
      "expertpriorityDmdetails": expertpriorityDmdetails,
  }
  
  return render(request, 'collection.html',context)

def collection_wide_sidebar(request):
  
  experts = ExpertUser.objects.all()
  
  return render(request, 'collections-wide-sidebar.html',{"experts":experts})

def collections(request):
  return render(request, 'collections.html')

def contact(request):
  return render(request, 'contact.html')

@login_required
def create(request):
  user = request.user
  return render(request, 'create.html',{'user':user})

def edit_profile(request):
  return render(request, 'edit-profile.html')

def help_center(request):
  return render(request, 'help-center.html')

def home_2(request):
  return render(request, 'home-2.html')

def home_3(request):
  return render(request, 'home-3.html')

def home_4(request):
  experts = ExpertUser.objects.exclude(id=None)
  return render(request, 'home-4.html',{"experts":experts})

def home_5(request):
  return render(request, 'home-5.html')

def home_6(request):
  return render(request, 'home-6.html')

def home_7(request):
  return render(request, 'home-7.html')

def home_8(request):
  return render(request, 'home-8.html')

def home_9(request):
  return render(request, 'home-9.html')

def home_10(request):
  return render(request, 'home-10.html')

def home_11(request):
  return render(request, 'home-11.html')

def home_12(request):
  return render(request, 'home-12.html')

def home_13(request):
  return render(request, 'home-13.html')

def index_rtl(request):
  return render(request, 'index-rtl.html')

def item(request):
  return render(request, 'item.html')

def landing(request):
  return render(request, 'landing.html')

def signup(request):
  return render(request, 'signup.html')

def login_view(request):
  return render(request, 'login.html')

def maintenance(request):
  return render(request, 'maintenance.html')

def newsletter(request):
  return render(request, 'newsletter.html')

def partners(request):
  return render(request, 'partners.html')

def platform_status(request):
  return render(request, 'platform-status.html')

def rankings(request):
  return render(request, 'rankings.html')

def single_case_study(request):
  return render(request, 'single-case-study.html')

def single_post(request):
  return render(request, 'single-post.html')

def tos(request):
  return render(request, 'tos.html')

def user(request):
  return render(request, 'user.html')

def wallet(request):
  return render(request, 'wallet.html')


def services(request):
  return render(request, 'services.html')

@login_required
def video(request):
  expertvideodetails = []
  expertvideosessiondetails =  ServiceVideoForm.objects.filter(expert = request.user.id)
  
  for expert in expertvideosessiondetails:
    expertvideodetails.append(expert)
  
  return render(request, 'video.html',{'expertvideosessiondetails':expertvideodetails})

def webinar(request):
  expertwebinardetails = []
  expertwebinarsessiondetails =  ServiceWebinarForm.objects.filter(expert = request.user.id)
  
  for expert in expertwebinarsessiondetails:
    expertwebinardetails.append(expert)
    
  return render(request, 'webinar.html',{'expertwebinarsessiondetails':expertwebinardetails})

def priorityDM(request):
  expertpriorityDmdetails = []
  expertprioritydmsessiondetails =  ServicePriorityDmForm.objects.filter(expert = request.user.id)
  
  for expert in expertprioritydmsessiondetails:
    expertpriorityDmdetails.append(expert)
  return render(request, 'priorityDM.html',{'expertpriorityDmdetails':expertpriorityDmdetails})


import requests
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail


User = get_user_model()

def verify_recaptcha(token):
    secret_key = settings.RECAPTCHA_SECRET_KEY  
    url = 'https://www.google.com/recaptcha/api/siteverify'
    response = requests.post(url, data={'secret': secret_key, 'response': token})
    result = response.json()
    return result.get('success', False)

@csrf_exempt
def signup_api(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')

        email = request.POST.get('email')
        yourusername = request.POST.get('username')
        contact_number = request.POST.get('contact_number')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        recaptcha_token = request.POST.get('recaptcha_token')

        if not verify_recaptcha(recaptcha_token):
            return JsonResponse({'error': 'Invalid reCAPTCHA. Please try again.'}, status=400)

        if password != password2:
            return JsonResponse({'error': 'Passwords do not match.'}, status=400)

        if User.objects.filter(email=email).exists():
                return JsonResponse({"email": ["Email already in use."]}, status=400)
       
        try:
            user = User(firstname=firstname,
                        lastname=lastname,  
                        email=email,
                        contact_number=contact_number,
                        yourusername= yourusername
                        )
            user.set_password(password)
            if request.POST.get('youtubelink'):
                user.youtubelink = request.POST.get('youtubelink')
            if request.POST.get('instagramlink'):
                user.instagramlink = request.POST.get('instagramlink')
            if request.POST.get('subscribersCount'):
                user.subscribersCount = int(request.POST.get('subscribersCount'))
            if request.POST.get('followersCount'):
                user.followersCount = int(request.POST.get('followersCount'))
            user.save()
            
            send_mail(
               subject=f"Welcome {firstname} - Complete Your Profile Now!",
                message=f"Your account has been successfully created! To enjoy a hassle-free experience and connect with more of your audience, please complete your profile now.",
                from_email="xhibiter@gmail.com",  
                recipient_list=[email],  
                fail_silently=False,  
            )

            return JsonResponse({'message': 'Registration successful!','redirect_url': '/login/'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
          
          
@csrf_exempt
def login_api(request):
    if request.method == "POST":
        email_or_contact = request.POST.get("email_or_contact")
        password = request.POST.get("password")
        recaptcha_token = request.POST.get("recaptcha_token")
        
        print('email', email_or_contact)
        print('password', password)

        # Verify reCAPTCHA token
        if not verify_recaptcha(recaptcha_token):
            return JsonResponse({'error': 'Invalid reCAPTCHA. Please try again.'}, status=400)

        # Authenticate the user
        user = authenticate(request, username=email_or_contact, password=password)

        # Redirect based on user type
        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful', 'redirect_url': '/create/'})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=400)
          


from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    if request.user.is_authenticated:
            logout(request)
            return redirect('login')  
    return redirect('login')  
            
            

def check_username(request):
    yourusername = request.GET.get("username", "").strip()
    exists = ExpertUser.objects.filter(yourusername=yourusername).exists()
    return JsonResponse({"exists": exists})
            

      
@login_required
@csrf_exempt
def update_profile_details_api(request):
    if request.method == 'POST':
        expert = User.objects.get(id=request.user.id)  
        
        

        if  request.POST.get('username'):
            expert.username = request.POST.get('username')
        if request.POST.get('firstname'):
            expert.firstname = request.POST.get('firstname')
        if request.POST.get('lastname'):
            expert.lastname =  request.POST.get('lastname')
        
        if  request.POST.get('displayname'):
            expert.displayname = request.POST.get('displayname')
        if request.POST.get('introduction'):
            expert.introduction = request.POST.get('introduction')
        if request.POST.get('aboutyourself'):
            expert.aboutyourself =  request.POST.get('aboutyourself')
        if request.POST.get('youtubeLink'):
            expert.youtubeLink =  request.POST.get('youtubeLink')
        
        if request.POST.get('instagramLink'):
            expert.instagramLink =  request.POST.get('instagramLink')
        
        if request.POST.get('followersCount'):
            expert.followersCount =  request.POST.get('followersCount')            
            
        if  request.POST.get('subscribersCount'):
            expert.subscribersCount = request.POST.get('subscribersCount')
    

        if 'profile_picture' in request.FILES:
            expert.profile_picture = request.FILES['profile_picture']
            
        expert.save()


        return JsonResponse({'message': ' details updated successfully'})

    return JsonResponse({'error': 'Invalid request method'}, status=405)
 

@login_required
@csrf_exempt
def update_account_details_api(request):
    if request.method == 'POST':
        expert = User.objects.get(id=request.user.id)  
        
        

        if  request.POST.get('email'):
            expert.email = request.POST.get('email')
        if request.POST.get('contact_number'):
            expert.contact_number = request.POST.get('contact_number')
        
        dob_input = request.POST.get('dob')
        
        if dob_input:
            try:
                dob = datetime.strptime(dob_input, '%Y-%m-%d').date()
                expert.dob = dob
            except ValueError:
                return JsonResponse({'error': 'Invalid date format. It must be in YYYY-MM-DD format.'}, status=400)    
        
        if  request.POST.get('state'):
            expert.state = request.POST.get('state')
        if request.POST.get('city'):
            expert.city = request.POST.get('city')
        if request.POST.get('personalAddress'):
            expert.personalAddress =  request.POST.get('personalAddress')
        if request.POST.get('officeAddress'):
            expert.officeAddress =  request.POST.get('officeAddress')
        
        if request.POST.get('alternateContactNumber'):
            expert.alternateContactNumber =  request.POST.get('alternateContactNumber')
        
        if request.POST.get('alternateEmail'):
            expert.alternateEmail =  request.POST.get('alternateEmail')            
            
            
        expert.save()


        return JsonResponse({'message': ' details updated successfully'})

    return JsonResponse({'error': 'Invalid request method'}, status=405)
   
   
   

@login_required
@csrf_exempt
def serviceVideo_api(request):
    if request.method == 'POST':
        try:
            expert = ExpertUser.objects.get(id=request.user.id)  
            title = request.POST.get('title')
            duration = request.POST.get('duration')
            amount = request.POST.get('amount')

            if not title or not duration or not amount:
                return JsonResponse({'error': 'All fields are required (title, duration, amount).'}, status=400)

            service_video = ServiceVideoForm.objects.create(
                expert=expert,
                title=title,
                duration=duration,
                amount=amount
            )

            return JsonResponse({
                'message': 'Service video created successfully!',
                'service_id': service_video.id
            }, status=201)

        except ExpertUser.DoesNotExist:
            return JsonResponse({'error': 'Expert user not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
  
  

@login_required
@csrf_exempt
def serviceWebinar_api(request):
    if request.method == 'POST':
        try:
            expert = ExpertUser.objects.get(id=request.user.id)  
            title = request.POST.get('title')
            duration = request.POST.get('duration')
            amount = request.POST.get('amount')
            session_date = request.POST.get('session_date')
            session_time = request.POST.get('session_time')


            if not title or not duration or not amount or not session_date or not session_time:
                return JsonResponse({'error': 'All fields are required (title, duration, amount).'}, status=400)

            try:
                session_date = datetime.strptime(session_date,'%Y-%m-%d').date()
            except ValueError:
                return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)

            try:
                session_time = datetime.strptime(session_time + ":00", '%H:%M:%S').time()
            except ValueError:
                return JsonResponse({'error': 'Invalid time format. Use HH:MM.'}, status=400)

            service_webinar = ServiceWebinarForm.objects.create(
                expert=expert,
                title=title,
                duration=duration,
                amount=amount,
                session_date=session_date,
                session_time=session_time
            )
            return JsonResponse({
                'message': 'Service video created successfully!',
                'service_id': service_webinar.id
            }, status=201)


        except ExpertUser.DoesNotExist:
            return JsonResponse({'error': 'Expert user not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
      
   

@login_required
@csrf_exempt
def servicePrioritydm_api(request):
    if request.method == 'POST':
        try:
            expert = ExpertUser.objects.get(id=request.user.id)  
            title = request.POST.get('title')
            amount = request.POST.get('amount')

            if not title or   not amount:
                return JsonResponse({'error': 'All fields are required (title, duration, amount).'}, status=400)

            service_prioritydm = ServicePriorityDmForm.objects.create(
                expert=expert,
                title=title,
                amount=amount
            )

            return JsonResponse({
                'message': 'Service video created successfully!',
                'service_id': service_prioritydm.id
            }, status=201)

        except ExpertUser.DoesNotExist:
            return JsonResponse({'error': 'Expert user not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
  
  
@csrf_exempt
def deletevideoSession_api(request,id):
  
  if request.method=="POST":
    
    videosession = ServiceVideoForm.objects.filter(id=id)
    
    videosession.delete()
    
    return JsonResponse({"message":"record deleted successfully"})
    
  return JsonResponse({"error":'invalid request method'},status=405)  


  
@csrf_exempt
def deletewebinarSession_api(request,id):
  
  if request.method=="POST":
    
    webinarsession = ServiceWebinarForm.objects.filter(id=id)
    
    webinarsession.delete()
    
    return JsonResponse({"message":"record deleted successfully"})
    
  return JsonResponse({"error":'invalid request method'},status=405) 



  
@csrf_exempt
def deleteprioritydmSession_api(request,id):
  
  if request.method=="POST":
    
    prioritydmsession = ServicePriorityDmForm.objects.filter(id=id)
    
    prioritydmsession.delete()
    
    return JsonResponse({"message":"record deleted successfully"})
    
  return JsonResponse({"error":'invalid request method'},status=405)  


@csrf_exempt
def updateVideoSession_api(request):
  
  if request.method=="POST":
    id = request.POST.get("id")
    title = request.POST.get("title")
    duration = request.POST.get("duration")
    amount = request.POST.get("amount")




    videosession = ServiceVideoForm.objects.get(id=id)
    videosession.title = title
    videosession.duration = duration
    videosession.amount = amount
    videosession.save()
    
    
    
    return JsonResponse({"message":"record updated successfully"})
    
  return JsonResponse({"error":'invalid request method'},status=405)  





@csrf_exempt
def updateWebinarSession_api(request):
  
  if request.method=="POST":
    id = request.POST.get("id")
    title = request.POST.get("title")
    duration = request.POST.get("duration")
    amount = request.POST.get("amount")
    session_date = request.POST.get('session_date')
    session_time = request.POST.get('session_time')


   

    try:
        session_date = datetime.strptime(session_date,'%Y-%m-%d').date()
    except ValueError:
        return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)

    try:
        session_time = datetime.strptime(session_time + ":00", '%H:%M:%S').time()
    except ValueError:
        return JsonResponse({'error': 'Invalid time format. Use HH:MM.'}, status=400)




    webinarsession = ServiceWebinarForm.objects.get(id=id)
    webinarsession.title = title
    webinarsession.duration = duration
    webinarsession.amount = amount
    webinarsession.session_date=session_date
    webinarsession.session_time= session_time
    webinarsession.save()
    
    
    
    return JsonResponse({"message":"record updated successfully"})
    
  return JsonResponse({"error":'invalid request method'},status=405) 



@csrf_exempt
def updatePriorityDmSession_api(request):
  
  if request.method=="POST":
    id = request.POST.get("id")
    title = request.POST.get("title")
    amount = request.POST.get("amount")




    priorityDmsession = ServicePriorityDmForm.objects.get(id=id)
    priorityDmsession.title = title
    priorityDmsession.amount = amount
    priorityDmsession.save()
    
    
    
    return JsonResponse({"message":"record updated successfully"})
    
  return JsonResponse({"error":'invalid request method'},status=405) 


  


  
    
    
      
        
  
      
   