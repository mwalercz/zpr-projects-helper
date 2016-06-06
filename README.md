# zpr-projects-helper

Instalacja dla *ubuntu
----------------------
Jeśli posiadamy rozpakowany projekt, to pomijamy kroki 1-3.

1. ściągamy gita: 
    * sudo apt-get install git
2. (opcjonalny) ściagamy gui do gita np smartgit: http://www.syntevo.com/smartgit/download , w środku jest smartgit.sh ktory sluzy do odpalania aplikacji
3. ściągamy projekt
    * tworzymy nowy folder, w ktorym bedzie projekt:
        * mkdir zpr-projects-helper
        * cd zpr-projects-helper
    * klonujemy repo:
        * git clone https://github.com/mwalercz/zpr-projects-helper
4. ściągamy pythona 3.4: 
    * sudo apt-get install python3.4
5. ściągamy virtualenv i virtualenvwrapper i tworzymy środowisko o nazwie "zpr-projects-helper":
    * sudo pip install virtualenv
    * sudo pip install virtualenvwrapper
    * export WORKON_HOME=~/Envs
    * mkdir -p $WORKON_HOME
    * source /usr/local/bin/virtualenvwrapper.sh
    * mkvirtualenv zpr-projects-helper --python=python3.4
6. rozpoczynamy pracę na wirtualnym środowisku pythona
    * workon zpr-projects-helper
    * od tej pory komendy pip install wykonujemy na wirtualnym środowisku (w terminalu powinno być to zaznaczone)   
7. instalujemy biblioteki pythona3.4 dla wirtualnego środowiska "zpr-projects-helper", ktore bedą nam potrzebne
    * pip install -r requirements.txt    
8. instalujemy postgresa i gui do postgresa 
    * sudo apt-get install postgresql
    * sudo apt-get install pgadmin3   
9. konfigurujemy bazę danych
    * pgadmin3
    * dodajemy nowego użytkownika: 
        * username: projects_user, password: password
    * dodajemy nową baze danych: 
        * name: projects_helper, jej właścicielem (ownerem) powinien być projects_user
        * jeśli nie podoba nam się nazwa/użytkownik bazy danych to można to zmienić w settings/local.py, równie dobrze możemy ustawić sqllite jako podstawową bazę i wtedy nic nie trzeba konfigurowac
10. django tworzy dla nas bazę danych z dostępnych modeli
    * python manage.py makemigrations
    * python manage.py migrate  
11. uruchamiamy testy automatyczne razem z coverage 
    * coverage run manage.py test
    * jeśli nie będzie błędów to znaczy, że wszystko działa
12. generujemy raport z testów w folderze docs/coverage
    * coverage html
    * żeby otworzyć raport należy otworzyć plik docs/coverage/index.html w dowolnej przeglądarce
12. uruchamiamy serwer
    * python manage.py runserver
    * wchodzimy w przeglądarce na stronę localhost:8000 -> powinnismy zostać przekierowani na stronę logowania

