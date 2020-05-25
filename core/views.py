from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(responde, nome, idade):
    return HttpResponse(f'<h1>Usuário: {nome}<br> Idade: {idade} </h1>'.title())

def soma(response, v1, v2):
    return HttpResponse(f'Soma: {v1} + {v2} = {v1 + v2} ')

def mult(responde, v1, v2):
    return HttpResponse(f'Multiplicação: {v1} X {v2} = {v1*v2}')

def div(response, v1, v2):
    return HttpResponse(f'Divisão: {v1} / {v2} = {v1/v2:.2f}')

def subt(responde, v1, v2):
    return HttpResponse(f'Subtração: {v1} - {v2} = {v1-v2}')