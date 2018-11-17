# S.I.E.
### Projedo simples em Django para controle de indicações de vendas

[![Build Status](https://travis-ci.org/tiagocordeiro/casaconceito-sie.svg?branch=master)](https://travis-ci.org/tiagocordeiro/casaconceito-sie)
[![Updates](https://pyup.io/repos/github/tiagocordeiro/casaconceito-sie/shield.svg)](https://pyup.io/repos/github/tiagocordeiro/casaconceito-sie/)
[![Python 3](https://pyup.io/repos/github/tiagocordeiro/casaconceito-sie/python-3-shield.svg)](https://pyup.io/repos/github/tiagocordeiro/casaconceito-sie/)


## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.

```
git clone https://github.com/tiagocordeiro/casaconceito-sie.git
cd casaconceito-sie
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python contrib/env_gen.py
python manage.py migrate
```


### Populando o banco de dados

Cria Categorias
```
python manage.py loaddata parceiros/fixtures/parceiros_categories.json
```
