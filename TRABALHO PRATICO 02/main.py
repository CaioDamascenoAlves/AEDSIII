from caminho_critico import AnalisadorCaminhoCritico

def main():
    # Solicita ao usuário o caminho do arquivo
    caminho_arquivo = input("Digite o caminho do arquivo CSV: ")
    
    # Cria uma instância do analisador
    analisador = AnalisadorCaminhoCritico(caminho_arquivo)
    
    # Executa a análise
    analisador.analisar()

if __name__ == "__main__":
    main()