from django.urls import path
from . import views
from django.contrib.auth import  views as auth_views


urlpatterns = [
    path('',views.attendances, name="attendance"),
    path('scores',views.scores, name="scores"),
    path('userinfo',views.userinfo, name="userinfo"),
    path('editinfo',views.editinfo, name="Edit info"),
    ]