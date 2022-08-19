from email.policy import default
from django.db import models

# Create your models here.

class Company_Info(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    logo = models.ImageField(upload_to='media/company/logo/', null=True, default='static/images/progamiz.jpg')
    name = models.CharField(max_length=100)
    internship_link = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class Engineering_Video_Embed_Code(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    company = models.ForeignKey(Company_Info, on_delete=models.CASCADE)
    code = models.TextField()
    def __str__(self):
        return self.company.name + "Video" 

class Finance_Video_Embed_Code(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    company = models.ForeignKey(Company_Info, on_delete=models.CASCADE)
    code = models.TextField()
    def __str__(self):
        return self.company.name + "Video"

class Marketing_Video_Embed_Code(models.Model):
    id = models.AutoField(primary_key=True,null=False)
    company = models.ForeignKey(Company_Info, on_delete=models.CASCADE)
    code = models.TextField()
    def __str__(self):
        return self.company.name + "Video"