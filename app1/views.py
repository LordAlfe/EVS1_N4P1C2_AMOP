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

def vistaTres(request):
    html="""
    <h1 style="color:blue">Hola Mundo, esta es mi primera vista</h1>
    <br>
    <h2 style="color:green">Mi nombre es Alex Oport</h2>
    <br>
    <h1 style="color:black">Tengo 20 años, uwu</h1>
    <br>
    <h2 style="color:red">Estudio en INACAP, en la carrera de ING. EN INFORMATICA</h2>
    """
    return HttpResponse(html)
# Create your views here.
