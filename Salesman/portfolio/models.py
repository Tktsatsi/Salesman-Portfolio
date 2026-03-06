from django.db import models

class Dealership(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Career(models.Model):
    dealership = models.ForeignKey(Dealership,on_delete=models.CASCADE)
    role = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True,blank=True)
    achievements = models.TextField()

    def __str__(self):
        return f"{self.dealership} - {self.role}"


class SoldCar(models.Model):
    name = models.CharField(max_length=200)
    dealership = models.ForeignKey(Dealership,on_delete=models.CASCADE)
    year_sold = models.IntegerField()
    image = models.ImageField(upload_to="cars")

    def __str__(self):
        return self.name


class Review(models.Model):
    customer_name = models.CharField(max_length=200)
    rating = models.IntegerField()
    car = models.CharField(max_length=200)
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name