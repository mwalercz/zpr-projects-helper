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
    * pip3.4 install virtualenv
    * pip3.4 install virtualenvwrapper
    * export WORKON_HOME=~/Envs
    * mkdir -p $WORKON_HOME
    * source /usr/local/bin/virtualenvwrapper.sh
    * mkvirtualenv zpr-projects-helper
6. sprawdzamy czy domyślna wersja pythona na wirtualnym środowisku to 3.4
    * workon zpr-projects-helper
    * python -V    - powinna być python3.4.x
    * od tej pory komendy pip3.4 install wykonujemy na wirtualnym środowisku (w terminalu powinno być to zaznaczone)   
7. instalujemy biblioteki pythona3.4 dla wirtualnego środowiska "zpr-projects-helper", ktore bedą nam potrzebne
    * cd zpr-projects-helper
    * pip3.4 install -r requirements.txt    
8. instalujemy postgresa i gui do postgresa 
    * sudo apt-get install postgresql
    * sudo apt-get install pgadmin3   
9. konfigurujemy bazę danych
    * pgadmin3
    * dodajemy nowego użytkownika: 
        * username: projects_user, password: password
    * dodajemy nową baze danych: 
        * name: projects_helper, jej właścicielem (ownerem) powinien być projects_user
        * jeśli nie podoba nam się nazwa/użytkownik bazy danych to można to zmienić w settings/local.py
10. django tworzy dla nas bazę danych z dostępnych modeli
    * python3.4 manage.py makemigrations
    * python3.4 manage.py migrate  
11. odpalamy serwer django
    * cd zpr-projects-helper
    * jeśli nie podoba nam się nazwa bazy danych/użytkownik, to w settings/local.py -> DATABASES możemy sobie zmienić, równie dobrze możemy ustawić sqllite jako podstawową bazę i wtedy nic nie trzeba konfigurowac
8. django tworzy dla nas bazę danych z dostępnych modeli
    * python3.4 manage.py makemigrations
    * python3.4 manage.py migrate
9. odpalamy serwer django
    * python3.4 manage.py runserver
    * wchodzimy w przeglądarce na stronę localhost:8000/projects - strona do zarządzania projektami   
12. odpalamy testy
    * python3.4 manage.py test
    * jeśli nie będzie błędów to znaczy, że wszystko działa
