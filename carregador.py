class Gramatica:
    def __init__(self, variaveis, inicial, terminais, producoes):
        self.variaveis = variaveis
        self.inicial = inicial
        self.terminais = terminais
        self.producoes = producoes

    def __str__(self):
        resultado = f"Variáveis: {self.variaveis}\n"
        resultado += f"Inicial: {self.inicial}\n"
        resultado += f"Terminais: {self.terminais}\n"
        resultado += "Produções:\n"
        for nt, regras in self.producoes.items():
            for r in regras:
                resultado += f"  {nt} → {r}\n"
        return resultado


def carregar_gramatica(caminho_arquivo):
    variaveis = []
    terminais = []
    inicial = ""
    producoes = {}
    lendo_producoes = False

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha or linha.startswith("#"):
                continue

            if linha.lower().startswith("variaveis:"):
                # Remove espaços e divide por vírgula
                variaveis = [v.strip() for v in linha.split(":", 1)[1].split(",")]
            elif linha.lower().startswith("terminais:"):
                terminais = [t.strip() for t in linha.split(":", 1)[1].split(",")]
            elif linha.lower().startswith("inicial:"):
                inicial = linha.split(":", 1)[1].strip()
            elif linha.lower() == "producoes":
                lendo_producoes = True
            elif lendo_producoes:
                if ":" in linha:
                    lado_esq, lado_dir = linha.split(":", 1)
                    lado_esq = lado_esq.strip()
                    lado_dir = lado_dir.strip()
                    if lado_esq not in producoes:
                        producoes[lado_esq] = []
                    producoes[lado_esq].append(lado_dir)

    return Gramatica(variaveis, inicial, terminais, producoes)
