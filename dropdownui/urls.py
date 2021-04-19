from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("get_states_list/<str:country>/", get_states_list, name="get_states_list"),
    path("get_cities_list/<str:country>/<str:state>/", get_cities_list, name="get_cities_list"),
    path("generate_numbers_list/", generate_numbers_list, name="generate_numbers_list"),
    path("generate_number_words_list/", generate_number_words_list, name="generate_number_words_list"),
    path("get_number_word/<int:number>/", get_number_word, name="get_number_word"),
]
