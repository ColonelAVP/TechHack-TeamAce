from rest_framework.decorators import api_view
from core.models import CustomUser
from core.helpers.base import (
    BadRequestJSONResponse,
    SuccessJSONResponse,
    NotFoundJSONResponse,
    UnauthorizedJSONResponse,
    # get_access_token,
    # datetime_from_epoch,
)

class VolunteerController:
    @staticmethod
    @api_view(["POST"])
    def be_volunteer(request):
        post_data = request.data
        success, response = volunteering(post_data)
        if not success:
            return BadRequestJSONResponse(message=response)
        return SuccessJSONResponse(message=response)
