# THE DJANGO TEST DRIVEN DEVELOPMENT COOKBOOK

## PROJECT SETUP

Let's create a new Django project
```bash
# from scratch
mkdir django-tested
# or just
git clone https://github.com/rokbot/django-tested

cd django-tested
```
Create virtual env and activate

```bash
python -m venv .venv && source .venv/bin/activate

```
Install project dependencies

```bash
# optional (from scratch)
pip install Django
django-admin startproject tested .

pip install -r requirements.txt
```
Add a "test_settings.py" file
```bash
touch ./tested/test_settings.py # if not exists
```
Install pytest & plugins and create "pytest.ini"

```bash
pip install pytest-django
# pip install pytest
pip install mixer
pip install pytest-cov

# required error reading pytest.ini file
deactivate && source .venv/bin/activate
$ pip install git+git://github.com/mverteuil/pytest-ipdb.git
```
### Try it!
```bash
pytest
```
Create ".coveragerc" and try it

We are ready to test!

pytest will find all files called "test_*.py"

It will execute all functions called "test_*()" on all class
that start with "Test*"

## REFERENCES
https://www.youtube.com/watch?v=41ek3VNx_6Q
