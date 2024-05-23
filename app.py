def solicitar_nota(bimestre):
    while True:
        try:
            nota = float(input(f"Digite a nota do {bimestre}º Bimestre: "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("A nota deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def calcular_media(notas):
    return sum(notas) / len(notas)

def main():
    while True:
        notas = []
        for i in range(1, 5):
            nota = solicitar_nota(i)
            notas.append(nota)

        media = calcular_media(notas)
        print("A média do aluno foi:", media)
        
        if media >= 7:
            print("Aprovado!!!")
        else:
            print("Reprovado!!!")
        
        # Pergunta ao usuário se deseja reiniciar o processo
        reiniciar = input("Deseja calcular a média de novo? (s/n): ").strip().lower()
        if reiniciar != 's':
            break

    print("Programa finalizado. Pressione Enter para sair...")
    input()

if __name__ == "__main__":
    main()
53