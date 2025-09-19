import csv # Biblioteca para ler arquivos CSV

# --- Função para carregar mensagens do arquivo CSV ---
def carregar_mensagens(nome_arquivo='mensagens.csv'):
    """
    Lê um arquivo CSV e retorna uma lista com as mensagens.
    Assume que o CSV tem um cabeçalho e que as mensagens estão na segunda coluna.
    """
    mensagens = []
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            next(leitor_csv) # Pula a linha do cabeçalho (id,mensagem)
            for linha in leitor_csv:
                # Adiciona a mensagem (segunda coluna, índice 1) à lista
                mensagens.append(linha[1])
    except FileNotFoundError:
        # Se o arquivo não for encontrado, usa uma mensagem padrão
        print(f"Aviso: O arquivo '{nome_arquivo}' não foi encontrado. Usando mensagem padrão.")
        return ["Arquivo de mensagens não encontrado. Por favor, fale sobre seus sentimentos."]
    return mensagens

