# THE DJANGO TEST DRIVEN DEVELOPMENT COOKBOOK

## PROJECT SETUP

Let's create a new Django project

```bash
$ mkvirtualenv tried_and_tested
$ pip install Django
$ django-admin.py startproject tested
```

Add a "test_settings.py" file
```bash
$ cd tested/tested
$ touch test_settings.py
```
Install pytest & plugins and create "pytest.ini"

```bash
$ pip install pytest
$ pip install pytest-django
$ pip install git+git://github.com/mverteuil/pytest-ipdb.git
$ pip install pytest-cov
$ deactivate
$ workon tried_and_tested
```
### Try it!
```bash
$ py.test
```
Create ".coveragerc" and try it

We are ready to test!

py.test will find all files called "test_*.py"

It will execute all functions called "test_*()" on all class
that start with "Test*"

## REFERENCES
https://www.youtube.com/watch?v=41ek3VNx_6Q