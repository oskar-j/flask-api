DISTNAME = 'devtest'
DESCRIPTION = "A showcase of flask framework's capabilities including REST and SQL-ALchemy"
AUTHOR = 'Oskar Jarczyk'
AUTHOR_EMAIL = 'oskar.jarczyk@gmail.com'
MAINTAINER = 'Oskar Jarczyk'
MAINTAINER_EMAIL = 'oskar.jarczyk@gmail.com'
LICENSE = 'MIT License'
URL = 'https://github.com/oskar-j/flask-api'
VERSION = '0.1.0'
KEYWORDS = ['flask', 'sql-alchemy', 'rest', 'api', 'marhsmallow']
CLASSIFIERS = ['Development Status :: 3 - Alpha', ]


def setup_package():
    from setuptools import setup, find_packages

    metadata = dict(
        name=DISTNAME,
        description=DESCRIPTION,
        version=VERSION,
        classifiers=CLASSIFIERS,
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        maintainer=MAINTAINER,
        maintainer_email=MAINTAINER_EMAIL,
        license=LICENSE,
        url=URL,
        packages=find_packages(exclude=['*tests*']),
        install_requires=['click', 'Flask', 'Flask-SQLAlchemy', 'itsdangerous',
                          'Jinja2', 'MarkupSafe', 'marshmallow', 'marshmallow-sqlalchemy',
                          'nose2', 'SQLAlchemy', 'Werkzeug'])

    setup(**metadata)


if __name__ == '__main__':
    setup_package()
