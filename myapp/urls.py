from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="home"),
    path("user", views.user, name="user"),
    path("registration", views.registration, name="registration"),
    path("login", views.loginUser, name="login"),
    path("logout", views.logoutUser, name="logout"),
    path("about", views.about, name="about"),

    path("ndetails", views.ndetails, name="ndetails"),
    path("customer/<str:my_id>/", views.customer, name="customer"),
    path("nproduct", views.nproduct, name="nproduct"),
    path("createOrder", views.createOrder, name="createOrder"),
    path("UpdateOrder/<str:pk>/", views.UpdateOrder, name="UpdateOrder"),
    path("remove/<str:pk>/", views.remove, name="remove"),


    path("settings", views.settings, name="settings"),
    path("services", views.services, name="services"),
    path("contact", views.contact, name="contact"),

    path('reset_password', auth_views.PasswordResetView.as_view(), name='reset_password'),

    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),

    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]