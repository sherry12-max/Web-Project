from django.urls import path, include
from . import views

urlpatterns = [
    path('accounts/logout-and-signup/', views.logout_and_signup, name='logout_and_signup'),
    path('accounts/', include('allauth.urls')),
]