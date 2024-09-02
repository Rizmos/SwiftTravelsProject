import json

from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pip._vendor.requests.auth import HTTPBasicAuth

from TravelApp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from TravelApp.models import Member, Shipment ,Plus ,Premium,Basic



# Create your views here.
def index(request):
    if request.method == 'POST':
        if Member.objects.filter(
                email=request.POST['email'],
                password=request.POST['password']
        ).exists():
            return render(request, 'index.html')

        else:
            return render(request, 'Login.html')
    else:
        return render(request, 'Login.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def pricing(request):
    return render(request,'pricing.html')
def register(request):
    if request.method == 'POST':
        members = Member(
            fullname=request.POST['fullname'],
            email=request.POST['email'],
            password=request.POST['password'],
        )
        members.save()
        return redirect('/Login')
    else:
        return render(request, 'register.html')
def login(request):
    return render(request,'login.html')
def basic(request):
    if request.method == 'POST':
        basic = Basic(
            name=request.POST['fullname'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            amount=request.POST['amount'],
        )
        basic.save()
        return redirect('/book')
    else:
        return render(request, 'basicpay.html')
def premium(request):
    if request.method == 'POST':
        premium = Premium(
            name=request.POST['fullname'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            amount=request.POST['amount'],
        )
        premium.save()
        return redirect('/book')
    else:
        return render(request, 'premiumpay.html')
def plus(request):
    if request.method == 'POST':
        plus = Plus(
            name=request.POST['fullname'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            amount=request.POST['amount'],
        )
        plus.save()
        return redirect('/book')
    else:
        return render(request, 'plus.html')
def book(request):
    if request.method == 'POST':
        book = Shipment(
            fullname=request.POST['fullname'],
            email=request.POST['email'],
            origin=request.POST['origin'],
            destination=request.POST['destination'],
            date=request.POST['date'],
            phone=request.POST['phone'],
            message=request.POST['message'],
        )
        book.save()
        return redirect('/book')
    else:
        return render(request, 'booking.html')

def token(request):
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})





def stk(request,):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "Apen Softwares",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Payment made successfully")

