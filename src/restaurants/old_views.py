import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
# Function based views
#def home(request): # Contoh untuk melakukan Rendering Tampilan dengan Standard HTML
#    html_var = 'f strings'
#    html_ = f"""
#    <!DOCTYPE html>
#<html>
#    <head>
#    <title>Try Django with Python 3</title>
#    </head>
#    <body>
#        <h1>Hello World!</h1>
#        <p>This is {html_var} coming with Django</p>
#    </body>
#</html>    
#    """
#    return HttpResponse(html_)
##    return render(request, "home.html", {}) # Ini bagian responsenya

##Percobaan Untuk Materi Context Tag
#def home(request): # Contoh untuk melakukan Rendering Tampilan dengan Template
#    num = random.randint(0, 10000)
#    some_list = [num, random.randint(0, 10000), random.randint(0, 10000)]
#    var_context = {
#        "bool_item": True,
#        "nomor": num,
#        "some_list": some_list
#    } 
#    return render(request, "base.html", var_context) # Ini bagian responsenya & base.html adalah nama templatenya

def home(request):
    num = random.randint(0, 10000)
    some_list = [num, random.randint(0, 10000), random.randint(0, 10000)]
    var_context = {
        "bool_item": True,
        "nomor": num,
        "some_list": some_list
    } 
    return render(request, "home.html", var_context)

def about(request):
    var_context = {
    } 
    return render(request, "about.html", var_context)

def contact(request):
    var_context = {
        
    } 
    return render(request, "contact.html", var_context)


#class ContactView(View):
#    def get(self, request, *args, **kwargs):
#        var_context = {}
#        return render(request, "contact.html", var_context)

    
class HomeView(TemplateView):
    template_name = 'home.html'
    
    #Untuk memanggil context value pakai pola dibawah ini
    def get_context_data(self, *args, **kwargs):
        var_context = super(HomeView, self).get_context_data(*args, **kwargs)
        num = None
        some_list = [
            
            random.randint(0, 10000),
            random.randint(0, 10000),
            random.randint(0, 10000)
        ]
        condition_bool_item = True
        if condition_bool_item:
            num = random.randint(0, 1000)
            var_context = {
                
                "num" : num,
                "some_list" : some_list
                
            }
        return var_context
    
    
class ContactView(TemplateView):
    template_name = 'contact.html'
    
    
    
class AboutView(TemplateView):
    template_name = 'about.html'
    
    
    
# Catatan PENTING

## Kita menggunakan cara seperti dibawah ini jika dalam template kita terdapat context view
## Namun jika tidak ada context view yang ingin ditambahkan pada template kita , kita bisa langsung
## Melakukan pemanggilan Template langsung pada urls.py , dengan memimport template dan template_name
#class HomeView(TemplateView):
#    template_name = 'home.html'
#    
#    #Untuk memanggil context value pakai pola dibawah ini
#    def get_context_data(self, *args, **kwargs):
#        var_context = super(HomeView, self).get_context_data(*args, **kwargs)
#        num = None
#        some_list = [
#            
#            random.randint(0, 10000),
#            random.randint(0, 10000),
#            random.randint(0, 10000)
#        ]
#        condition_bool_item = True
#        if condition_bool_item:
#            num = random.randint(0, 1000)
#            var_context = {
#                
#                "num" : num,
#                "some_list" : some_list
#                
#            }
#        return var_context