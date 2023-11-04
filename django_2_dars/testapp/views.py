from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

 
def main(request):
    return HttpResponse("Suhrob Allamurodov") 

def ism_familiya(request):
    return HttpResponse("<h1 style='color:green'>Suhrob Allamurodov</h1><h6>Suhrob Allamurodov</h6>")

def manzil(request):
    return HttpResponse(" <h4> Jizzax viloyati, Baxmal tumani</h4>")

def malumot(request):
    return HttpResponse("<h3>'Ipak yo'li' xalqaro turizm universiteti</h3>")

def umumiy(request):
    return HttpResponse(f"{main},{ism_familiya}, {manzil}, {malumot}")

def html(request):
    return render(request=request, template_name='test.html',context={})

