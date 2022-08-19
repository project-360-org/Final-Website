from django.db import models

# Create your models here.

class Non_Technical_Sub_Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Non_Technical_mini_Sub_Category(models.Model):
    mini_sub_category_of = models.ForeignKey(Non_Technical_Sub_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Non_Technical_sub_mini_Sub_Category(models.Model):
    mini_sub_category_of = models.ForeignKey(Non_Technical_mini_Sub_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
