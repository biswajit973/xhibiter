import calendar
import json
from django.shortcuts import render

from .models import *
from django.contrib.auth.decorators import login_required
from datetime import datetime

from django.http import Http404
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


def collection(request,slug):
  
  creatorvideodetails = []
  creatorwebinardetails = []
  creatorpriorityDmdetails = []

  formatted_followers = "0"
  formatted_subscribers = "0"

  creator = get_object_or_404(UserProfile, slug=slug, is_creator=True)
  id = creator.id
  
  if creator.followersCount is not None:
        try:
            followers_count = int(float(creator.followersCount))  
            if followers_count >= 1000000:
                formatted_followers = f"{followers_count / 1000000:.1f}".rstrip('0').rstrip('.') + "M"
            elif followers_count >= 1000:
                formatted_followers = f"{followers_count / 1000:.1f}".rstrip('0').rstrip('.') + "K"
            else:
                formatted_followers = str(followers_count)
        except ValueError:
            formatted_followers = "0"  

  if creator.subscribersCount is not None:
      try:
          subscribers_count = int(float(creator.subscribersCount))  
          if subscribers_count >= 1000000:
              formatted_subscribers = f"{subscribers_count / 1000000:.1f}".rstrip('0').rstrip('.') + "M"
          elif subscribers_count >= 1000:
              formatted_subscribers = f"{subscribers_count / 1000:.1f}".rstrip('0').rstrip('.') + "K"
          else:
              formatted_subscribers = str(subscribers_count)
      except ValueError:
          formatted_subscribers = "0"    

  
  creatorvideosessiondetails =  ServiceVideoForm.objects.filter(creator=id)
  
  for creatorvideosession in creatorvideosessiondetails:
    creatorvideodetails.append(creatorvideosession)
    
  creatorwebinarsessiondetails =  ServiceWebinarForm.objects.filter(creator=id)
  
  for creatorwebinarsession in creatorwebinarsessiondetails:
    creatorwebinardetails.append(creatorwebinarsession) 
      
  creatorprioritydmsessiondetails =  ServicePriorityDmForm.objects.filter(creator=id)
  
  for creatorprioritydmsession in creatorprioritydmsessiondetails:
    creatorpriorityDmdetails.append(creatorprioritydmsession)   
    
  context = {
      "creator": creator,
      "formatted_followers": formatted_followers,
      "formatted_subscribers": formatted_subscribers,
      "creatorvideosessiondetails": creatorvideodetails,
      "creatorwebinarsessiondetails": creatorwebinardetails,
      "creatorpriorityDmdetails": creatorpriorityDmdetails,
  }
  
  return render(request, 'collection.html',context)

def collection_wide_sidebar(request):
  
  user= request.user.id
  creators = UserProfile.objects.filter(is_creator=True).exclude(id=user)
  
  return render(request, 'collections-wide-sidebar.html',{"creators":creators})

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
  user= request.user.id
  creators = UserProfile.objects.filter(is_creator=True).exclude(id=user)
  return render(request, 'home-4.html',{"creators":creators})

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

# def item(request):
#   return render(request, 'item.html')

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

@login_required
def create_service(request):
    try:
        profile = UserProfile.objects.get(id=request.user.id)
    except UserProfile.DoesNotExist:
        raise Http404("Page not found.")

    if not profile.is_creator:
        raise Http404("Page not found.")

    
    return render(request, 'create-service.html')

@login_required
def video(request):
  creatorvideodetails = []
  
  try:
        profile = UserProfile.objects.get(id=request.user.id)
  except UserProfile.DoesNotExist:
        raise Http404("Page not found.")

  if not profile.is_creator:
        raise Http404("Page not found.")
    
  creatorvideosessiondetails =  ServiceVideoForm.objects.filter(creator = request.user.id)
  
  for creator in creatorvideosessiondetails:
    creatorvideodetails.append(creator)
  
  return render(request, 'video.html',{'creatorvideosessiondetails':creatorvideodetails})

def webinar(request):
  creatorwebinardetails = []
  try:
        profile = UserProfile.objects.get(id=request.user.id)
  except UserProfile.DoesNotExist:
        raise Http404("Page not found.")

  if not profile.is_creator:
        raise Http404("Page not found.")
  creatorwebinarsessiondetails =  ServiceWebinarForm.objects.filter(creator = request.user.id)
  
  for creator in creatorwebinarsessiondetails:
    creatorwebinardetails.append(creator)
    
  return render(request, 'webinar.html',{'creatorwebinarsessiondetails':creatorwebinardetails})

def priorityDM(request):
  creatorpriorityDmdetails = []
  try:
        profile = UserProfile.objects.get(id=request.user.id)
  except UserProfile.DoesNotExist:
        raise Http404("Page not found.")

  if not profile.is_creator:
        raise Http404("Page not found.")

  creatorprioritydmsessiondetails =  ServicePriorityDmForm.objects.filter(creator = request.user.id)
  
  for creator in creatorprioritydmsessiondetails:
    creatorpriorityDmdetails.append(creator)
  return render(request, 'priorityDM.html',{'creatorpriorityDmdetails':creatorpriorityDmdetails})


import requests
from django.conf import settings
from django.http import HttpResponseForbidden, JsonResponse
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
        
        creator_recaptcha_token = request.POST.get('creator_recaptcha_token')

        if not verify_recaptcha(creator_recaptcha_token):
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
                        yourusername= yourusername,
                        is_creator = True
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
        next_url = request.POST.get("next", "/create/") 
        
        print('email', email_or_contact)
        print('password', password)

        # Verify reCAPTCHA token
        if not verify_recaptcha(recaptcha_token):
            return JsonResponse({'error': 'Invalid reCAPTCHA. Please try again.'}, status=400)

        user = authenticate(request, username=email_or_contact, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'message': 'Login successful', 'redirect_url': next_url})
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
    exists = UserProfile.objects.filter(yourusername=yourusername).exists()
    return JsonResponse({"exists": exists})
            

      
@login_required
@csrf_exempt
def update_profile_details_api(request):
    if request.method == 'POST':
        creator = User.objects.get(id=request.user.id)  
      
        if  request.POST.get('username'):
            creator.username = request.POST.get('username')
        if request.POST.get('firstname'):
            creator.firstname = request.POST.get('firstname')
        if request.POST.get('lastname'):
            creator.lastname =  request.POST.get('lastname')
        
        if  request.POST.get('displayname'):
            creator.displayname = request.POST.get('displayname')
        if request.POST.get('introduction'):
            creator.introduction = request.POST.get('introduction')
        if request.POST.get('aboutyourself'):
            creator.aboutyourself =  request.POST.get('aboutyourself')
        if request.POST.get('youtubeLink'):
            creator.youtubeLink =  request.POST.get('youtubeLink')
        
        if request.POST.get('instagramLink'):
            creator.instagramLink =  request.POST.get('instagramLink')
        
        if request.POST.get('followersCount'):
            creator.followersCount =  request.POST.get('followersCount')            
            
        if  request.POST.get('subscribersCount'):
            creator.subscribersCount = request.POST.get('subscribersCount')
    

        if 'profile_picture' in request.FILES:
            creator.profile_picture = request.FILES['profile_picture']
            
        creator.save()


        return JsonResponse({'message': ' details updated successfully'})

    return JsonResponse({'error': 'Invalid request method'}, status=405)
 

@login_required
@csrf_exempt
def update_account_details_api(request):
    if request.method == 'POST':
        creator = User.objects.get(id=request.user.id)  
        
        if request.POST.get('contact_number'):
            creator.contact_number = request.POST.get('contact_number')
        
        dob_input = request.POST.get('dob')
        
        if dob_input:
            try:
                dob = datetime.strptime(dob_input, '%Y-%m-%d').date()
                creator.dob = dob
            except ValueError:
                return JsonResponse({'error': 'Invalid date format. It must be in YYYY-MM-DD format.'}, status=400)    
        
        if  request.POST.get('state'):
            creator.state = request.POST.get('state')
        if request.POST.get('city'):
            creator.city = request.POST.get('city')
        if request.POST.get('personalAddress'):
            creator.personalAddress =  request.POST.get('personalAddress')
        if request.POST.get('officeAddress'):
            creator.officeAddress =  request.POST.get('officeAddress')
        
        if request.POST.get('alternateContactNumber'):
            creator.alternateContactNumber =  request.POST.get('alternateContactNumber')
        
        if request.POST.get('alternateEmail'):
            creator.alternateEmail =  request.POST.get('alternateEmail')            
            
            
        creator.save()


        return JsonResponse({'message': ' details updated successfully'})

    return JsonResponse({'error': 'Invalid request method'}, status=405)
   
   
   

@login_required
@csrf_exempt
def serviceVideo_api(request):
    if request.method == 'POST':
        try:
            creator = UserProfile.objects.get(id=request.user.id)  
            title = request.POST.get('title')
            description = request.POST.get('description')
            duration = request.POST.get('duration')
            amount = request.POST.get('amount')
            
            bufferTime = request.POST.get('bufferTime')
            maxBookings = request.POST.get('maxBookings')
            if not title or not duration or not amount or not bufferTime or not maxBookings :
                return JsonResponse({'error': 'All fields are required (title, duration, amount, date, time, timezone).'}, status=400)

            service_video = ServiceVideoForm.objects.create(
                creator=creator,
                title=title,
                description = description,
                duration=duration,
                amount=amount,
                bufferTime=bufferTime,
                maxBookings=maxBookings,
                
            )

            return JsonResponse({
                'message': 'Service video created successfully!',
                'service_id': service_video.id
            }, status=201)

        except UserProfile.DoesNotExist:
            return JsonResponse({'error': 'creator user not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
  
  

@login_required
@csrf_exempt
def serviceWebinar_api(request):
    if request.method == 'POST':
        try:
            creator = UserProfile.objects.get(id=request.user.id)  
            title = request.POST.get('title')
            description = request.POST.get('description')
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
                creator=creator,
                title=title,
                description =description,
                duration=duration,
                amount=amount,
                session_date=session_date,
                session_time=session_time
            )
            return JsonResponse({
                'message': 'Service video created successfully!',
                'service_id': service_webinar.id
            }, status=201)


        except UserProfile.DoesNotExist:
            return JsonResponse({'error': 'creator user not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
      
   

@login_required
@csrf_exempt
def servicePrioritydm_api(request):
    if request.method == 'POST':
        try:
            creator = UserProfile.objects.get(id=request.user.id)  
            title = request.POST.get('title')
            description = request.POST.get('description')
            amount = request.POST.get('amount')

            if not title or   not amount:
                return JsonResponse({'error': 'All fields are required (title, duration, amount).'}, status=400)

            service_prioritydm = ServicePriorityDmForm.objects.create(
                creator=creator,
                title=title,
                description = description,
                amount=amount
            )

            return JsonResponse({
                'message': 'Service video created successfully!',
                'service_id': service_prioritydm.id
            }, status=201)

        except UserProfile.DoesNotExist:
            return JsonResponse({'error': 'creator user not found.'}, status=404)
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
    description = request.POST.get('description')
    duration = request.POST.get("duration")
    amount = request.POST.get("amount")
    
    bufferTime = request.POST.get("bufferTime")
    maxBookings = request.POST.get("maxBookings")
    
    
    videosession = ServiceVideoForm.objects.get(id=id)
    videosession.title = title
    videosession.description = description
    videosession.duration = duration
    videosession.amount = amount
    
    videosession.bufferTime = bufferTime
    videosession.maxBookings = maxBookings
    videosession.save()
    
    
    
    return JsonResponse({"message":"record updated successfully"})
    
  return JsonResponse({"error":'invalid request method'},status=405)  





@csrf_exempt
def updateWebinarSession_api(request):
  
  if request.method=="POST":
    id = request.POST.get("id")
    title = request.POST.get("title")
    description = request.POST.get('description')
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
    webinarsession.description = description
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
    description = request.POST.get('description')
    amount = request.POST.get("amount")




    priorityDmsession = ServicePriorityDmForm.objects.get(id=id)
    priorityDmsession.title = title
    priorityDmsession.description = description
    priorityDmsession.amount = amount
    priorityDmsession.save()
    
    
    
    return JsonResponse({"message":"record updated successfully"})
    
  return JsonResponse({"error":'invalid request method'},status=405) 

from django.shortcuts import render, get_object_or_404

def item(request, slug):
    slug_entry = get_object_or_404(ServiceSlugRouter, slug=slug)
    
    model_map = {
        'video': ServiceVideoForm,
        'webinar': ServiceWebinarForm,
        'priority': ServicePriorityDmForm,
    }
    label_map = {
        'video': 'Video',
        'webinar': 'Webinar',
        'priority': 'Priority Demo',
    }

    model_class = model_map.get(slug_entry.model_type)
    if not model_class:
        return render(request,status=404)

    item = get_object_or_404(model_class, pk=slug_entry.object_id)
    model_type_label = label_map.get(slug_entry.model_type, 'Service')
    
    if hasattr(item, 'slug') and item.slug and hasattr(item, 'bufferTime') and item.bufferTime:
        session_type = "open"
        
    elif hasattr(item, 'session_date') and item.session_date and hasattr(item, 'session_time') and item.session_time:
        session_type = "fixed"
    else:
        session_type = "none"

    return render(request, 'item.html', {'item': item,'model_type': slug_entry.model_type,
        'model_type_label': model_type_label,'session_type': session_type})

@csrf_exempt
def buyer_signup_api(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')

        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        buyer_recaptcha_token = request.POST.get('buyer_recaptcha_token')

        if not verify_recaptcha(buyer_recaptcha_token):
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
                        is_creator = False
                        )
            user.set_password(password)
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
          


from datetime import datetime
@csrf_exempt
def book_video_session_api(request):
    
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required'}, status=401)

    session_date = None
    session_time = None
    user = request.user 
    user_id = user.id

    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        session_title = request.POST.get('session_title')
        session_name = request.POST.get('session_name')

        if request.POST.get('selectedDate'):
            selected_date = request.POST.get('selectedDate')  
            session_date = datetime.strptime(selected_date, "%Y-%m-%d").date()

        if request.POST.get('selectedTime'):
            selected_time = request.POST.get('selectedTime')  
            session_time = datetime.strptime(selected_time, "%I:%M %p").time()

        creator_id = request.POST.get('creator_id')
        print("creator_id",creator_id)
        
        if str(user_id) == str(creator_id):
            return JsonResponse({'error': "You cannot book your own session."}, status=403)
        
        if session_name == 'Video':
            creator_session = ServiceVideoForm.objects.filter(id=session_id, creator_id=creator_id).first()
       
        print("creator_session",creator_session)
       
        print("session_id",session_id,session_title)
        if not creator_session:
            return JsonResponse({'error': 'session not found or unavailable.'}, status=400)
        
        day_name = calendar.day_name[session_date.weekday()]
        availability = Availability.objects.filter(creator_id=creator_id, day=day_name).first()

        if not availability:
            return JsonResponse({'error': 'Creator is not available on this day.'}, status=400)

        if not (availability.from_time <= session_time <= availability.to_time):
            return JsonResponse({'error': 'Selected time is outside of creator’s available hours.'}, status=400)

        if request.POST.get('additionalDetails'):
            additionalDetails = request.POST.get('additionalDetails')  
    
        existing_booking = BookingStatus.objects.filter(
            session_id=session_id,
            selectedDate=session_date,
            selectedTime=session_time,
        ).exists()

        if existing_booking:
            return JsonResponse({'error': 'This slot is already booked. Please choose another.'}, status=400)

        booking_status = BookingStatus.objects.create(
            user_id=user_id,
            session_title=session_title,
            session_id=session_id,
            session_name=session_name,
            selectedDate=session_date,
            selectedTime=session_time,
            additionalDetails=additionalDetails,
            status="success",
            creator_id=creator_id,
        )


        

        try:
            creator = UserProfile.objects.get(id=creator_id)
        except UserProfile.DoesNotExist:
            return JsonResponse({'error': 'Creator not found'}, status=404)

        formatted_date = session_date.strftime('%B %d, %Y')
        formatted_time = session_time.strftime('%I:%M %p')

        creator_subject = "New Session Booking Alert"
        creator_message = f"""
Hello {creator.firstname},

{user.firstname} {user.lastname} has booked your session.

Session Title: {session_title}
Date: {formatted_date}
Time: {formatted_time}

Please log in to your dashboard to view details.

Thank you!
"""
        send_mail(
            subject=creator_subject,
            message=creator_message,
            from_email='xhibiter@gmail.com',
            recipient_list=[creator.email],
            fail_silently=False,
        )

        user_subject = "Session Booking Confirmation"
        user_message = f"""
Hello {user.firstname} {user.lastname},

Your session booking with {creator.firstname} {creator.lastname} is confirmed.

Session Title: {session_title}
Date: {formatted_date}
Time: {formatted_time}

Thank you for booking!

Best regards,
Team
"""
        send_mail(
            subject=user_subject,
            message=user_message,
            from_email='xhibiter@gmail.com',
            recipient_list=[user.email],
            fail_silently=False,
        )

        return JsonResponse({'message': 'Booking successful', 'booking_id': booking_status.id}, status=201)

    return JsonResponse({'error': 'Invalid request method'}, status=400)



import pytz
from django.utils.timezone import make_aware, localtime
from datetime import datetime
@csrf_exempt
def book_webinar_session_api(request):
    
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required'}, status=401)

    session_date = None
    session_time = None
    user = request.user 
    user_id = user.id

    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        session_title = request.POST.get('session_title')
        session_name = request.POST.get('session_name')
        

        if request.POST.get('selectedDate'):
            selected_date = request.POST.get('selectedDate')  
            session_date = datetime.strptime(selected_date, "%Y-%m-%d").date()

        if request.POST.get('selectedTime'):
            selected_time = request.POST.get('selectedTime')  
            session_time = datetime.strptime(selected_time, "%I:%M %p").time()

        creator_id = request.POST.get('creator_id')
        print("creator_id",creator_id)
        
        if str(user_id) == str(creator_id):
            return JsonResponse({'error': "You cannot book your own session."}, status=403)
       
        creator_session = None
        
        if session_name == 'Webinar':
            creator_session = ServiceWebinarForm.objects.filter(id=session_id, creator_id=creator_id).first()
       
        print("creator_session",creator_session)
       
        print("session_id",session_id,session_title)
        if not creator_session:
            return JsonResponse({'error': 'session not found or unavailable.'}, status=400)

        if hasattr(creator_session, 'session_date') and creator_session.session_date:
            creator_session_date = creator_session.session_date.strftime('%Y-%m-%d')             
            selected_date_str = session_date.strftime('%Y-%m-%d')            
            if selected_date_str != creator_session_date:
                return JsonResponse({'error': 'Selected date is not available based on the creator\'s updated availability.'}, status=400)


        if hasattr(creator_session, 'session_time') and creator_session.session_time:
            creator_session_time = creator_session.session_time

            if session_time != creator_session_time:
                return JsonResponse({'error': 'Selected time does not match the creator\'s available time.'}, status=400)


        existing_booking = BookingStatus.objects.filter(
            session_id=session_id,
            selectedDate=session_date,
            selectedTime=session_time,
            session_name=session_name,
            user_id = user_id
        ).exists()

        if existing_booking:
            return JsonResponse({'error': 'You already booked this session.'}, status=400)

        # 5. Create the booking if all checks pass
        booking_status = BookingStatus.objects.create(
            user_id=user_id,
            session_title=session_title,
            session_id=session_id,
            session_name=session_name,
            selectedDate=session_date,
            selectedTime=session_time,
            status="success",
            creator_id=creator_id,
        )



        try:
            creator = UserProfile.objects.get(id=creator_id)
        except UserProfile.DoesNotExist:
            return JsonResponse({'error': 'Creator not found'}, status=404)

        formatted_date = session_date.strftime('%B %d, %Y')
        formatted_time = session_time.strftime('%I:%M %p')

        creator_subject = "New Session Booking Alert"
        creator_message = f"""
Hello {creator.firstname},

{user.firstname} {user.lastname} has booked your session.

Session Title: {session_title}
Date: {formatted_date}
Time: {formatted_time}

Please log in to your dashboard to view details.

Thank you!
"""
        send_mail(
            subject=creator_subject,
            message=creator_message,
            from_email='xhibiter@gmail.com',
            recipient_list=[creator.email],
            fail_silently=False,
        )

        user_subject = "Session Booking Confirmation"
        user_message = f"""
Hello {user.firstname} {user.lastname},

Your session booking with {creator.firstname} {creator.lastname} is confirmed.

Session Title: {session_title}
Date: {formatted_date}
Time: {formatted_time}

Thank you for booking!

Best regards,
Team
"""
        send_mail(
            subject=user_subject,
            message=user_message,
            from_email='xhibiter@gmail.com',
            recipient_list=[user.email],
            fail_silently=False,
        )

        return JsonResponse({'message': 'Booking successful', 'booking_id': booking_status.id}, status=201)

    return JsonResponse({'error': 'Invalid request method'}, status=400)



@csrf_exempt
def book_priorityDm_session_api(request):
    
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'Authentication required'}, status=401)

   
    user = request.user 
    user_id = user.id

    if request.method == 'POST':
        session_id = request.POST.get('session_id')
        session_title = request.POST.get('session_title')
        session_name = request.POST.get('session_name')
        
        creator_id = request.POST.get('creator_id')
        print("creator_id",creator_id)
        
        if str(user_id) == str(creator_id):
            return JsonResponse({'error': "You cannot book your own session."}, status=403)
       
        creator_session = None
        
        if session_name == 'Priority Demo':
            creator_session = ServicePriorityDmForm.objects.filter(id=session_id, creator_id=creator_id).first()
       
        print("creator_session",creator_session)
       
        print("session_id",session_id,session_title)
        if not creator_session:
            return JsonResponse({'error': 'Creator has updated availability, session not found or unavailable.'}, status=400)


        existing_booking = BookingStatus.objects.filter(
            session_id=session_id,
            user_id=user_id,
            session_name=session_name
        ).exists()

        if existing_booking:
            return JsonResponse({'error': 'You already booked this session.'}, status=400)

        booking_status = BookingStatus.objects.create(
            user_id=user_id,
            session_title=session_title,
            session_id=session_id,
            session_name=session_name,
            status="success",
            creator_id=creator_id,
        )



        try:
            creator = UserProfile.objects.get(id=creator_id)
        except UserProfile.DoesNotExist:
            return JsonResponse({'error': 'Creator not found'}, status=404)
        
        creator_subject = "New Session Booking Alert"
        creator_message = f"""
Hello {creator.firstname},

{user.firstname} {user.lastname} has booked your session.

Session Title: {session_title}

Please log in to your dashboard to view details.

Thank you!
"""
        send_mail(
            subject=creator_subject,
            message=creator_message,
            from_email='xhibiter@gmail.com',
            recipient_list=[creator.email],
            fail_silently=False,
        )

        user_subject = "Session Booking Confirmation"
        user_message = f"""
Hello {user.firstname} {user.lastname},

Your session booking with {creator.firstname} {creator.lastname} is confirmed.

Session Title: {session_title}

Thank you for booking!

Best regards,
Team
"""
        send_mail(
            subject=user_subject,
            message=user_message,
            from_email='xhibiter@gmail.com',
            recipient_list=[user.email],
            fail_silently=False,
        )

        return JsonResponse({'message': 'Booking successful', 'booking_id': booking_status.id}, status=201)

    return JsonResponse({'error': 'Invalid request method'}, status=400)



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .models import BookingStatus

@csrf_exempt
def get_booked_times(request):
    creator_id = request.GET.get('creator_id')
    session_name = request.GET.get('session_name')
    model_id = request.GET.get('model_id') 
    selected_date_str = request.GET.get('selectedDate')

    if not creator_id or not session_name or not selected_date_str or not model_id:
        return JsonResponse({'error': 'Missing parameters'}, status=400)

    try:
        service_form = ServiceVideoForm.objects.get(id=model_id)
        max_bookings = int(service_form.maxBookings)

    except ServiceVideoForm.DoesNotExist:
        return JsonResponse({'error': 'Invalid model ID'}, status=400)

    bookings = BookingStatus.objects.filter(
        creator_id=creator_id,
        session_name=session_name,
        selectedDate=selected_date_str
    )

    booked_times = []
    for booking in bookings:
        if booking.selectedTime:
            booked_times.append(booking.selectedTime.strftime('%H:%M:%S'))

    fully_booked = len(booked_times) >= max_bookings

    return JsonResponse({
        'booked_times': booked_times,
        'fully_booked': fully_booked
    })



from datetime import datetime, time

@login_required
def creator_bookings(request):
    try:
        profile = UserProfile.objects.get(id=request.user.id)
    except UserProfile.DoesNotExist:
        raise Http404("Page not found.")

    if not profile.is_creator:
        raise Http404("Page not found.")
    creator_id = request.user.id 
    bookings = BookingStatus.objects.filter(creator_id=creator_id)  

    user_bookings = {}
    
    def format_time(time_obj):
        if isinstance(time_obj, time):  # Check if it's a datetime.time object
            hour = time_obj.hour
            minute = time_obj.minute
            if hour == 0:
                return f"12:{minute:02d} AM"  # Midnight
            elif hour < 12:
                return f"{hour}:{minute:02d} AM"  # Morning (AM)
            elif hour == 12:
                return f"12:{minute:02d} PM"  # Noon
            else:
                return f"{hour - 12}:{minute:02d} PM"  # Afternoon/Evening (PM)
        return time_obj
        
    for booking in bookings:
        user = UserProfile.objects.filter(id=booking.user_id).first()  

        if not user:
            continue  

        session_id = booking.session_id
        session_name = booking.session_name

        session = None
        if session_name == "Video":
            session = ServiceVideoForm.objects.filter(id=session_id).first()
        elif session_name == "Priority Demo":
            session = ServicePriorityDmForm.objects.filter(id=session_id).first()
        elif session_name == "Webinar":
            session = ServiceWebinarForm.objects.filter(id=session_id).first()

        if user not in user_bookings:
            user_bookings[user] = []  

        user_bookings[user].append({
            "booking_id": booking.id,
            "session_name": booking.session_name,
            "selected_date": booking.selectedDate,
            "selected_time": format_time(booking.selectedTime),
            "status": booking.status,
            'additional_details':booking.additionalDetails if booking.additionalDetails else "NA",
            "session_title": booking.session_title if session else "Session Not Found"
        })
        print("user_boookings",user_bookings)
    return render(request, 'creator-bookings.html', {
        "user_bookings": user_bookings,
    })
    
    


@login_required
def buyer_bookings(request):
    try:
        profile = UserProfile.objects.get(id=request.user.id)
    except UserProfile.DoesNotExist:
        return HttpResponseForbidden("Access denied.")  

    if profile.is_creator:
        return HttpResponseForbidden("Only buyers can access this page.")
        
    user_id = request.user.id
    bookings = BookingStatus.objects.filter(user_id=user_id)

    now = datetime.now()

    upcoming_bookings = []
    past_bookings = []

    for booking in bookings:
        session = None
        if booking.session_name == "Video":
            session = ServiceVideoForm.objects.filter(id=booking.session_id).first()
            session_date = booking.selectedDate if session else None
            session_time = booking.selectedTime if session else None
        elif booking.session_name == "Priority Demo":
            session = ServicePriorityDmForm.objects.filter(id=booking.session_id).first()
            session_date = None
            session_time = None
        elif booking.session_name == "Webinar":
            session = ServiceWebinarForm.objects.filter(id=booking.session_id).first()
            session_date = session.session_date if session else None
            session_time = session.session_time if session else None

        creator = UserProfile.objects.filter(id=booking.creator_id).first()
        creator_full_name = f"{creator.firstname} {creator.lastname}" if creator else "Unknown"

        item = {
            "booking_id": booking.id,
            "session_name": booking.session_name,
            "selected_date": session_date,
            "selected_time": session_time,
            "status": booking.status,
            "session_title": booking.session_title if session else "Session Not Found",
            "creator": creator_full_name
        }

        if booking.selectedDate and booking.selectedTime:
            booking_datetime = datetime.combine(booking.selectedDate, booking.selectedTime)

            if booking_datetime >= now:
                upcoming_bookings.append({
                    **item,
                    'display_date': booking_datetime.strftime('%d %B %Y'),  
                    'display_time': booking_datetime.strftime('%I:%M %p')   
                })
            else:
                past_bookings.append({
                    **item,
                    'display_date': booking_datetime.strftime('%d %B %Y'),  
                    'display_time': booking_datetime.strftime('%I:%M %p')   
                })

        else:
            past_bookings.append(item)

    return render(request, 'buyer-bookings.html', {
        "upcoming_bookings": upcoming_bookings,
        "past_bookings": past_bookings
    })



import json

@csrf_exempt
@login_required
def availability(request):
    user_availability = Availability.objects.filter(creator_id=request.user.id)

    availability_data = [
        {
            'day': entry.day,
            'from_time': entry.from_time.strftime('%I:%M %p'),
            'to_time': entry.to_time.strftime('%I:%M %p')
        }
        for entry in user_availability
    ]

    return render(request, 'calendar.html', {
        'availability': json.dumps(availability_data) 
    })

    
    
@csrf_exempt
@login_required
def save_availability(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Availability.objects.filter(creator=request.user).delete()

        for day, time_slot in data.items():
            Availability.objects.create(
                creator=request.user,
                day=day.capitalize(),
                from_time=datetime.strptime(time_slot['from'], '%I:%M %p').time(),
                to_time=datetime.strptime(time_slot['to'], '%I:%M %p').time()
            )
        return JsonResponse({'status': 'success'})
    return JsonResponse({'error': 'Invalid request'}, status=400)    



from datetime import datetime, timedelta
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Availability, ServiceVideoForm

def generate_time_slots(from_time, to_time, buffer_minutes=15):
    slots = []
    start = datetime.combine(datetime.today(), from_time)
    end = datetime.combine(datetime.today(), to_time)
    
    while start + timedelta(minutes=buffer_minutes) <= end:
        slot_start = start.time()
        start += timedelta(minutes=buffer_minutes)
        slot_end = start.time()
        slots.append({
            "from": slot_start.strftime('%I:%M %p'), 
            "to": slot_end.strftime('%I:%M %p')
        })
    
    return slots


def get_availability_slots(request):
    creator_id = request.GET.get('creator_id')
    session_id = request.GET.get('session_id')
    print("id",session_id)
    if not creator_id:
        return JsonResponse({'error': 'creator_id is required'}, status=400)
    if not session_id:
        return JsonResponse({'error': 'session_id is required'}, status=400)

    today = datetime.today()
    availability = Availability.objects.filter(creator_id=creator_id)

    try:
        service_form = ServiceVideoForm.objects.get(creator_id=creator_id,id=session_id)
        buffer_time_str = service_form.bufferTime or "15"
        duration_str = service_form.duration or "0"

        buffer_minutes = int(buffer_time_str)
        duration_minutes = int(duration_str)

        total_slot_minutes = buffer_minutes + duration_minutes
    except (ServiceVideoForm.DoesNotExist, ValueError):
        total_slot_minutes = 15  # fallback default

    availability_map = {
        a.day.lower(): {
            'from_time': a.from_time,
            'to_time': a.to_time
        }
        for a in availability
    }

    next_14_days = []
    for i in range(14):
        date = today + timedelta(days=i)
        day_name = date.strftime('%A').lower()
        
        if day_name in availability_map:
            day_availability = availability_map[day_name]
            slots = generate_time_slots(
                day_availability['from_time'], 
                day_availability['to_time'], 
                buffer_minutes=total_slot_minutes
            )
        else:
            slots = []

        next_14_days.append({
            "date": date.strftime('%Y-%m-%d'),
            "day": day_name.capitalize(),
            "slots": slots
        })

    return JsonResponse({"availability": next_14_days})
