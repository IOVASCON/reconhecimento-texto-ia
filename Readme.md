# Projeto de Reconhecimento de Texto com Tesseract OCR

## Descrição

Este projeto utiliza o OCR (Reconhecimento Óptico de Caracteres) para extrair texto de imagens usando a biblioteca Tesseract, integrada ao Python através do `pytesseract`. O objetivo é explorar a capacidade de transformar imagens contendo texto em texto digitalizado editável.

portanto, o foco desta aplicação prática de reconhecimento de texto é a extração dos textos contidos nas imagens.
Porque? porque este desafio é uma excelente maneira de explorar como a IA pode ser aplicada na prática para resolver problemas reais, como a extração de informações de imagens, que é amplamente utilizada em várias aplicações industriais e comerciais.

Veja os passos a seguir:

    1.  Seleção de Imagens:
        Incluir na pasta inputs algumas imagens que contêm texto que deseja extrair. Estas podem ser imagens de documentos, capturas de tela, placas, ou qualquer outro material visual que contenha texto legível.

    2.  Processamento das Imagens:
        Utilizando ferramentas de reconhecimento óptico de caracteres (OCR), você processará essas imagens para extrair o texto delas. Existem várias bibliotecas e APIs que podem ser utilizadas para isso, como Tesseract, Google Vision API, ou mesmo APIs providas pela OpenAI.

    3.  Salvar os Resultados:
        Os textos extraídos serão salvos na pasta output. Você pode salvar os resultados em formatos como texto puro (.txt) ou em um formato estruturado como JSON, que pode incluir informações adicionais como a localização do texto na imagem e a confiança na detecção.

    4.  Documentação:
        Documentar todo o processo, incluindo como as imagens são processadas, quais ferramentas foram usadas, exemplos de entrada e saída, e quaisquer desafios ou aprendizados durante o projeto.

## Configuração do Ambiente

O próximo passo é processá-las para extrair o texto. Para isso, vamos passar pelo processo de configuração e execução de uma ferramenta de OCR (Reconhecimento Óptico de Caracteres), neste caso, optamos pelo aplicativo Tesseract, uma biblioteca de OCR de código aberto, última versão 5.4.0.

### Instalação do Tesseract

O Tesseract OCR é um motor de OCR de código aberto que precisa ser instalado no sistema operacional antes de ser usado.

### Instalação da Biblioteca pytesseract

O `pytesseract` é uma biblioteca Python que facilita a interação com o Tesseract. Sua instalação foi feita via pip, e alguns desafios de permissão foram enfrentados e resolvidos ao executar o terminal como administrador.

    pip install pytesseract

#### Estrutura de Diretórios

    ReconhecimentoTextoIA
    │
    ├── inputs
    │   ├── imagem1.jpg
    │   ├── imagem2.png
    │   └── ...
    │
    ├── output
    │   ├── resultado1.txt
    │   ├── resultado2.txt
    │   └── ...
    │
    └── extract_text.py
    |__ Readme.md

- **inputs**: Pasta contendo as imagens das quais o texto será extraído.
- **output**: Pasta onde os textos extraídos são salvos como arquivos .txt.
- **extract_text.py**: Script Python que executa a extração de texto.
- **Readme.md**: este arquivo de documentação.

Para o seu projeto de reconhecimento de texto com IA, as pastas inputs e output terão papéis específicos. Aqui estão algumas ideias sobre o que você pode incluir em cada pasta para que o Git possa rastreá-las e para que você possa prosseguir com seu projeto:

Pasta inputs

Esta pasta deve conter as imagens das quais você deseja extrair texto. Aqui estão algumas sugestões de tipos de imagens:

    1.  Imagens de Documentos: Fotos ou scans de documentos como cartas, faturas ou páginas de livros.
    2.  Capturas de Tela: Imagens de páginas da web, e-mails ou qualquer interface que mostre texto que você deseja processar.
    3.  Imagens com Texto Incorporado: Fotos que incluem sinais, menus, ou qualquer objeto que tenha texto visível.

Você pode começar com algumas imagens de teste. Por exemplo, você pode usar imagens de domínio público ou criar algumas imagens de texto simples usando um editor de imagens.

Pasta output

Inicialmente, esta pasta estará vazia, mas aqui é onde você salvará os resultados do seu processo de reconhecimento de texto. Por exemplo:

    1.  Arquivos de Texto (.txt): Contendo o texto extraído de cada imagem correspondente.
    2.  Arquivos JSON: Podem incluir o texto extraído junto com metadados adicionais, como a posição do texto na imagem, confiança da detecção, etc.

Adicionar Arquivos de Exemplo

Como os diretórios vazios não são rastreados pelo Git, você pode adicionar um arquivo .gitkeep em cada diretório para permitir que eles sejam incluídos no repositório, mesmo estando vazios por enquanto. Isso é útil para manter a estrutura do diretório enquanto você ainda não tem arquivos de output para incluir. Você pode fazer isso executando:

    echo "" > inputs/.gitkeep
    echo "" > output/.gitkeep
    git add inputs/.gitkeep output/.gitkeep
    git commit -m "Add .gitkeep to maintain folder structure"

Após adicionar esses arquivos, você poderá fazer o commit e continuar o processo de configuração do seu repositório. Assim que tiver imagens e resultados para trabalhar, você pode remover os arquivos .gitkeep e adicionar os arquivos relevantes.

#### Script de Processamento de Imagem

Script Python

O script extract_text.py foi desenvolvido para automatizar o processo de extração de texto das imagens. Ele lê imagens de uma pasta inputs, processa cada uma usando o Tesseract e salva o resultado em textos na pasta output.

Exemplo básico de script Python que usa pytesseract para extrair texto de imagens

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

#### Explicação detalhada

    for img_file in os.listdir(input_dir):
        Este loop itera sobre cada arquivo no diretório especificado pela variável input_dir. A função os.listdir() retorna uma lista de todos os arquivos e diretórios no caminho especificado.

    if img_file.endswith(tuple(image_formats)):
        Esta linha verifica se o arquivo atual termina com uma das extensões de arquivo contidas na tupla image_formats. Isso ajuda a garantir que o script processe apenas arquivos de imagem.

    print(f"Processing {img_file}..."):
        Imprime uma mensagem para indicar qual arquivo está sendo processado no momento. Isso é útil para acompanhamento em tempo real do progresso do script.

    img_path = os.path.join(input_dir, img_file):
        Combina o diretório de entrada (input_dir) com o nome do arquivo de imagem para criar um caminho absoluto para o arquivo. Isso é necessário para abrir a imagem no próximo passo.

    img = Image.open(img_path):
        Abre o arquivo de imagem usando a função open() da biblioteca PIL.Image. Se o arquivo não puder ser aberto como uma imagem, isso gerará uma exceção.

    text = pytesseract.image_to_string(img):
        Chama o Tesseract OCR para extrair o texto da imagem. A função image_to_string() converte o conteúdo visual da imagem em texto string.

    with open(...) as file:
        Abre um arquivo de texto para escrita. Se o arquivo não existir, ele será criado. O nome do arquivo de texto é derivado do nome do arquivo de imagem, substituindo a extensão original por .txt.

    file.write(text):
        Escreve o texto extraído no arquivo de texto aberto. Isso salva o texto para uso posterior ou análise.

    except Exception as e:
        Captura quaisquer exceções que ocorram durante a abertura da imagem ou a extração do texto, permitindo que o script continue processando outros arquivos sem interrupção. A exceção capturada é impressa para ajudar no diagnóstico de problemas.

Esse código é uma parte essencial do seu projeto, lidando com a abertura, processamento e armazenamento do texto extraído de cada imagem de maneira eficiente e tratando possíveis erros para evitar falhas completas do script.

#### Execução do Script

Salve este script em um arquivo Python no seu diretório do projeto (neste projeto, extract_text.py) e execute-o no terminal integrado do VSCode

    python extract_text.py

Verificação dos Resultados:

Após a execução do script, verifique a pasta output para ver os arquivos de texto gerados. Cada arquivo deve conter o texto extraído de uma imagem correspondente

#### Tratamento de Erros Comuns

    1.  Inicialmente, o script tentou processar um arquivo .gitkeep, que não é uma imagem. A solução foi ajustar o script para filtrar apenas arquivos com extensões de imagem.
    2.  Ajustamos a sensibilidade a maiúsculas e minúsculas no script para aceitar formatos de imagem como .PNG e .JPEG.

#### Resultados e Aprendizados

Os resultados foram satisfatórios com a extração bem-sucedida de texto de várias imagens. Alguns dos aprendizados incluem:

    A importância de verificar e tratar os formatos de arquivos ao processar diretórios dinamicamente.
    Diferentes configurações de pré-processamento podem ser necessárias dependendo da qualidade e tipo das imagens.

**Como Usar**

- **Clone o repositório.**
- **Instale as dependências.**
- **Coloque suas imagens na pasta inputs.**
- **Execute o script extract_text.py.**
- **Verifique os textos extraídos na pasta output.**

#### Sugestões para Aperfeiçoamento

- **Pré-processamento de Imagens:** Implementar rotinas de ajuste de imagem (como correção de iluminação, alinhamento e escala) para melhorar a qualidade do texto extraído.
- **Suporte a Mais Formatos de Imagem:** Ampliar a lista de formatos suportados e melhorar a robustez do script para manipular diferentes tipos de arquivos de imagem.
- **Interface Gráfica:** Desenvolver uma interface gráfica para facilitar o uso do programa por usuários não técnicos.
- **Integração com APIs de Armazenamento:** Adicionar funcionalidade para salvar resultados diretamente em serviços de nuvem como Google Drive ou Dropbox.

#### Desafios e Soluções

Durante o desenvolvimento, enfrentamos vários desafios técnicos, principalmente relacionados à configuração do ambiente e peculiaridades do processamento de imagens com OCR. As soluções foram documentadas ao longo deste arquivo para ajudar em futuras configurações e execuções.

#### Conclusão

Este projeto demonstrou como a tecnologia OCR pode ser aplicada para extrair texto de imagens, facilitando processos que requerem digitalização e interpretação de documentos impressos ou escritos à mão.
