from django.contrib import admin
from django.urls import path
from businesses import views

urlpatterns = [
   path('home/', views.home, name="home"),
   path('business_list/', views.business_list, name="business_list"),
   path('business_detail/<int:business_id>/', views.business_detail, name="business_detail"),
   path('create/', views.business_create, name="business_create"),
   path('business_update/<int:business_id>/', views.business_update, name="business_update"),
   path('business_delete/<int:business_id>/', views.business_delete, name="business_delete"),




]