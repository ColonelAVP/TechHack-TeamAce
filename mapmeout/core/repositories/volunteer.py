from rest_framework.decorators import api_view
from core.models import CustomUser, Volunteer
from core.helpers.base import (
    BadRequestJSONResponse,
    SuccessJSONResponse,
    NotFoundJSONResponse,
    UnauthorizedJSONResponse,
    get_access_token,
    datetime_from_epoch,
)
from models import Volunteer


def volunteering(data):
    user_data = data.get("user")
    pan_no = data.get("pan_no")
    country = data.get("country")
    state = data.get("state")
    city = data.get("city")
    apartment_add = data.get("apartment_add")

    if not user_data:
        return False, BadRequestJSONResponse("Invalid User details")
    volunteer_data = Volunteer.objects.filter(user_data=user_data)
    if volunteer_data.first():
        return False, BadRequestJSONResponse("The user is already a Volunteer")
    volunteer = Volunteer.objects.create(
        pan_no=pan_no,
        country=country,
        state=state,
        city=city,
        apartment_add=apartment_add,
    )
    volunteer.save()
    return True, SuccessJSONResponse("You're a Volunteer now")
