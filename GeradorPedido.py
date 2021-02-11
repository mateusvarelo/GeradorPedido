from random import randint
def geradorNumeroPedido(numeroPedido):
     for i in range(4):
          numero= randint(0,9)
          numeroPedido = numeroPedido + str(numero)   
     return numeroPedido
numeroPedido = ""
print(geradorNumeroPedido(numeroPedido))