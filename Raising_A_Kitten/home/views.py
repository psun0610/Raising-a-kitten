from django.shortcuts import render

# Create your views here.
def start(request):
    return render(request, "home/home.html")


def home(request):
    return render(request, "home/home.html")
