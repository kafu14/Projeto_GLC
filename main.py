from carregador import carregar_gramatica
from gerador import gerar_cadeias
from interativo import modo_detalhado

def main():
    caminho = "C:\\Users\\Elion\\Documents\\projeto_GLC\\class\\gramatica.txt"
    
    try:
        gramatica = carregar_gramatica(caminho)
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado no caminho '{caminho}'")
        return
    except Exception as e:
        print(f"Erro ao carregar a gramática: {e}")
        return

    print("\nGramática carregada com sucesso!\n")
    print(gramatica)

    while True:
        print("\n--- MENU ---")
        print("1. Modo rápido (geração automática)")
        print("2. Modo detalhado (interativo)")
        print("0. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            try:
                qtd = int(input("Quantas cadeias deseja gerar? "))
                cadeias = gerar_cadeias(gramatica, limite=qtd)

                if not cadeias:
                    print("Nenhuma cadeia foi gerada.")
                else:
                    for i, (cadeia, regras) in enumerate(cadeias):
                        print(f"\nCadeia {i+1}: '{cadeia}'")
                        for passo in regras:
                            print(f"  {passo}")
            except ValueError:
                print("Por favor, insira um número inteiro válido.")
        elif opcao == "2":
            modo_detalhado(gramatica)
        elif opcao == "0":
            print("Encerrando programa.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
