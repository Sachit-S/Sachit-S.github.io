from django.shortcuts import render
import random
from django.shortcuts import HttpResponse
from .models import Dog


def index(request):
    profiles = Dog.objects.all()
    dogz = (random.choices(profiles, k=25))
    dogs = []
    for d in dogz:
        if d not in dogs:
            dogs.append(d)
    return render(request, 'index.html', {'dogs': dogs})
