def calcular_imc(peso, altura):
    """
    Função para calcular o Índice de Massa Corporal (IMC) dado o peso e a altura.

    Argumentos:
    - peso: Peso da pessoa em quilogramas.
    - altura: Altura da pessoa em metros.

    Retorna:
    - O IMC calculado.
    """
    return peso / (altura ** 2)  # Calcula e retorna o IMC utilizando a fórmula peso / (altura ** 2)

def classificar_imc(imc):
    """
    Função para classificar o IMC de acordo com os valores padrão.

    Argumentos:
    - imc: Índice de Massa Corporal (IMC) da pessoa.

    Retorna:
    - Uma string indicando a classificação do IMC.
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 24.9:
        return "Peso normal"
    elif imc < 29.9:
        return "Sobrepeso"
    elif imc < 34.9:
        return "Obesidade grau I"
    elif imc < 39.9:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"

def main():
    """
    Função principal do programa.
    """
    peso = float(input("Digite o seu peso em quilogramas: "))  # Solicita ao usuário o peso em quilogramas
    altura = float(input("Digite a sua altura em metros: "))  # Solicita ao usuário a altura em metros

    imc = calcular_imc(peso, altura)  # Calcula o IMC
    classificacao = classificar_imc(imc)  # Classifica o IMC

    print(f"Seu IMC é {imc:.2f}, o que indica {classificacao}.")  # Exibe o IMC com duas casas decimais e sua classificação

if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa
