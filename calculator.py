def soma(numero1, numero2):
	return numero1 + numero2

def subtracao(numero1, numero2):
	return numero1 - numero2

def multiplicacao(numero1, numero2):
	return numero1 * numero2

def divisao(numero, numero2):
	if numero2 == 0:
		print("erro: não divide por zero")
	return numero1 / numero2 



operacao = input("calculadora: escolha a operacao ")


numero1 = float(input("numero 1: escolha "))
numero2 = float(input("numero 2: escolha "))

if operacao == "soma":
	
	print(f"{soma(numero1, numero2)}")

elif operacao == "subtracao":

	print(f"{subtracao(numero1, numero2)}")

elif operacao == "multiplicacao":
	
	print(f"{multiplicacao(numero1, numero2)}")

elif operacao == "divisao":
	
	print(f"{divisao(numero1, numero2)}")
	