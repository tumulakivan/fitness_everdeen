"""
URL configuration for fitness_everdeen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('schedule/', views.workout_list, name='workout_list'),
    path('schedule/add/', views.add_workout, name='add_workout'),
    path('schedule/<int:pk>/update/', views.edit_workout, name='edit_workout'),
    path('schedule/<int:pk>/delete/', views.delete_workout, name='delete_workout'),
    path('tips/', views.tip_list, name='tip_list'),
    path('tips/add/', views.add_tip, name='add_tip'),
    path('tips/<int:pk>/update/', views.update_tip, name='update_tip'),
    path('tips/<int:pk>/delete/', views.delete_tip, name='delete_tip'),
]
