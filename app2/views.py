from django.shortcuts import render
from django.http import HttpResponse

def vistaDos(response):
    html="""
    <h1 style="color:red">Hola Mundo, esta es mi segunda vista</h1>
    <h2 style="color:purple">Me vuelvo a presentar, me llamo Alex</h2>
    <h1 style="color:blue">Estudio en Inacap</h1>
    <h2 style="color:green">Y tengo 20 años</h2>
    """
    return HttpResponse(html)
# Create your views here.
