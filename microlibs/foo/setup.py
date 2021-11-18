from setuptools import setup
microlib_name = 'macrolib.foo'

setup(
    name=microlib_name,
    version="0.1.0",
    author="yourname",
    author_email="yourname@email.com",
    description="Your microlib description",
    license="TBD",
    classifiers=[
        'Private :: Do Not Upload to pypi server',
    ],
    namespace_packages=['macrolib'],
    packages=[microlib_name],
    install_requires=[
        'macrolib.bar',
        # add more packages if needed
    ],
)