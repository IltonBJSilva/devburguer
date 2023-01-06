# Dev Burguer!

Um projeto criado a fim de praticar praticas de desenvolvimento de software frontend e backend onde estarei documentando cada etapa

Estou desenvolvendo uma aplicação baseado nos principios do dry, oque seria?

### Não se repita? DRY e o dilema entre código duplicado e alto acoplamento
O princípio DRY ("não se repita") busca reduzir a duplicação de código e os problemas de manutenção resultantes, mas quando é mal aplicado aumenta o acoplamento e atrapalha a leitura do código. Conheça a opinião de vários especialistas sobre o princípio, suas aplicações e armadilhas.

DRY é uma abreviação para o inglês  _Don't Repeat Yourself_, "Não se Repita". É o primeiro princípio do desenvolvimento de software mencionado por Andy Hunt e Dave Thomas no clássico livro  [O Programador Pragmático: de aprendiz a mestre](http://en.wikipedia.org/wiki/The_Pragmatic_Programmer).

~~_____________________________________________________________________________~~

***Primeira etapa eu criei uma virtual environment***
``
python -m venv venv
``

***Segunda etapa eu instalei o Django***
``
pip install django
``

***Terceira  etapa criar o arquivo onde vai conter todas as depedencias do projeto***
``
pip freeze > requirements.txt
``

***Quarta etapa e criar um projeto django***
``
 django-admin startproject core .
 ``

***Quinta etapa ligar o projeto Django - Python***
``
python .\manage.py runserver
 ``

***Sexta etapa, criar um app do django***
``
 django-admin startapp burguer
 ``
 
Quando se cria uma aplicação a necessidade de registar o path em urls.py e tambem de registar a aplicação em settings.py

<<<<<<< HEAD
Tambem criar um arquivo urls.py dentro da aplicação pois a mesma não vem criada e isso torna-se um processo manual de ser feito
=======
Tambem criar um arquivo urls.py dentro da aplicação pois a mesma não vem criada e isso torna-se um processo manual de ser feito
>>>>>>> origin/master
