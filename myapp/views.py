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
        return HttpResponseForbidden("Access denied.")  # Or redirect to home/login

  if not profile.is_creator:
      return HttpResponseForbidden("Only creators can access this page.")
    
  return render(request, 'create-service.html')

@login_required
def video(request):
  creatorvideodetails = []
  
  try:
        profile = UserProfile.objects.get(id=request.user.id)
  except UserProfile.DoesNotExist:
        return HttpResponseForbidden("Access denied.")  # Or redirect to home/login

  if not profile.is_creator:
      return HttpResponseForbidden("Only creators can access this page.")
    
  creatorvideosessiondetails =  ServiceVideoForm.objects.filter(creator = request.user.id)
  
  for creator in creatorvideosessiondetails:
    creatorvideodetails.append(creator)
  
  return render(request, 'video.html',{'creatorvideosessiondetails':creatorvideodetails})

def webinar(request):
  creatorwebinardetails = []
  try:
        profile = UserProfile.objects.get(id=request.user.id)
  except UserProfile.DoesNotExist:
        return HttpResponseForbidden("Access denied.")  

  if not profile.is_creator:
      return HttpResponseForbidden("Only creators can access this page.")
  creatorwebinarsessiondetails =  ServiceWebinarForm.objects.filter(creator = request.user.id)
  
  for creator in creatorwebinarsessiondetails:
    creatorwebinardetails.append(creator)
    
  return render(request, 'webinar.html',{'creatorwebinarsessiondetails':creatorwebinardetails})

def priorityDM(request):
  creatorpriorityDmdetails = []
  try:
        profile = UserProfile.objects.get(id=request.user.id)
  except UserProfile.DoesNotExist:
        return HttpResponseForbidden("Access denied.")  

  if not profile.is_creator:
      return HttpResponseForbidden("Only creators can access this page.")
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
        
        print('email', email_or_contact)
        print('password', password)

        # Verify reCAPTCHA token
        if not verify_recaptcha(recaptcha_token):
            return JsonResponse({'error': 'Invalid reCAPTCHA. Please try again.'}, status=400)

        user = authenticate(request, username=email_or_contact, password=password)

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
            selectedDates = request.POST.get('selectedDates')
            selectedTime = request.POST.get('selectedTime')
            bufferTime = request.POST.get('bufferTime')
            maxBookings = request.POST.get('maxBookings')
            if not title or not duration or not amount or not selectedTime or not selectedDates or not bufferTime or not maxBookings:
                return JsonResponse({'error': 'All fields are required (title, duration, amount, date, time).'}, status=400)

            service_video = ServiceVideoForm.objects.create(
                creator=creator,
                title=title,
                description = description,
                duration=duration,
                amount=amount,
                selectedDates=selectedDates,
                selectedTime=selectedTime,
                bufferTime=bufferTime,
                maxBookings=maxBookings
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
    selectedTime = request.POST.get("selectedTime")
    selectedDates = request.POST.get("selectedDates")
    bufferTime = request.POST.get("bufferTime")
    maxBookings = request.POST.get("maxBookings")




    videosession = ServiceVideoForm.objects.get(id=id)
    videosession.title = title
    videosession.description = description
    videosession.duration = duration
    videosession.amount = amount
    videosession.selectedDates = selectedDates
    videosession.selectedTime = selectedTime
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

@login_required
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
    
    if hasattr(item, 'selectedDates') and item.selectedDates and hasattr(item, 'selectedTime') and item.selectedTime:
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
          


@csrf_exempt
@login_required
def book_session_api(request):
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
        
        if request.POST.get('additionalDetails'):
            additionalDetails = request.POST.get('additionalDetails')  
            
        booking_status = BookingStatus.objects.create(
            user_id=user_id,
            session_title=session_title,
            session_id=session_id,
            session_name=session_name,
            selectedDate=session_date,
            selectedTime=session_time,
            additionalDetails=additionalDetails,
            status="success",
            creator_id=creator_id
        )

        # Get creator and user objects
        try:
            creator = UserProfile.objects.get(id=creator_id)
        except UserProfile.DoesNotExist:
            return JsonResponse({'error': 'Creator not found'}, status=404)

        # Format date and time for display
        formatted_date = session_date.strftime('%B %d, %Y')
        formatted_time = session_time.strftime('%I:%M %p')

        # Email content for creator
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

        # Email content for user
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
@login_required
def get_booked_times(request):
    selected_date = request.GET.get('selectedDate')
    creator_id = request.GET.get('creator_id')
    session_name = request.GET.get('session_name')

    if not selected_date or not creator_id:
        return JsonResponse({'error': 'Missing parameters'}, status=400)

    # Get all booked times
    booked = BookingStatus.objects.filter(
        selectedDate=selected_date,
        creator_id=creator_id,
        session_name=session_name
    )
    print("bookingtimes",booked)
    booked_times = booked.values_list('selectedTime', flat=True)
    booked_times_str = [bt.strftime('%I:%M %p') for bt in booked_times]  

    try:
        service_form = ServiceVideoForm.objects.get(id=request.GET.get('model_id'))
        max_bookings = int(service_form.maxBookings or 0)
    except ServiceVideoForm.DoesNotExist:
        max_bookings = 0

    booking_count = booked.count()

    return JsonResponse({
        'booked_times': booked_times_str,
        'booking_count': booking_count,
        'max_bookings': max_bookings
    })





@login_required
def creator_bookings(request):
    try:
          profile = UserProfile.objects.get(id=request.user.id)
    except UserProfile.DoesNotExist:
          return HttpResponseForbidden("Access denied.")  

    if not profile.is_creator:
        return HttpResponseForbidden("Only creators can access this page.")
    creator_id = request.user.id 
    bookings = BookingStatus.objects.filter(creator_id=creator_id)  

    user_bookings = {}

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
            "selected_time": booking.selectedTime,
            "status": booking.status,
            'additional_details':booking.additionalDetails if booking.additionalDetails else "NA",
            "session_title": booking.session_title if session else "Session Not Found"
        })
    return render(request, 'creator-bookings.html', {
        "user_bookings": user_bookings,
    })


from datetime import datetime
from django.utils.timezone import make_aware

@login_required
def buyer_bookings(request):
    try:
          profile = UserProfile.objects.get(id=request.user.id)
    except UserProfile.DoesNotExist:
          return HttpResponseForbidden("Access denied.")  

    if  profile.is_creator:
        return HttpResponseForbidden("Only buyers can access this page.")
    user_id = request.user.id
    bookings = BookingStatus.objects.filter(user_id=user_id)

    now = make_aware(datetime.now())

    upcoming_bookings = []
    past_bookings = []

    for booking in bookings:
        session = None
        if booking.session_name == "Video":
            session = ServiceVideoForm.objects.filter(id=booking.session_id).first()
        elif booking.session_name == "Priority Demo":
            session = ServicePriorityDmForm.objects.filter(id=booking.session_id).first()
        elif booking.session_name == "Webinar":
            session = ServiceWebinarForm.objects.filter(id=booking.session_id).first()
        creator = UserProfile.objects.filter(id=booking.creator_id).first()
        
        creator_full_name = f"{creator.firstname} {creator.lastname}" if creator else "Unknown"
        item = {
            "booking_id": booking.id,
            "session_name": booking.session_name,
            "selected_date": booking.selectedDate,
            "selected_time": booking.selectedTime,
            "status": booking.status,
            "session_title": booking.session_title if session else "Session Not Found",
            "creator": creator_full_name
        }

        if booking.selectedDate and booking.selectedTime:
            booking_datetime = make_aware(datetime.combine(booking.selectedDate, booking.selectedTime))
            if booking_datetime >= now:
                upcoming_bookings.append(item)
            else:
                past_bookings.append(item)
        else:
            past_bookings.append(item)

    return render(request, 'buyer-bookings.html', {
        "upcoming_bookings": upcoming_bookings,
        "past_bookings": past_bookings
    })
