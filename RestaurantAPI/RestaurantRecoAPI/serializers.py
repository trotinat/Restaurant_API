from rest_framework import serializers
from RestaurantRecoAPI.models import Restaurant,Cities,Restaurant_Details,Image


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ('id','city_name')


class Restaurant_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant_Details
        fields = ('montant','cuisine','RdvEndTime','top_food')


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id','name','review','rating','long','lat','address','status','phone','restaurant_details','city')



class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('img_link','restaurant')