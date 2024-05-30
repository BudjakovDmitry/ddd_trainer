from pydantic import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from adapty_app.domains.entities import Device, User
from adapty_app.services.user_service import UserService


class UserView(APIView):
    def post(self, request) -> Response:
        device_data = request.data.get('device_info')
        if device_data is None:
            return Response(
                {"details": "Device info is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            user_data = User(**request.data)
            device_data = Device(**device_data)
        except ValidationError as e:
            return Response({"details": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        UserService.create_or_update_user(user_data, device_data)
        return Response(user_data.dict(), status=status.HTTP_200_OK)
