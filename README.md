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
uv venv 
```
Install project dependencies

```bash
# optional
pip install Django # (from scratch) or uv add django
django-admin startproject tested .

pip install -r requirements.txt # or uv sync
```
Add a "test_settings.py" file
```bash
touch ./tested/test_settings.py # if not exists


```
Create pytest, coverage configs" to the pyproject.toml and try it

Install pytest & plugins

```bash
pip install pytest-django # pip install pytest
pip install pytest-cov
pip install mixer

# using uv
uv add pytest-django --dev
uv add pytest-cov --dev
uv add mixer --dev

# required error reading pytest.ini file
deactivate && source .venv/bin/activate

# optional https://github.com/mverteuil/pytest-ipdb.git
pip install pdbpp # https://github.com/bretello/pdbpp
```
### Try it!
```bash
pytest # py.test
```

We are ready to test!

pytest will find all files called "test_*.py"

It will execute all functions called "test_*()" on all class
that start with "Test*"

## REFERENCES

https://www.youtube.com/watch?v=41ek3VNx_6Q
