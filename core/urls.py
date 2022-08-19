from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Tabs.main, name='main'),
    path('career_roadmap/', Tabs.career_roadmap, name='career_roadmap'),
    path('partners_form/', Tabs.partners_form, name='partners_form'),
    path('about_us/', Tabs.about_us, name='about_us'),
]