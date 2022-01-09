# Advanced-Web-Development-Midterm-REST-APP

REST API for the module Advanced Web Development (CM3035) - University of London

Midterm Coursework


## How to run the app

1. Open the git bash terminal in the VS Code editor

2. Navigate to the directory containing the source code.

3. Activate the virtual environment:

    `source REST-API/Scripts/activate`

4. Navigate to the project directory

cd REST

5. Run the app

    `python manage.py runserver 127.0.0.1:8000`

6. Access the endpoints by typing the following URLs in your web browser:

* GET

http://127.0.0.1:8000/api/protein/A0A016S8J7

* POST

http://127.0.0.1:8000/api/protein/

* GET

http://127.0.0.1:8000/api/pfam/PF00360

* GET

http://127.0.0.1:8000/api/proteins/55661

* GET

http://127.0.0.1:8000/api/pfams/55661

* GET

http://127.0.0.1:8000/api/coverage/A0A016S8J7
