from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    var_context = {}
    return render(request, template_name, var_context)