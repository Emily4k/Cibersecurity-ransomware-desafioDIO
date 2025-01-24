from cryptography.fernet import Fernet
import os


def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as arquivo_chave:
        arquivo_chave.write(chave)


def carregar_chave():
    with open("chave.key", "rb") as arquivo_chave:
        return arquivo_chave.read()


def criptografar_arquivo(caminho_arquivo, chave):
    with open(caminho_arquivo, "rb") as arquivo:
        dados = arquivo.read()
    fernet = Fernet(chave)
    dados_criptografados = fernet.encrypt(dados)
    with open(caminho_arquivo, "wb") as arquivo:
        arquivo.write(dados_criptografados)


def criptografar_diretorio(diretorio, chave):
    for pasta, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(pasta, arquivo)
            print(f"Criptografando: {caminho_arquivo}")
            criptografar_arquivo(caminho_arquivo, chave)


if __name__ == "__main__":
    diretorio_para_criptografar = input("Digite o caminho do diretório a ser criptografado: ")

    if not os.path.exists("chave.key"):
        gerar_chave()

    chave = carregar_chave()
    criptografar_diretorio(diretorio_para_criptografar, chave)
    print("Criptografia concluída!")
