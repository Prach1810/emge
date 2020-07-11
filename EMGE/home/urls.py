from django.urls import path

from home.views import home,about,partner,terms,dashboard, search, post,companyprofile,profile
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home, name="home"),
    path('about', about, name="about"),
    path('partner', partner, name="partner"),
    path('terms', terms, name="terms"),
    path('dashboard',dashboard , name="dashboard"),
    path('companyprofile<inf_id>', companyprofile, name="companyprofile"),
    path('search', search, name="search"),
    path('post', post, name="post"),
    path('profile', profile, name="profile"),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
