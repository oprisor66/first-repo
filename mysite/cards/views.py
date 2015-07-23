from django.shortcuts import render
from django.http import HttpResponse
from .models import Cards

# Create your views here.
def index(request):
    latest_card_list = Cards.objects.order_by('-create_at')[:3]
    output = ', '.join([p.name for p in latest_card_list])
    return HttpResponse(output)