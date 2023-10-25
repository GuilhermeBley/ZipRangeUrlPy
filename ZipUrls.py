import urllib.request
import zipfile
from io import BytesIO

urls = ['https://example.com/arquivo1.txt', 'https://example.com/arquivo2.txt', 'https://example.com/arquivo3.txt']

nome_do_zip = 'arquivos_comprimidos.zip'

with zipfile.ZipFile(nome_do_zip, 'w') as zipf:
    for url in urls:
        try:
            with urllib.request.urlopen(url) as response:
                if response.getcode() == 200:
                    arquivo_nome = url.split('/')[-1]
                    conteudo = response.read()
                    zipf.writestr(arquivo_nome, conteudo)
                    print(f'O arquivo "{arquivo_nome}" foi baixado e adicionado ao ZIP.')
                else:
                    print(f'Erro ao baixar o arquivo da URL: {url}')
        except Exception as e:
            print(f'Erro ao baixar o arquivo da URL: {url} - {str(e)}')