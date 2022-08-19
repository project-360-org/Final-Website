from django.db import models

# Create your models here.
class Technical_Sub_Category(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Technical_mini_Sub_Category(models.Model):
    sub_id = models.AutoField(primary_key=True,null=False)
    mini_sub_category_of = models.ForeignKey(Technical_Sub_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name} - {self.mini_sub_category_of.name}'

class Technical_sub_mini_Sub_Category(models.Model):
    sub_mini_sub_id = models.AutoField(primary_key=True)
    mini_sub_category_of = models.ForeignKey(Technical_mini_Sub_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name} - {self.mini_sub_category_of.name} - {self.mini_sub_category_of.mini_sub_category_of.name}'