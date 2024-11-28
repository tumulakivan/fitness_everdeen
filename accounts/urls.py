from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('main/', views.main_view, name='main'),
    path('main/add-workout', views.add_workout, name='add_workout'),
    path('main/workout-list', views.workout_list, name='workout_list'),
    path('edit_workout/<int:pk>/', views.edit_workout, name='edit_workout'),
    path('delete-workout/<int:pk>/', views.delete_workout, name='delete_workout'),
    path('logout/', views.logout_view, name='logout'),
]