from django.shortcuts import render
from django.http import HttpResponse
def vistaUno(request):
    html="""
    <h1 style="color:red">Hola Mundo</h1>
    <br>
    <h2 style="color:green">Mi nombre es Alex</h2>
    <br>
    <h1 style="color:blue">Tengo 20 años</h1>
    <br>
    <h2 style="color:purple">Estudio en INACAP</h2>
    """
    return HttpResponse(html)
# Create your views here.
