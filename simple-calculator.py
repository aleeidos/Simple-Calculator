#!/usr/bin/env python
# coding: utf-8

# In[10]:


print('Bem vindo à Calculadora simples!\n')
num1 = float(input('Para começarmos, digite um valor que deseja calcular: '))
num2 = float(input('Muito bem! Agora, digite outro valor que deseja calcular: '))
operador = input('''Qual operação você deseja fazer? Digite o sinal de operação que aparece após o "=":
multiplicação = *
divisão = /
soma = +
subtração = -\n''')

if operador == '*':
    resultado = num1 * num2
    print('O resultado do cálculo é: ', resultado)
    
elif operador == '/' and num2 != 0:
    resultado = num1 / num2
    print('O resultado do cálculo é: ', resultado)
    
elif operador == '+':
    resultado = num1 + num2
    print('O resultado do cálculo é: ', resultado)
    
elif operador == '-':
    resultado = num1 - num2
    print('O resultado do cálculo é: ', resultado)
    
else:
    print('Operação inválida, tente novamente!')


# In[ ]:





# In[ ]:




