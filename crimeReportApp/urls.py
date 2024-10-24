from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('signup/', views.signup, name="signup"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('settings/', views.user_settings, name="settings"),
    path('crimeReport/', views.crimeReport, name="crimeReport"),
    path('viewReport/', views.viewReport, name="viewReport"),
    
    path('update-crime/<int:id>', views.update_crime, name="update-crime"),
    path('delete-crime/<int:id>', views.delete_crime, name="delete-crime"),
]
