from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from django_request_mapping import request_mapping


@request_mapping("")
class MyView(View):

    @request_mapping("/", method="get")
    def home(self,request):
        return render(request,'home.html');
    @request_mapping("/next2", method="get")
    def home(self,request):
        return render(request,'next2.html');
    @request_mapping("/next3", method="get")
    def home(self,request):
        return render(request,'next3.html');
    @request_mapping("/next4", method="get")
    def home(self,request):
        return render(request,'next4.html');
    @request_mapping("/next5", method="get")
    def home(self,request):
        return render(request,'next5.html');