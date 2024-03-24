from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .randomizer import load_data, generate_character

def generate_character_ajax(request):
    data = load_data()
    new_character = generate_character(data)
    return JsonResponse(new_character)

# Create your views here.
def home(request):
    return render(request, "home.html")