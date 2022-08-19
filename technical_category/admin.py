from django.contrib import admin
from .models import *
# Register your models here.
class Technical_mini_Sub_Category_Admin(admin.ModelAdmin):
    list_display = ['name', 'mini_sub_category_of']
    list_filter = ['mini_sub_category_of']
    search_fields = ['name']

class Technical_sub_mini_Sub_Category_Admin(admin.ModelAdmin):
    list_display = ['name', 'mini_sub_category_of']
    list_filter = ['mini_sub_category_of']
    search_fields = ['name']
admin.site.register(Technical_Sub_Category)
admin.site.register(Technical_mini_Sub_Category, Technical_mini_Sub_Category_Admin)
admin.site.register(Technical_sub_mini_Sub_Category, Technical_sub_mini_Sub_Category_Admin)