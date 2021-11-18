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