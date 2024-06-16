# Classificador de abandono do tratamento da turbeculose

## Visão geral do projeto 
Seja bem vindo ao repositório sobre o classificador de abandono do tratamento da tuberculose 

Este repositório contém arquivos com implementações em python e dados para um projeto sobre marchine learning com o objetivo de prever o abandono de pacientes no tratamento da tuberculose, onde foram usados varios metodos e tecnicas para se chegar ao resultado desejado.

Imagem dos arquivos do projeto:

![alt text](imgReadme/imagearquivos.png)

## Sumário
1. [Banco-dados](#banco-dados)
2. [Instalação](#instalação)
3. [Executar](#executar-projeto)
4. [Contribuição](#contribuição)
5. [Agradecimentos](#agradecimentos)


## Banco Dados
Os bancos de dados pode ser encontrado na pasta **data** com um arquivo zipado com o titulo : *casos_tuberculose_2015-2022* com os dados a serem extraidos e também possuimos um arquivo csv com o nome *tuberculose_imputed*  para salvar as variáveis escolhidas para o projeto.

![alt text](imgReadme/data.png)

## Instalação

Para executar o projeto é necessário fazer umas instalações importantes antes de tudo (lembrando que está sendo usado Ubuntu 22.04).

Primeiramente é necessário ter os arquivos do programa apenas clonando na pasta que deseja: 

```
git clone https://github.com/intel-comp-saude-ufes/2024-1-P1-TB-treatment-abandonment-classifier.git
```

Instale o python e suas dependencias do projeto que se encontram dentro de requirements.txt: 
```
sudo apt-get install python3-pip
```

Dentro da pasta raiz que o repositório foi clonado insira o seguinte comando: 

```
pip3 install -r requirements.txt
```

Caso o usuário quiser usar jupyter instale-o através do comando: 
```
pip install notebook
```

## Executar projeto

Para executar o programa, basta executar o comando:

Aqui você vera as informaçoes analisadas: 
```
jupyter abandono_trat_tuberculose_analise.ipynb
```

Aqui é os dados sendo modelados :
```
jupyter modelando.ipynb
```

## Contribuição

Se você achou o projeto útil e interessante, sinta-se à vontade para deixar sua contribuição.

* Crie uma cópia do projeto original na sua conta.
* No GitHub, clique no botão "Fork" no canto superior direito do repositório.
* Use o comando git checkout -b <nome_branch> para criar um novo ramo.
* Adicione suas alterações ao staged com git add ..
* Confirme as alterações usando git commit -m 'add commit'
* Envie suas alterações com git push origin <nome_branch>
* Faça um pull request

## Agradecimentos

Agradecimentos ao professor [André Georghton Cardoso Pacheco](https://github.com/paaatcha) por proporcionar a oportunidade de concretizar este projeto.