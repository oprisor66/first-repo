from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404

from .models import Cards

# Create your views here.
def index(request):
    latest_card_list = Cards.objects.order_by('-create_at')[:5]
    context = {'latest_card_list': latest_card_list}
    return render(request, 'cards/index.html', context)

def detail(request, card_id):
    card = get_object_or_404(Cards, pk=card_id)
    return render(request, 'cards/detail.html', {'card': card})




