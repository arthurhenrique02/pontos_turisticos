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

#### Há rotas para pontos turisticos (pontos-turisticos/), enderecos(enderecos/), comentários (comentarios/), avaliações (avaliacoes/), autenticação do token (url do proprio django rest, api-token-auth/) e para ver as imagens dos pontos turisticos e atrações

