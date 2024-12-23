print("SEJA BEM VINDO AO CALCULO DE IMC")
print("IREMOS MEDIR SEU INDICE DE MASSA CORPORAL, COM BASE DOS SEUS DADOS.")

def calcular_imc(peso, altura):
    return peso / (altura ** 2)
    ## Função do calculo IMC

def classificar_imc(imc):
    if imc < 18.5:
        return ("Abaixo do peso")
    elif 18.5 <= imc < 24.9:
        return("Peso normal")
    elif 25 <= imc < 29.9:
        return("Sobrepeso")
    elif 30 <= imc < 34.9:
        return("Obesidade grau 1")
    elif 35 <= imc < 39.9:
        return("Obesidade grau 2")
    else:
        return("Obesidade grau 3")
    
  ## Dados do usuario...
altura = float(input("Coloque sua altura em metros: "))
peso = float(input("Coloque seu peso em quilogramas: "))

imc = calcular_imc(peso, altura)

print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificar_imc(imc)}")
