# I. Using HttpResponse
# from django.http import HttpResponse #needs to be imported to use HttpResponse

# # Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# II. Using render
#Render : a shortcut function that takes a request and a template name and returns an HttpResponse object of that rendered template.
from django.shortcuts import render 
def home(request):
  context = {"name": "Shin"}
  return render(request, "polls/home.html", context)  # polls/home.html is the template file

def tourist_attractions(request):
  context = {"attractions": [{"name": "The Louvre", "location" : "Paris, France", "rating": 5}, {"name": "The Great Wall of China", "location" : "China", "rating": 4}, 
  {"name": "The Eiffel Tower", "location" : "Paris, France", "rating": 2}, {"name": "The Taj Mahal", "location" : "Agra, India", "rating": 3},]}
  return render(request, "tourist_attractions/tourist_attractions.html", context)