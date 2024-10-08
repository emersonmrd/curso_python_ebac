import requests

def enviar_arquivo():
    # Caminho do arquivo para upload
    caminho = r"C:\Users\emers\Downloads\arquivo_teste.txt"

    # Enviar o arquivo
    requisicao = requests.post("https://file.io", files={"file": open(caminho, "rb")})
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao["link"]
    print(f"Arquivo enviado. Link para acesso:{url}")

def enviar_arquivo_chave():
    # Caminho do arquivo e chave para upload
    caminho = r"C:\Users\emers\Downloads\arquivo_teste.txt"
    chave_acesso = "" # API KEY

    # Enviar o arquivo 
    requisicao = requests.post(
        "https://file.io",
        files={"file": open(caminho, "rb")},
        headers={"Authorization": chave_acesso}
    )
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['link']
    print(f"Arquivo enviado com chave. Link para acesso:{url}")

def receber_arquivo(file_url):
    # Receber o arquivo
    requisicao = requests.get(file_url)

    # Salvar o arquivo
    if requisicao.ok:
        with open("arquivo_baixado.txt", "wb") as file:
            file.write(requisicao.content)
        print("Arquivo baixado com sucesso.")
    else:
        print("Erro ao baixar o arquivo: ", requisicao.json())

#enviar_arquivo()
#enviar_arquivo_chave()
receber_arquivo("https://file.io/AslMUUU44gPh")