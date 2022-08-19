from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib import messages 
from django.conf import settings
from non_technical_category.models import *
from technical_category.models import *
from core.models import *
from company.models import *
# Create your views here.
class Tabs:
    def main(self):
        return render(self, 'index.html')
    def career_roadmap(self):
        technical_sub_categories = Technical_Sub_Category.objects.all()
        technical_mini_sub_categories = Technical_mini_Sub_Category.objects.all()
        technical_sub_mini_sub_categories = Technical_sub_mini_Sub_Category.objects.all()
        non_technical_sub_categories = Non_Technical_Sub_Category.objects.all()
        non_technical_mini_sub_categories = Non_Technical_mini_Sub_Category.objects.all()
        non_technical_sub_mini_sub_categories = Non_Technical_sub_mini_Sub_Category.objects.all()
        company_info = Company_Info.objects.all()
        engineering_video_embed_code = Engineering_Video_Embed_Code.objects.all()


        context = {
            'technical_sub_categories': technical_sub_categories,
            'technical_mini_sub_categories': technical_mini_sub_categories,
            'technical_sub_mini_sub_categories': technical_sub_mini_sub_categories,
            'non_technical_sub_categories': non_technical_sub_categories,
            'non_technical_mini_sub_categories': non_technical_mini_sub_categories,
            'non_technical_sub_mini_sub_categories': non_technical_sub_mini_sub_categories,
            'company_info': company_info,
            'engineering_video': engineering_video_embed_code,
            'finance_video': Finance_Video_Embed_Code.objects.all(),
            'others_video': Marketing_Video_Embed_Code.objects.all(),
        }
        return render(self, 'career_roadmap.html', context)

    def partners_form(self):
        return render(self, 'partners_form.html')
    
    def about_us(self):
        return render(self, 'aboutus.html')