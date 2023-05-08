from django.urls import re_path,include
from RestaurantRecoAPI import views



urlpatterns = [
    re_path(r'^restaurants$',views.get_restaurants),
    re_path(r'^restaurants/(?P<restaurant_id>\d+)$', views.get_restaurant_by_id),
    re_path(r'^cities$',views.get_cities)
    
]
