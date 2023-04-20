from rest_framework.decorators import api_view
from core.models import CustomUser
from core.helpers.base import (
    BadRequestJSONResponse,
    SuccessJSONResponse,
    NotFoundJSONResponse,
    UnauthorizedJSONResponse,
    get_access_token,
    datetime_from_epoch,
)

from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.utils import timezone
from django.core.cache import cache
from knox.auth import AuthToken

# from core.serializers.token_serializer import get_token_pair
from django.contrib.auth import authenticate

# from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated

# from core.repositories.google_login import (
#     get_consent_url,
#     get_consent_callback,
# )

from django.views.decorators.csrf import csrf_protect


# def register(data):
#     mobile_number = data.get("mobile_number")
#     password = data.get("password")
#     email = data.get("email")
#     first_name = data.get("first_name")
#     last_name = data.get("last_name")
#     if not mobile_number:
#         return False, BadRequestJSONResponse(message="Mobile Number not found")
#     user = CustomUser.objects.filter(mobile_number=mobile_number)
#     print(user)
#     if user.first():
#         return True, SuccessJSONResponse(message="User already exists!")
#     else:
#         user = CustomUser.objects.create(
#             mobile_number=mobile_number,
#             email=email,
#             first_name=first_name,
#             last_name=last_name,
#         )
#         user.set_password(password)
#         user.save()
#         _, token = AuthToken.objects.create(user)
#         response = {"access_token": token, "message": "User created successfully!"}
#         return True, SuccessJSONResponse(response)


# def login(data):
#     """Logins an existing user in database"""
#     serializer = AuthTokenSerializer(data=data)
#     authenticated_user = serializer.is_valid()
#     if not authenticated_user:
#         return False, BadRequestJSONResponse(message="Invalid Credentials")
#     user = serializer.validated_data["user"]
#     _, token = AuthToken.objects.create(user)
#     response = {"access_token": token}
#     return True, SuccessJSONResponse(response)


