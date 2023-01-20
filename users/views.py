from django.shortcuts import render
from django.http.request import HttpRequest

# Create your views here.
def main(request):
    return render(request,"users/main.html")