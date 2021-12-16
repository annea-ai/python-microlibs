Python Microlibs
================

An implementation of Python Microlibs inspired by [this](https://medium.com/@jherreras/python-microlibs-5be9461ad979) excellent blogpost.

# Using the microlibs
Start by installing them with the provided `setup.py` file
```bash
python setup.py install
```
You have now installed the microlib packages and can run
```bash
python -c 'from macrolib.foo import module1' 
```

# Installing in dev mode
You can install the packages in (editable) dev mode by
```bash
python setup.py develop
```

# Running tests
You can run tests using [tox](https://tox.wiki/en/latest/install.html) by simply running `tox` in a directory containing a `tox.ini` file.

# Distribute
Individual microlibs cannot be distributed by the macrolib `setup.py`, but should be built individually by
```bash
python setup.py bdist_wheel 
```
These wheels can then be uploaded to a pypi server

## Local pypi server
You can start a pypi server by running
```bash
docker-compose up -d
```
in the root directory. This will serve packages built from the microlibs directory, and can thereafter be installed by: 
```bash
pip install --extra-index-url http://localhost:8080/simple/ macrolib.foo
```

# Applications
Contains runnable applications. Apps are by default run with docker, see example app in [baz](applications/baz/README.md).
