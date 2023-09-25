from django.shortcuts import render
from .models import SchoolData

# Create your views here.


def index(request):
    return render(request, 'mainapp/index.html')

def gender(request):
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
    context['male_count'] = male_count
    context['female_count'] = female_count
    context['other_count'] = other_count
    context['total_count'] = data_count


    return render(request, 'mainapp/gender.html', context=context)

def caste(request):
    data = SchoolData.objects.all()
    data_count = data.count()
    general_count = data.filter(caste="General").count()
    general_percentage = general_count/data_count*100
    scst_count = data.filter(caste="SC/ST").count()
    scst_percentage = scst_count/data_count*100
    obc_count = data.filter(caste="OBC").count()
    obc_percentage = obc_count/data_count*100

    context = {}
    context['general_count'] = general_percentage
    context['scst_count'] = scst_percentage
    context['obc_count'] = obc_percentage

    return render(request, 'mainapp/caste.html', context=context)

def age(request):
    data = SchoolData.objects.all()
    data_count = data.count()
    small_count = data.filter(age__gte=5).filter(age__lt=10).count()
    small_percentage = small_count/data_count*100
    middle_count = data.filter(age__gte=10).filter(age__lt=15).count()
    middle_percentage = middle_count/data_count*100
    teen_count = data.filter(age__gte=15).filter(age__lt=20).count()
    teen_percentage = teen_count/data_count*100

    context = {}
    context['small_count'] = small_percentage
    context['middle_count'] = middle_percentage
    context['teen_count'] = teen_percentage

    return render(request, 'mainapp/age.html', context=context)

def region(request):
    data = SchoolData.objects.all()
    data_count = data.count()
    hadwani_count = data.filter(address="Haldwani").count()
    bhimtal_count = data.filter(address="Bhimtal").count()
    ramnagar_count = data.filter(address="Ramnagar").count()
    bhowali_count = data.filter(address="Bhowali").count()
    mukteshwar_count = data.filter(address="Mukteshwar").count()
    nanital_count = data.filter(address="Nanital").count()
    haldwani_percentage = hadwani_count/data_count*100
    nanital_percentage = nanital_count/data_count*100
    bhimtal_percentage = bhimtal_count/data_count*100
    bhowali_percentage = bhowali_count/data_count*100
    ramnagar_percentage = ramnagar_count/data_count*100
    mukteshwar_percentage = mukteshwar_count/data_count*100
    

    context = {}
    context['haldwani_count'] = haldwani_percentage
    context['nanital_count'] = nanital_percentage
    context['bhimtal_count'] = bhimtal_percentage
    context['bhowali_count'] = bhowali_percentage
    context['ramnagar_count'] = ramnagar_percentage
    context['mukteshwar_count'] = mukteshwar_percentage


    return render(request, 'mainapp/region.html', context=context)

