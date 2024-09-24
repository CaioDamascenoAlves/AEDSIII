from caminho_critico import AnalisadorCaminhoCritico

def main():
    while True:
        # Solicita ao usuário o caminho do arquivo ou para sair
        caminho_arquivo = input("Digite o caminho do arquivo CSV ou 0 para sair: ")
        
        # Se o usuário digitar '0', encerra o programa
        if caminho_arquivo == '0':
            print("Encerrando o programa.")
            break
        
        # Caso contrário, continua com a análise
        try:
            # Cria uma instância do analisador
            analisador = AnalisadorCaminhoCritico(caminho_arquivo)
            
            # Executa a análise
            analisador.analisar()
        
        # Caso o arquivo não seja encontrado, exibe uma mensagem de erro
        except FileNotFoundError:
            print("Arquivo não encontrado. Tente novamente.")

if __name__ == "__main__":
    main()
