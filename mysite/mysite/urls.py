"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path

# Import new path for drinks - use project 
from mysite import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # Path for Django Admin site
    path('admin/', admin.site.urls),
    # Path for drinks site - mysite
    path('mysite/', views.drink_list),
    # Path for page to display drink detials
    path('mysite/<int:id>', views.drink_detail)
   
]

    # We can use a function called 'format_suffix_patterns(urlpatterns)' to be able to create the same url's
    # but for different data types, so if we are using Return() but only want to display the raw JSON
    # we can use this functon

urlpatterns= format_suffix_patterns(urlpatterns)