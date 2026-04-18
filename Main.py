def saudacao(nome: str) -> str:
    return f"Olá, {nome}! Conexão com GitHub funcionando."


if __name__ == "__main__":
    nome = input("Digite seu nome: ")
    print(saudacao(nome))