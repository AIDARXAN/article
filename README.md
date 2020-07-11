

# Installation instructions

## Ubuntu and Ubuntu-based

### Python

1. Install prerequisites for Python build:
  ```bash 
  sudo apt-get update
  sudo apt-get install --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
  ```
1. Install pyenv: https://github.com/pyenv/pyenv#basic-github-checkout
1. Install Python: `pyenv install 3.7.4`
1. Install pyenv-virtualenv: https://github.com/pyenv/pyenv-virtualenv
1. Create virtualenv while in project directory: `pyenv virtualenv 3.7.4 article`
   
   * Virtualenv name `article` is important because `.python-version` also points to it. 
   It is needed for virtualenv to be activated automatically when you enter project directory 
   and deactivated when you leave.


In activated virtualenv install requirements:
```
pip install -r requirements.txt
```


Then run migrations:
```
./manage.py migrate
```



This will create a super user with username `admin` and password `Password123`

Run the backend dev server:
```
./manage.py runserver
```


Api urls:
```
/api/v1/categories
/api/v1/articles
```
