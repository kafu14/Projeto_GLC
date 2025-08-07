def modo_detalhado(gramatica):
    cadeia = [gramatica.inicial]
    passos = []

    print("\n--- MODO DETALHADO ---\n")
    print(f"Iniciando com: {''.join(cadeia)}")

    while any(simbolo in gramatica.variaveis for simbolo in cadeia):
        # Encontra o primeiro símbolo que é uma variável
        for i, simbolo in enumerate(cadeia):
            if simbolo in gramatica.variaveis:
                producoes = gramatica.producoes.get(simbolo, [])
                if not producoes:
                    print(f"Nenhuma produção encontrada para '{simbolo}'. Abortando derivação.")
                    return

                print(f"\nCadeia atual: {''.join(cadeia)}")
                print(f"O não-terminal '{simbolo}' pode ser substituído por:")
                for idx, p in enumerate(producoes):
                    print(f"  {idx + 1}. {p}")

                # Solicita escolha do usuário até que seja válida
                while True:
                    try:
                        escolha = int(input("Escolha uma produção (número): "))
                        if 1 <= escolha <= len(producoes):
                            break
                        else:
                            print("Opção fora do intervalo. Tente novamente.")
                    except ValueError:
                        print("Entrada inválida. Digite um número.")

                producao_escolhida = producoes[escolha - 1]
                nova_substituicao = [] if producao_escolhida == "epsilon" else list(producao_escolhida)
                cadeia = cadeia[:i] + nova_substituicao + cadeia[i+1:]
                passos.append(f"{simbolo} → {producao_escolhida}")
                break  # Sai do for e volta ao while principal

    print("\n--- DERIVAÇÃO CONCLUÍDA ---")
    print(f"Cadeia gerada: {''.join(cadeia) if cadeia else '(vazia)'}")
    print("Regras aplicadas:")
    for passo in passos:
        print(f"  {passo}")
