import datetime

def obter_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                return ano_nascimento
            else:
                print("Ano de nascimento inválido. Digite um valor entre 1922 e 2021.")
        except ValueError:
            print("Entrada inválida. Digite um valor numérico.")

def calcular_idade(ano_nascimento):
    ano_atual = datetime.date.today().year
    return ano_atual - ano_nascimento

def main():
    nome_completo = input("Digite seu nome completo: ")
    ano_nascimento = obter_ano_nascimento()
    idade = calcular_idade(ano_nascimento)

    print(f"Olá, {nome_completo}! Em 2023, você completou ou completará {idade} anos.")

if __name__ == "__main__":
    main()