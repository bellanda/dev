# Email Signature Base64 Converter

Este script converte todas as imagens referenciadas em um arquivo HTML para o formato base64, permitindo que elas fiquem embutidas diretamente no HTML, sem necessidade de arquivos externos.

## Requisitos

Instale as dependências necessárias:

```bash
pip install beautifulsoup4 requests
```

## Como usar

Execute o script Python:

```bash
cd script
python email_base64_converter.py
```

O script vai:

1. Ler o arquivo `email-sign.html` na pasta raiz
2. Converter todas as imagens para base64
3. Gerar um novo arquivo `email-sign-base64.html` na pasta raiz

## Vantagens

- O arquivo HTML com as imagens em base64 pode ser usado em qualquer lugar sem depender de arquivos externos
- Ideal para assinaturas de email, onde links externos podem ser bloqueados
- O conteúdo é visualizado mesmo offline

## Observações

- O tamanho do arquivo HTML aumentará significativamente
- Algumas plataformas de email têm limitações de tamanho para assinaturas
