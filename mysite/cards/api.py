from rest_framework import serializers,viewsets
from .models import Cards



class CardSerializer(serializers.ModelSerializer):
     class Meta:
          model = Cards
           


class CardViewSet(viewsets.ModelViewSet):
     queryset = Cards.objects.all()
     serializer_class = CardSerializer