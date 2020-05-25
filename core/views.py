from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(responde, nome, idade):
    return HttpResponse(f'<h1>Usuário: {nome}<br> Idade: {idade} </h1>'.title())
