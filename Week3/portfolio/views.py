from django.shortcuts import render

# Create your views here.
from .models import Portfolio


def main(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolio/main.html', {'portfolios': portfolios})
