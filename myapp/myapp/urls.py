"""myapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myapp.views import *

from django.conf import settings
from django.conf.urls.static import static

# django  conf import seeting taticss files.. 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',home, name='hm'),
    path('about/',about),
    path('services/',services),
    path('',home),
    path("emp/",include("emp.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Here we dont call the functions like Test() ..function is () called by Default by the Django Engine... >>> Django Engine >> used HERE >> 
# giving the name in the url with url tags {% url 'page_name'  %}
# url tage {% url 'name'    %} form actino always gives the URL tag URL can be mentioned with slash tags /
# emp/ it says about the folder name and include("emp.urls")

# for the static url path, you need to give the MEdia root and media_url in setting and urls.py file 
# + static(settings.Media_URL, document_root = setting.Media_Root)
# in the setting you need to import the setting files.. 