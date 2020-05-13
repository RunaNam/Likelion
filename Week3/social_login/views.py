from django.shortcuts import render
from .models import Pictures

# Create your views here.
def home(request):
    
    pictures = Pictures.objects.all()
    return render(request, 'social_login/home.html', {'pictures': pictures });    