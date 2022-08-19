from django.contrib import admin
from .models import *

class Non_Technical_mini_Sub_Category_Admin(admin.ModelAdmin):
    list_display = ['name', 'mini_sub_category_of']
    list_filter = ['mini_sub_category_of']
    search_fields = ['name']

class Non_Technical_sub_mini_Sub_Category_Admin(admin.ModelAdmin):
    list_display = ['name', 'mini_sub_category_of']
    list_filter = ['mini_sub_category_of']
    search_fields = ['name']

admin.site.register(Non_Technical_Sub_Category)
admin.site.register(Non_Technical_mini_Sub_Category, Non_Technical_mini_Sub_Category_Admin)
admin.site.register(Non_Technical_sub_mini_Sub_Category, Non_Technical_sub_mini_Sub_Category_Admin)
