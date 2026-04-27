def saudacao(nome: str) -> str:
    return f"Olá, {nome}! Conexão com GitHub funcionando1."


if __name__ == "__main__":
    nome = input("Digite seu nome: ")
    print(saudacao(nome))