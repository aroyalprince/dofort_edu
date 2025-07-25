from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("dofort-secure-admin/", admin.site.urls), 
    path("", views.home, name='home'),
    path("courses", views.courses, name='courses'),
    path("enquiry", views.enquiry, name='enquiry'),
    path("faculties", views.faculties, name='faculties'),
    path("aboutus", views.aboutus, name='aboutus'),
    path('submit-enquiry/', views.submit_enquiry, name='submit_enquiry'),
    path("policy", views.policy, name='policy'),
    path("admission", views.admission, name='admission'),
    path("gallery", views.gallery, name='gallery'),
    path("term_serv", views.term_serv, name='term_serv'),
    path("contact", views.contact, name='contact'),
    path("subject", views.subject, name='subject'),
    path('thank-you/', views.thank_you, name='thank_you')


]