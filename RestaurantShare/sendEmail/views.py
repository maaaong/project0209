from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sendEmail(request) :
    return HttpResponse("sendEmail 앱에서 메일을 전송하는 기능을 수행할 예정입니다.")
