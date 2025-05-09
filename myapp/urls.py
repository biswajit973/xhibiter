from django.urls import path
from myapp import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

   path('',views.index,name="index"),
   path('error-404/',views.error_404,name="error-404"),
   path('about/',views.about,name="about"),
   path('activity/',views.activity,name="activity"),
   path('blog/',views.blog,name="blog"),
   path('careers/',views.careers,name="careers"),
   path('case-studies/',views.case_studies,name="case-studies"),
   path('creators/<slug:slug>/', views.collection, name='creator_profile'),
   path('collections-wide-sidebar/',views.collection_wide_sidebar,name="collections-wide-sidebar"),
   path('collections/',views.collections,name="collections"),
   path('contact/',views.contact,name="contact"),
   path('create/',views.create,name="create"),
   path('edit-profile/',views.edit_profile,name="edit-profile"),
   path('help-center/',views.help_center,name="help-center"),
   path('home-2/',views.home_2,name="home-2"),
   path('home-3/',views.home_3,name="home-3"),
   path('home-4/',views.home_4,name="home-4"),
   path('home-5/',views.home_5,name="home-5"),
   path('home-6/',views.home_6,name="home-6"),
   path('home-7/',views.home_7,name="home-7"),
   path('home-8/',views.home_8,name="home-8"),
   path('home-9/',views.home_9,name="home-9"),
   path('home-10/',views.home_10,name="home-10"),
   path('home-11/',views.home_11,name="home-11"),
   path('home-12/',views.home_12,name="home-12"),
   path('home-13/',views.home_13,name="home-13"),
   path('index-rtl/',views.index_rtl,name="index-rtl"),
   path('services/<slug:slug>/', views.item, name='item'),

   path('landing/',views.landing,name="landing"),
   path('login/',views.login_view,name="login"),
   path('signup/',views.signup,name="signup"),
   path('signup_api/', views.signup_api, name='signup_api'),
   path('buyer_signup_api/', views.buyer_signup_api, name='buyer_signup_api'),

    path('login_api/', views.login_api, name='login_api'),
    path('logout/', views.logout_view, name='logout'),

   path('maintenance/',views.maintenance,name="maintenance"),
   path('newsletter/',views.newsletter,name="newsletter"),
   path('partners/',views.partners,name="partners"),
   path('platform-status/',views.platform_status,name="platform-status"),
   path('rankings/',views.rankings,name="rankings"),
   path('single-case-study/',views.single_case_study,name="single-case-study"),
   path('single-post/',views.single_post,name="single-post"),
   path('tos/',views.tos,name="tos"),
   path('user/',views.user,name="user"),
   path('wallet/',views.wallet,name="wallet"),
   path('check-username/',views.check_username,name="check-username"),
   path('update_profile_api/', views.update_profile_details_api, name='update_profile_api'),
   path('update_account_api/', views.update_account_details_api, name='update_account_api'),
   path('create-service/',views.create_service,name="create-service"),
   path('service/video/',views.video,name="service/video"),
   path('service/webinar/',views.webinar,name="service/webinar"),
   path('service/priorityDM/',views.priorityDM,name="service/priorityDM"),
   path('serviceVideo_api/', views.serviceVideo_api, name='serviceVideo_api'),
   path('serviceWebinar_api/', views.serviceWebinar_api, name='serviceWebinar_api'),
   path('servicePrioritydm_api/', views.servicePrioritydm_api, name='servicePrioritydm_api'),
   path('deletevideoSession_api/<int:id>/', views.deletevideoSession_api, name='deletevideoSession_api'),
   path('deletewebinarSession_api/<int:id>/', views.deletewebinarSession_api, name='deletewebinarSession_api'),
   path('deleteprioritydmSession_api/<int:id>/', views.deleteprioritydmSession_api, name='deleteprioritydmSession_api'),
   path('updateVideoSession_api/', views.updateVideoSession_api, name='updateVideoSession_api'),
   path('updateWebinarSession_api/', views.updateWebinarSession_api, name='updateWebinarSession_api'),
   path('updatePriorityDmSession_api/', views.updatePriorityDmSession_api, name='updatePriorityDmSession_api'),
   path('book_video_session_api/', views.book_video_session_api, name='book_video_session_api'),
   path('book_webinar_session_api/', views.book_webinar_session_api, name='book_webinar_session_api'),
   path('book_priorityDm_session_api/', views.book_priorityDm_session_api, name='book_priorityDm_session_api'),
   path("get-booked-times/", views.get_booked_times, name="get_booked_times"),
   path('creator/bookings/', views.creator_bookings, name='creator/bookings'),
   path('buyer/my-bookings/', views.buyer_bookings, name='buyer/bookings'),
   path('creator/availability/', views.availability, name='creator/availability'),
   path('save-availability/', views.save_availability, name='save_availability'),
    path('get-availability-slots/', views.get_availability_slots, name='get_availability_slots'),






   
   



   








   
   
   
   
   ]

if True:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)        
        