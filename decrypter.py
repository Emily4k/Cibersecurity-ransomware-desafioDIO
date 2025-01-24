from cryptography.fernet import Fernet
import os


def carregar_chave():
    with open("chave.key", "rb") as arquivo_chave:
        return arquivo_chave.read()


def descriptografar_arquivo(caminho_arquivo, chave):
    with open(caminho_arquivo, "rb") as arquivo:
        dados_criptografados = arquivo.read()
    fernet = Fernet(chave)
    dados_descriptografados = fernet.decrypt(dados_criptografados)
    with open(caminho_arquivo, "wb") as arquivo:
        arquivo.write(dados_descriptografados)


def descriptografar_diretorio(diretorio, chave):
    for pasta, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(pasta, arquivo)
            print(f"Descriptografando: {caminho_arquivo}")
            descriptografar_arquivo(caminho_arquivo, chave)


if __name__ == "__main__":
    diretorio_para_descriptografar = input("Digite o caminho do diretório a ser descriptografado: ")
    
    if not os.path.exists("chave.key"):
        print("Erro: Arquivo de chave não encontrado!")
        exit()

    chave = carregar_chave()
    descriptografar_diretorio(diretorio_para_descriptografar, chave)
    print("Descriptografia concluída!")
