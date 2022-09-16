import re
from tkinter import N
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.db.models import Q
from rest_framework import generics
from .models import Contact, Person
from .serializers import ContactSerializer, SignUpSerializer
from rest_framework.views import APIView
from django.core import serializers
# from .auth import CheckPasswordBackend
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from urllib3 import HTTPResponse

from api.models import Contact

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))

def login(request):
    phone_number = request.data.get("phone_number")
    password = request.data.get("password")

    if phone_number is None or password is None:
        return Response({'error': 'Please enter username & password!'},status=HTTP_400_BAD_REQUEST)

    person = authenticate(phone_number=phone_number, password=password)
    if not person:
        return Response({'error': 'Please enter Valid Creadentials!'},status=HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=person)
    return Response({'token': token.key}, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])

def search_by_name(request):
    contact_name=request.data.get("name")
    startw=Contact.objects.filter(contact_name__startswith=contact_name)
    cont=Contact.objects.filter(~Q(contact_name__startswith=contact_name),Q(contact_name__contains=contact_name))
    data=list()
    for i in startw:
        node=[]
        node.append(i.contact_name)
        node.append(i.contact_phone_number)
        node.append(i.spam)
        node.append(i.cid)
        data.append(node)   
    for i in cont:
        node=[]
        node.append(i.contact_name)
        node.append(i.contact_phone_number)
        node.append(i.spam)
        node.append(i.cid)
        data.append(node)
    # data=serializers.serialize ("json",qset)
    # print(data)
    return Response({'results':data},status=HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])

def search_by_number(request):
    data=list()
    phone_number=request.data.get("phone_number")
    try:
        person=Person.objects.get(phone_number=phone_number)
        data.append(person.name)
        data.append(person.phone_number)
    except:
        contacts=Contact.objects.filter(phone_number=phone_number)
        for i in contacts:
            node=[]
            node.append(i.contact_name)
            node.append(i.contact_phone_number)
            node.append(i.spam)
            node.append(i.cid)
            data.append(node)   
    # data=serializers.serialize ("json",qset)
    # print(data)
    return Response({'results':data},status=HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])

def view_contact(request):
    data=list()
    contact_id=request.data.get("contact_id")
    try:
        contact=Contact.objects.get(cid=contact_id)
        phone_number=contact.contact_phone_number
    except:
        return Response({'error': 'Please enter Valid Contact ID!'},status=HTTP_404_NOT_FOUND)

    try:
        person=Person.objects.get(phone_number=phone_number)
        data.append(person.name)
        data.append(person.phone_number)
        current_user=request.user.contact_id
        print("Current user ok", current_user)
        current_user_contact=Contact.objects.get(cid=current_user)
        if(current_user_contact in person.contacts.all()):
            print("if statement")
            data.append(person.email)
        
    except:
        data.append(contact.contact_name)
        data.append(phone_number)
    # data=serializers.serialize ("json",qset)
    # print(data)
    return Response({'results':data},status=HTTP_200_OK)


# @csrf_exempt

# def register(request):
#     if request.method=='post':
#         name = request.POST.get("name")
#         phone_number = request.POST.get("phone_number")
#         password = request.POST.get("password")
#         contact=Contact()
#         contact.contact_name=name
#         contact.contact_phone_number=phone_number
#         contact.save()
#         contact_id=contact.id
#         person=Person()
#         person.name=name
#         person.contact_id=contact_id
#         person.phone_number=phone_number
#         person.password=password
#         person.save()
#         return Response({"Success":"User Registered Succesfully"})
#     return Response({"Register":"Provide User Credentials"})

# class ContactList(generics.ListCreateAPIView):
#     queryset = Contact.objects.all()
#     serializer_class = ContactSerializer


@permission_classes((AllowAny,))

class Register(APIView):

    def get(self,request):
        return Response({'Message':'This is get method of signup API'},status=HTTP_200_OK)

    def post(self,request):
        try:
            data={
                'contact_name':request.data.get("name"),
                'contact_phone_number':request.data.get("phone_number")
            }
            cnt = ContactSerializer(data=data)
            if cnt.is_valid():
                contact=cnt.save()
                print("cnt created")
                print(contact.cid)
            data={
                'name':request.data.get("name"),
                'phone_number':request.data.get("phone_number"),
                'password':request.data.get("password"),
                'contact_id':contact.cid,
                'email':request.data.get("email"),
                'confirm_password':request.data.get("confirm_password")
            }
        except:
            data=request.data

        try:
            obj =  SignUpSerializer(data = data)
            if obj.is_valid():
                obj.save()
                return Response({'Message':'Successfully Signed up'},status = HTTP_200_OK)

            return Response(obj.errors,status = HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'Message':'Something Failed due to {}'.format(str(e))}, status = HTTP_400_BAD_REQUEST)
    

