from django.shortcuts import render
from website.models import Property

# Create your views here.

def index(request):
    return render(request, "index.html")

def properties(request):
    props = Property.objects.all()
    return render(request, "properties.html", {'props': props})
