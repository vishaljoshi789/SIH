from django.shortcuts import render
from .models import SchoolData

# Create your views here.

def index(request):
    data = SchoolData.objects.all()
    data_count = data.count()
    male_count = data.filter(gender="Male").count()
    male_percentage = male_count/data_count*100
    female_count = data.filter(gender="Female").count()
    female_percentage = female_count/data_count*100
    other_count = data.filter(gender="Other").count()
    other_percentage = other_count/data_count*100

    context = {}
    context['male_count'] = male_percentage
    context['female_count'] = female_percentage
    context['other_count'] = other_percentage

    return render(request, 'mainapp/index.html', context=context)

