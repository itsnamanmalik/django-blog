from django.shortcuts import render
from blog.models import *
from video.models import *
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from api.serializers import *
from rest_framework.views import APIView
from django.contrib.auth import login, logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView

# Create your views here.

@api_view(['GET',])
def blogAPI(request):
    all_post = Blog.objects.all()
    serializer = BlogSerializer(all_post, many=True)
    return Response(serializer.data)

@api_view(['GET',])
def categoryAPI(request):
    all_category = Category.objects.all()
    serializer = CategorySerializer(all_category, many=True)
    return Response(serializer.data)

@api_view(['GET',])
def videoAPI(request):
    all_video = Video.objects.all()
    serializer = VideoSerializer(all_video, many=True)
    return Response(serializer.data)

# @api_view(['POST', ])
# def registration_view(request):

# 	if request.method == 'POST':
# 		serializer = RegistrationSerializer(data=request.data)
# 		data = {}
# 		if serializer.is_valid():
# 			account = serializer.save()
# 			data['response'] = 'successfully registered new user.'
# 			data['email'] = account.email
# 			data['username'] = account.username
# 		else:
# 			data = serializer.errors
# 		return Response(data)


# class LoginView(GenericAPIView):
#     serializer_class = LoginSerializer
    
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data["user"]
#         login(request, user)
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({"token": token.key}, status=200)


# class LogoutView(APIView):
#     authentication_classes = (TokenAuthentication, )

#     def post(self, request):
#         logout(request)
#         return Response(status=204)	