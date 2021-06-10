from django.test import TestCase

# Create your tests here.
def divisao(numero1, numero2):
    try:
        divisao = numero1 / numero2
        message = ('<h1>Hello, a divisão de {num1} e {num2} é {div}.</h1>'.format(num1=numero1, num2=numero2, div=divisao))
    except ZeroDivisionError:
        message = 'Sorry ! You are dividing by zero.'
    finally:
        print(message)

divisao(1,2)
