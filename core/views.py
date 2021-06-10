from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, numero1, numero2):
    # return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))
    soma = numero1 + numero2
    return HttpResponse('<h1>Hello, a soma de {num1} e {num2} é {soma}.</h1>'.format(num1=numero1, num2=numero2, soma=soma))

def multiplicacao(request, numero1, numero2):
    multiplicacao = numero1 * numero2
    return HttpResponse('<h1>Hello, a multiplicação de {num1} e {num2} é {mult}.</h1>'.format(num1=numero1, num2=numero2, mult=multiplicacao))

def soma(request, numero1, numero2):
    soma = numero1 + numero2
    return HttpResponse('<h1>Hello, a soma de {num1} e {num2} é {soma}.</h1>'.format(num1=numero1, num2=numero2, soma=soma))

def divisao(request, numero1, numero2):
    try:
        divisao = numero1 / numero2
        message = ('<h1>Hello, a divisão de {num1} e {num2} é {div}.</h1>'.format(num1=numero1, num2=numero2, div=divisao))
    except ZeroDivisionError:
        message = ('<h1>Sorry ! You are dividing by zero.</h1>')
    finally:
        return HttpResponse(message)

def subtracao(request, numero1, numero2):
    subtracao = numero1 - numero2
    return HttpResponse('<h1>Hello, a soma de {num1} e {num2} é {sub}.</h1>'.format(num1=numero1, num2=numero2, sub=subtracao))
