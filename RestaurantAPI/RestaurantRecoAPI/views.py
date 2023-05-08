from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from RestaurantRecoAPI.models import Restaurant,Cities,Image,Restaurant_Details
from RestaurantRecoAPI.serializers import Restaurant_DetailsSerializer,RestaurantSerializer,ImageSerializer,CitySerializer


@csrf_exempt
def get_restaurants(request):
    if request.method=='GET':
        restaurants=Restaurant.objects.all()
        restaurants_serializer=RestaurantSerializer(restaurants,many=True)
        return JsonResponse(restaurants_serializer.data,safe=False)
    
def get_cities(request):
    if request.method=='GET':
        cities=Cities.objects.all()
        cities_serializer=CitySerializer(cities,many=True)
        return JsonResponse(cities_serializer.data,safe=False)
    


def get_restaurant_by_id(request, restaurant_id):
    if request.method == 'GET':
        try:
            restaurant = Restaurant.objects.get(id=restaurant_id)
            restaurant_serializer = RestaurantSerializer(restaurant)
            return JsonResponse(restaurant_serializer.data)
        except Restaurant.DoesNotExist:
            return JsonResponse({'error': 'Restaurant not found.'}, status=404)