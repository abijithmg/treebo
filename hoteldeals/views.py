from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from hoteldeals.serializers import UserSerializer, DealsSerializer, ListSerializer, StatSerializer
from hoteldeals.models import Deals
from django.core.paginator import Paginator
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pdb;
from django.db.models import Avg, Max, Min
import json

api_hits = 0


def increase_api_hit_count():
    global api_hits
    api_hits += 1


# def get_api_count():
#     # context = {'API_HITS': api_hits}
#     # return Response(context)
#     return api_hits


@api_view(['GET'])
def users(request):
    increase_api_hit_count()
    queryset = User.objects.all()
    serializer = UserSerializer
    return Response(serializer.data)

# @api_view(['GET'])
# def DealsViewSet(request):
#     queryset = Deals.objects.all()
#     serializer_class = DealsSerializer


@api_view(['GET', 'POST'])
def hotels_list(request, no_of_pages):
    increase_api_hit_count()
    if request.method == 'GET':
        hotel_deals = Deals.objects.all()
        serializer = ListSerializer(hotel_deals, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        hotel_deals = Deals.objects.all()
        serializer = ListSerializer(hotel_deals, many=True)
        paginator = Paginator(hotel_deals, 10)
        page = paginator.page(no_of_pages)
        objects = page.object_list
        response = HttpResponse(page.object_list)
        return response


@api_view(['GET'])
def stats(request):
    increase_api_hit_count()
    avg = Deals.objects.values('rating').aggregate(Avg('rating'))
    max_price = Deals.objects.values('actual_price').aggregate(Max('actual_price'))
    min_price = Deals.objects.values('actual_price').aggregate(Min('actual_price'))
    hotel_locations = Deals.objects.values('location')
    city_dict = {'BLR': 0, 'MUM': 0, 'CHE': 0, 'HYD': 0, 'DEL': 0, 'OTHERS': 0}
    for hotel_location in hotel_locations:
        if '560' in hotel_location['location']:
            city_dict['BLR'] += 1
        elif '400' in hotel_location['location']:
            city_dict['MUM'] += 1
        elif '600' in hotel_location['location']:
            city_dict['CHE'] += 1
        elif '500' in hotel_location['location']:
            city_dict['HYD'] += 1
        elif '110' in hotel_location['location']:
            city_dict['DEL'] += 1
        else:
            city_dict['OTHERS'] += 1

    json_data = {'average-rating': avg['rating__avg'], 'api-hits': api_hits,
                 'price': [{'Maximum': max_price['actual_price__max'],
                            'Minimum': min_price['actual_price__min']}],
                 'area-wise-hotel-distribution': [city_dict]}

    # serializer = StatSerializer(queryset, many=True)
    return Response(json_data)
