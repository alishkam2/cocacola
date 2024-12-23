from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist


class UserConfirmAPIView(APIView):
    def post(self, request):
        code = request.data.get("code")
        username = request.data.get("username")

        if not code or not username:
            return Response(
                {"error": "Code and username are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = User.objects.get(username=username)
            if str(user.profile.confirmation_code) == str(code):
                user.is_active = True
                user.save()
                return Response(
                    {"message": "User confirmed successfully!"},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {"error": "Invalid confirmation code."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except ObjectDoesNotExist:
            return Response(
                {"error": "User not found."}, status=status.HTTP_404_NOT_FOUND
            )
