
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('/register',register,name='register'),
    path('login/',login_view,name='login'),
    path('/logout',logout_view,name='logout'),
    path('/profile',profile,name='profile'),
    path('reset_password/',reset_password,name='reset_password'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)