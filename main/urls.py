from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from users.forms import CustomLoginForm

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('signup', views.signup, name="signup"),
    path('editprofile', views.editprofile, name="editprofile"),
    path('login/', LoginView.as_view(
        authentication_form=CustomLoginForm),
         name="login"
         ),
    path('addreservation/<str:date>', views.addreservation, name="addreservation"),
    path('addreservation/', views.redirect_to_today, name="redirect_to_today"),
    path('ownreservations', views.ownreservations, name="ownreservations"),
]