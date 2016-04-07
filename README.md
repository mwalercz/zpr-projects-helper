# zpr-projects-helper

Instalacja dla *ubuntu
---------
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
    * od tej pory wszystkie komendy pip install wykonujemy na wirtualnym środowisku (w terminalu powinno być to zaznaczone)
    
7. instalujemy biblioteki pythona3.4 dla wirtualnego środowiska "zpr-projects-helper", ktore bedą nam potrzebne
    * cd zpr-projects-helper
    * pip3.4 install -r requirements.txt
    
8. instalujemy postgresa i gui do postgresa 
    * sudo apt-get install postgresql
    * sudo apt-get install pgadmin3   
9. konfigurujemy bazę danych
    * odpalamy pgadmin3
    * dodajemy nowego użytkownika: username: projects_user, password: password
    * dodajemy nową baze danych: name: projects_helper
    
10. odpalamy serwer django
    * cd zpr-projects-helper
    * python manage.py runserver
    * wchodzimy w przeglądarce na stronę localhost:8000/projects - strona do zarządzania projektami
    
11. odpalamy testy
    * python manage.py test
    * jeśli nie będzie błędów to znaczy, że wszystko działa