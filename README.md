# zpr-projects-helper

Instalacja szkieletu projektu dla *ubuntu
-----------------------------------------
Jeśli posiadamy rozpakowany szkielet projektu z innego źródła niż github, to pomijamy kroki 1-3.

1. ściągamy gita: 
    * sudo apt-get install git
2. ściągamy projekt
    * klonujemy repozytorium:
        * git clone https://github.com/mwalercz/zpr-projects-helper
    * przełączamy się na gałąź skeleton
        * cd zpr-projects-helper
        * git branch skeleton
3. ściągamy pythona 3.4: 
    * sudo apt-get install python3.4
4. ściągamy virtualenv i virtualenvwrapper i tworzymy środowisko o nazwie "zpr-projects-helper":
    * pip3.4 install virtualenv
    * pip3.4 install virtualenvwrapper
    * export WORKON_HOME=~/Envs
    * mkdir -p $WORKON_HOME
    * source /usr/local/bin/virtualenvwrapper.sh
    * mkvirtualenv zpr-projects-helper
5. sprawdzamy czy domyślna wersja pythona na wirtualnym środowisku to 3.4
    * workon zpr-projects-helper
    * python -V    - powinna być python3.4.x
    * od tej pory komendy pip3.4 install wykonujemy na wirtualnym środowisku (w terminalu powinno być to zaznaczone)   
6. instalujemy biblioteki pythona3.4 dla wirtualnego środowiska "zpr-projects-helper", ktore bedą nam potrzebne
    * cd zpr-projects-helper
    * pip3.4 install -r requirements.txt    
7. instalujemy postgresa i gui do postgresa 
    * sudo apt-get install postgresql
    * sudo apt-get install pgadmin3   
8. konfigurujemy bazę danych
    * pgadmin3
    * dodajemy nowego użytkownika: 
        * username: projects_user, password: password
    * dodajemy nową baze danych: 
        * name: projects_helper, jej właścicielem (ownerem) powinien być projects_user.   
    * jeśli chcemy stworzyć bazę danych o innej nazwie/innego użytkownika możemy wejść w settings/local.py i tam w Databases wpisać odpowiednie informacje(name/user)
8. django tworzy dla nas bazę danych z dostępnych modeli
    * python3.4 manage.py makemigrations
    * python3.4 manage.py migrate
9. odpalamy serwer django
    * cd zpr-projects-helper
    * python3.4 manage.py runserver
    * wchodzimy w przeglądarce na stronę localhost:8000/projects - strona do zarządzania projektami   
10. odpalamy testy
    * python3.4 manage.py test
    * jeśli nie będzie błędów to znaczy, że wszystko działa
