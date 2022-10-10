from django.shortcuts import render, redirect
from .models import Cat, Items, Snacks, Challenge

# Create your views here.
def start(request):
    return render(request, "home/start.html")


def home(request):
    cat = Cat.objects.get(id=1)

    context = {
        'cat': cat,
    }
    return render(request, "home/home.html", context)
