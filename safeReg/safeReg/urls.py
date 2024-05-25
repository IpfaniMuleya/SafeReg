from django.contrib import admin
from django.urls import path, include
from two_factor.urls import urlpatterns as tf_urls

urlpatterns = [
    path('supreme-Admin/', admin.site.urls), #change to something else
    
    path('', include('secureReg.urls')),
    
    path('', include(tf_urls)),
]
