from django.urls import path
from .views import CustomUserController, VolunteerController
from knox import views as knox_views

urlpatterns = [
    ### START LOGIN URLS
    path("register/", CustomUserController.register, name="user-register"),
    path("login/", CustomUserController.login, name="user-login"),
    # path("logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path("volunteer/", VolunteerController.be_volunteer, name="be-volunteer"),
]
