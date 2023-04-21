# API de pontos turisticos

## Sobre

#### Projeto realizado em Python/Django rest framework com o intuito de criar uma API com pontos turisticos levando em conta diversos pontos, como: Ponto turístico, localização, comentários, atrações, entre outros
#### O projeto permite a criação de pontos turisticos no banco de dados e que irá imitar uma aplicação real, contendo comentários sobre aquele ponto, localização, avaliações, etc
#### O foco deste projeto é utilizar as funções do Django Rest Framework a fim de aprendizado

## Como utilizar

#### Primeiro instale as dependencias do projeto com o pip instal -r requirements-dev.txt (ou requirements.txt caso deseje instalar as dependências de deploy no Heroku também)
#### Depois, basta rodar o aplicativo com o comando python manage.py runserver e apreciar
#### Na API há um requerimento de Token para que se possa manipular e alterar os dados, você pode criar seu usuário e utilizar o token do mesmo, não é necessário ter um token especial (token de admin, por exemplo). Então crie seu usuário e utilize o Token de reconhecimento do mesmo

## Rotas
#### &nbsp; &nbsp; &nbsp; &nbsp; * pontos turisticos (pontos-turisticos/)
#### &nbsp; &nbsp; &nbsp; &nbsp; * enderecos(enderecos/) 
#### &nbsp; &nbsp; &nbsp; &nbsp; * comentários (comentarios/)
#### &nbsp; &nbsp; &nbsp; &nbsp; * avaliações (avaliacoes/)
#### &nbsp; &nbsp; &nbsp; &nbsp; * autenticação do token (url do proprio django rest, api-token-auth/)
#### &nbsp; &nbsp; &nbsp; &nbsp; * para ver as imagens dos pontos turisticos e atrações


## Algumas bibliotecas

### python decouple
#### &nbsp; &nbsp; &nbsp; &nbsp; * Biblioteca responsável por pegar os dados necessários (secrect_key e debug) do sistema, mais especificamente da pasta .env
#### &nbsp; &nbsp; &nbsp; &nbsp; * É utilizada quando fizer deploy no Heroku

### dj-database-url
#### &nbsp; &nbsp; &nbsp; &nbsp; * Cria uma URL para o banco de dados, podendo utilizá-lo de maneira mais segura
#### &nbsp; &nbsp; &nbsp; &nbsp; * Cria-se a URL a partir a localização do banco de dados, caso não o encontre, utiliza um default

### dj-static
#### &nbsp; &nbsp; &nbsp; &nbsp; * Responsável por disponibilizar as imagens do projeto, já que o Djnago Rest Framework não tem uma disponibilização muito boa para essas imagens
#### &nbsp; &nbsp; &nbsp; &nbsp; * Ele trabalha com todos os arquivos estáticos, disponibilizando-os de maneira mais simples

### Pillow
#### &nbsp; &nbsp; &nbsp; &nbsp; * Uma das principais bibliotecas para trabalho com imagem do Python, ele é utilizado para pegar as imagens enviadas pelo usuário.
