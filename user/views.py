from djoser.conf import settings
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from social_django.utils import psa


@psa("social:begin", "social:complete")
def google_auth(request):
    return HttpResponseRedirect("/")


# class FirebaseLoginView(APIView):
#     def post(self, request, *args, **kwargs):
#         # Obtain the Firebase access token from the request data
#         access_token = request.data.get("access_token")

#         # Verify the Firebase access token using Firebase Admin SDK
#         try:
#             decoded_token = firebase_admin.auth.verify_id_token(access_token)
#             # Fetch user information from the decoded token
#             uid = decoded_token["uid"]
#             # email = decoded_token["email"]
#             # Add more fields as needed

#             # Check if the user already exists in your database
#             # Create a new user or fetch the existing user

#             # Generate a DRF authentication token
#             token_serializer = TokenCreateSerializer(data={"uid": uid})
#             token_serializer.is_valid(raise_exception=True)
#             token = token_serializer.save()

#             return Response({"token": token.key})
#         except (ValueError, firebase_admin.auth.InvalidIdTokenError):
#             raise AuthenticationFailed("Invalid access token")


# class FirebaseTokenExchangeView(views.TokenCreateView):
#     serializer_class = FirebaseLoginSerializer
