API REACT FLASK

1) crear archivo $ Pipfile


2) en terminal

    $$$$ pipenv shell 


3) crear app.py (seria como el index.js)

3.1) en terminal

    $$$$ pipenv install
    $ pipenv install flask
    $ pipenv install flask-script
    $ pipenv install flask-cors
    $ pipenv install flask-migrate
    $ pipenv install flask-cors
    $ pipenv install flask-sqlalchemy

flask: libreria ppal
flask-script y flask-migrate: para configurar el entorno de ejecucion de la app 
flask-cors: quien puede ver la pagina
flask-sqalchemy: conecta con el gestor de BBDD

genera un Pipfile.lock q es como el Package.json


5) en terminal 
    
    $ python app.py runserver


6) en terminal

    $ pipenv install PyMySQL

    
6) en terminal
    $ python app.py db init
    $ python app.py db migrate
    $ python app.py db upgrade

