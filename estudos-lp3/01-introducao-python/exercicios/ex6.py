def converter_pontuacao_para_nota(pontuacao):
    if pontuacao < 0 or pontuacao > 100:
        return "Entrada inválida. Coloque uma pontuação de 0 a 100."
    
    if pontuacao >= 90:
        return 'A'
    elif pontuacao >= 80:
        return 'B'
    elif pontuacao >= 70:
        return 'C'
    elif pontuacao >= 60:
        return 'D'
    else:
        return 'F'
    
def main():
    try:
        pontuacao = float(input("Digite sua pontuação: "))
    except ValueError:
        print("Digite um número válido.")
        return
    
    nota = converter_pontuacao_para_nota(pontuacao)

    print(f"A pontuação corresponde à nota {nota}")

main()
