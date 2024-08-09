# Importa as bibliotecas necessárias para o script
import pytesseract  # Interface Python para o Tesseract
from PIL import Image  # Biblioteca para abrir e manipular imagens
import os  # Biblioteca para interação com o sistema operacional

# Define o caminho para o executável do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Caminho do diretório contendo as imagens de entrada
input_dir = r'L:\VSCode\IA\ReconhecimentoTextoIA\inputs'

# Caminho do diretório onde os resultados serão salvos
output_dir = r'L:\VSCode\IA\ReconhecimentoTextoIA\output'

# Formatos de arquivo de imagem que o script pode processar
image_formats = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif', '.webp', '.PNG', '.JPG', '.JPEG', '.TIFF', '.BMP', '.GIF', '.WEBP')

# Loop sobre cada arquivo dentro do diretório especificado em 'input_dir'
for img_file in os.listdir(input_dir):
    # Verifica se o arquivo atual termina com uma das extensões de imagem especificadas em 'image_formats'
    if img_file.endswith(tuple(image_formats)):
        # Imprime o nome do arquivo que está sendo processado
        print(f"Processing {img_file}...")
        # Cria o caminho completo para o arquivo de imagem combinando o diretório de entrada e o nome do arquivo
        img_path = os.path.join(input_dir, img_file)
        try:
            # Tenta abrir a imagem usando a biblioteca PIL (Python Imaging Library)
            img = Image.open(img_path)
            # Usa o Tesseract para extrair o texto da imagem aberta
            text = pytesseract.image_to_string(img)
            # Abre (ou cria, se não existir) um arquivo de texto para salvar o texto extraído. O nome do arquivo de texto
            # corresponde ao nome do arquivo de imagem, mas com a extensão '.txt'
            with open(os.path.join(output_dir, f'{os.path.splitext(img_file)[0]}.txt'), 'w') as file:
                # Escreve o texto extraído no arquivo de texto
                file.write(text)
        # Captura exceções que podem ocorrer durante a abertura da imagem ou a extração de texto
        except Exception as e:
            # Imprime uma mensagem de erro se algo der errado durante o processamento do arquivo de imagem
            print(f"Failed to process {img_file}: {e}")

# Mensagem indicando que o processamento foi concluído
print("Processamento concluído!")
