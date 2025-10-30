
'''
FATEC - Faculdade de Tecnologia de São Paulo
Disciplina: Estrutura de Dados
PROF. Orlando Saraiva Júnior
Aluno: Jonas Pantoja 
PROVA 2 DO 2º SEMESTRE 2025
PROJETO: PROTOCOLO MANCHESTER

'''
#Importando as classes e funções necessárias

# main.py

from estruturadedados import NodoArvore, Fila, montar_arvore, triagem

def main():
    print("=== SISTEMA DE TRIAGEM MANCHESTER ===")

    # Criar filas
    filas = {
        "Vermelho": Fila(),
        "Laranja": Fila(),
        "Amarelo": Fila(),
        "Verde": Fila(),
        "Azul": Fila()
    }

    # Montar árvore
    arvore = montar_arvore()

    while True:
        print("\n1 - Cadastrar paciente")
        print("2 - Chamar paciente")
        print("3 - Mostrar status das filas")
        print("0 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            nome = input("Nome do paciente: ").strip()
            cor = triagem(arvore)
            print(f"Cor atribuída: {cor}")
            filas[cor].enqueue(nome)
            print(f"Paciente {nome} adicionado à fila {cor}.")

        elif opcao == "2":
            # Ordem de prioridade
            for cor in ["Vermelho", "Laranja", "Amarelo", "Verde", "Azul"]:
                if not filas[cor].vazia():
                    paciente = filas[cor].dequeue()
                    print(f"Chamando paciente da fila {cor}: {paciente}")
                    break
            else:
                print("Nenhum paciente nas filas.")

        elif opcao == "3":
            print("\n=== STATUS DAS FILAS ===")
            for cor, fila in filas.items():
                print(f"{cor}: {fila.tamanho()} paciente(s)")

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
