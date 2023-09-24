from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='DbUnify',
    version='1.0.1',
    author='Sepehr0Day',
    description='A database manager unify for various database types',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['DbUnify'],
    install_requires=[
        'sqlite3',
        'pymysql',
        'psycopg2',
        'pymongo',
        'pyodbc',
    ],
)
