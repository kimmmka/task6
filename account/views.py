import datetime
import random

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import ConfirmCode, User

# Create your views here.
from rest_framework.views import APIView


class RegisterAPIView(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.create_user(
            username=username,
            email = "a@n.com",
            password=password,
            is_active=True
        )
        code = str(random.randint(1000,9999))
        valid_until = datetime.datetime.now() + datetime.timedelta(minutes=5)
        ConfirmCode.objects.create(user=user, code=code, valid_until=valid_until)
        # send_code_to_phone(code,username)
        return Response(data={'message': 'User created!!!'})
'''
class ConfirmAPIView(APIView):
    def post(self, request):
        code = request.data['code']
        code_list = ConfirmCode.objects.filter(code=code,
                                               valid_until__gte=datetime.datetime.now()
                                               )
        if code_list:

            confirmcode = code_list[0]
            confirmcode.user.is_active = True
            confirmcode.user.save()
            print("test")


            code_list.delete()
            return Response(data={'message': 'user activated'})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
'''
class UpdateAPIView(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']
        print(username, password)
        user = authenticate(username = username, password=password)
        print(user)
        if user:
            user.email="lala@qmail.com"
            user.save()
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            return Response(data={
                'token': token.key
            })
        else:
            return Response(data={
                'message': "User not found!"
            }, status = status.HTTP_404_NOT_FOUND)


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        print(username, password)
        user = authenticate(username = username, password=password)
        print(user)
        if user:
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            return Response(data={
                'token': token.key
            })
        else:
            return Response(data={
                'message': "User not found!"
            }, status = status.HTTP_404_NOT_FOUND)