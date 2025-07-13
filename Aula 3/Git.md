<!-- Clonar o repositorio pra sua maquina: Talvez precise usar o comando (git init) -->
git clone https://github.com/HenriqueMotton/curso-python.git

<!-- ENTRE NA PASTA -->
cd curso-python


<!-- PROCESSO PARA SUBIR -->
<!-- Realizando modificações e subindo para o projeto -->
git add .

<!-- Nome para o marco que você está subindo: -->
git commit -m "feat: adiciona aula 3 com exemplos de laços e listas"

<!-- Subindo para o repositório: -->
git push origin master
<!-- Caso você esteja subindo a sua branch para depois fazer um pull request! -->
git push --set-upstream origin nome-da-sua-branch


<!-- Caso não consiga subir direto na master, é porque precisa criar uma branch partindo da master(estando dentro da master) -->
git checkout -b nome-da-sua-branch
<!-- Realizou as modificações? Quer subir? -->
<!-- REPITA O PROCESSO: PROCESSO PARA SUBIR -->

