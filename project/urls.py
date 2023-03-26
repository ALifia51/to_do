
from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', home_view),
    # path('home/<mk>', home_view),
    path('', home_view , name ='home'),
    path('about/', about_view, name ='about')
]
