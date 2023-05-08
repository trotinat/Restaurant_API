from django.db import models

class Cities(models.Model):
    id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=500)


class Restaurant_Details(models.Model):
    montant = models.CharField(max_length=500)
    cuisine = models.CharField(max_length=500)
    top_food=models.CharField(max_length=500)

class Restaurant(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=500)
    review = models.CharField(max_length=500)
    rating = models.CharField(max_length=500)
    long = models.CharField(max_length=500)
    lat = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    status = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    restaurant_details = models.OneToOneField(Restaurant_Details,on_delete=models.CASCADE)
    city = models.ForeignKey(Cities,on_delete=models.CASCADE)


class Image(models.Model):
    img_link = models.CharField(max_length=500)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)