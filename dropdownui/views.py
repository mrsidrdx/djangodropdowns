from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from num2words import num2words

# Create your views here.

geo_sample_dict = {
    'India' : {
        'Delhi' : ['Alipur', 'Bawana', 'East Delhi', 'South Delhi'],
        'Maharashtra' : ['Amravati', 'Badlapur', 'Goregaon', 'Mumbai'],
        'Odisha' : ['Angul', 'Balasore', 'Bhubaneswar', 'Sambalpur'],
        'Karnataka' : ['Bangalore', 'Belgaum', 'Dharwad', 'Mangalore'],
    },
    'USA' : {
        'Alabama' : ['Abbeville', 'Adamsville', 'Anniston', 'Auburn'],
        'Alaska' : ['Fairbanks', 'Girdwood', 'Ketchikan', 'Metlakatla'],
        'California' : ['Adelanto', 'Alameda', 'Brisbane', 'Burlingame'],
        'Georgia' : ['Dallas', ' Dawson County', 'Lakeland', 'Reidsville']
    }
}

def index(request):
    context = {
        'countries_list' : list(geo_sample_dict.keys()),
    }
    return render(request, 'dropdownui/index.html', context=context)

def get_states_list(request, country):
    states_list = list(geo_sample_dict[country].keys())
    return JsonResponse({'values':states_list})

def get_cities_list(request, country, state):
    cities_list = geo_sample_dict[country][state]
    return JsonResponse({'values':cities_list})

def generate_numbers_list(request):
    if request.is_ajax():
        if 'q' in request.GET:
            start = int(request.GET['q'])
            end = start + 20
            if 'page' in request.GET:
                start = int(request.GET['q']) + 20 * (int(request.GET['page']) - 1)
                end = start + 20
        elif 'page' in request.GET:
            page = int(request.GET.get('page'))
            end = page * 20 + 1
            start = end - 20
        else:
            page = 1
            end = page * 20 + 1
            start = end - 20
        numbers_list = list(range(start,end))
        return JsonResponse(numbers_list, safe=False)

def generate_number_words_list(request):
    if request.is_ajax():
        if 'q' in request.GET:
            start = int(request.GET['q'])
            end = start + 20
            if 'page' in request.GET:
                start = int(request.GET['q']) + 20 * (int(request.GET['page']) - 1)
                end = start + 20
        elif 'page' in request.GET:
            page = int(request.GET.get('page'))
            end = page * 20 + 1
            start = end - 20
        else:
            page = 1
            end = page * 20 + 1
            start = end - 20
        numbers_list = list(range(start,end))
    numbers_words_list = {}
    for number in numbers_list:
        numbers_words_list[number] = num2words(number)
    return JsonResponse(numbers_words_list)

def get_number_word(request, number):
    return JsonResponse({'numberword':num2words(number)})