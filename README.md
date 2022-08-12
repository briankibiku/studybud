## Django Project

## How to run this project locally
1. Clone project using this command ```git clone git@github.com:briankibiku/studybud.git```
2. cd into the project directory ```cd studybud```
3. Activate the virtual environment using this command ```. env/bin/activate```
4. Run project using this command ```python3  manage.py runserver```

### How to start a django project from scratch
1. Create a project folder and create a virtual env [see here](https://linoxide.com/how-to-create-python-virtual-environment-on-ubuntu-20-04) in it
2. Activate virtual
3. Install django using pip ```pip install django```
4. Create Project ```django-admin startproject <project_name>```
5. Run project ```python3  manage.py runserver```
6. Create base app Add templates ```python3 manage.py startapp <app_name>```
7. Connect app to our django project(studybud) 
8. Configure routes in base urls file

9. Navigation using <a< tag  
```<a href="{%url 'create-room'%}">Create Room</a>```