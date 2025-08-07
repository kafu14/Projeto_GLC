from collections import deque

def eh_terminal(simbolo, terminais):
    return simbolo in terminais

def derivacao_mais_a_esquerda(gramatica, derivacao_atual):
    """
    Realiza uma derivação mais à esquerda a partir da derivação atual.
    Retorna uma lista com todas as novas derivações possíveis (uma para cada produção).
    """
    resultado = []

    for i, simbolo in enumerate(derivacao_atual):
        if simbolo in gramatica.variaveis:
            producoes = gramatica.producoes.get(simbolo, [])
            for p in producoes:
                # Substitui epsilon por cadeia vazia de forma segura
                nova_derivacao = (
                    derivacao_atual[:i]
                    + ([] if p == "epsilon" else list(p))
                    + derivacao_atual[i+1:]
                )
                resultado.append((nova_derivacao, f"{simbolo} → {p}"))
            break  # Substitui apenas o primeiro não-terminal encontrado
    return resultado

def gerar_cadeias(gramatica, limite=5):
    """
    Gera até `limite` cadeias únicas por derivação mais à esquerda.
    Mostra as derivações usadas.
    """
    cadeias_geradas = []
    fila = deque([ ([gramatica.inicial], []) ])  # (derivação atual, lista de regras aplicadas)

    while fila and len(cadeias_geradas) < limite:
        derivacao_atual, regras = fila.popleft()

        if all(eh_terminal(s, gramatica.terminais) for s in derivacao_atual):
            cadeia = ''.join(derivacao_atual)
            if cadeia not in [c[0] for c in cadeias_geradas]:
                cadeias_geradas.append((cadeia, regras))
        else:
            novos_passos = derivacao_mais_a_esquerda(gramatica, derivacao_atual)
            for nova_derivacao, regra in novos_passos:
                fila.append((nova_derivacao, regras + [regra]))

    return cadeias_geradas
