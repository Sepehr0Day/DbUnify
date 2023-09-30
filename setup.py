from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='DbUnify',
    version='1.0.4',
    author='Sepehr0Day',
    description='A database manager unify for various database types',
    long_description=long_description,
    url="https://github.com/Sepehr0Day/DbUnify",
    long_description_content_type='text/markdown',
    packages=['DbUnify'],
    install_requires=[
        'pymysql',
        'psycopg2',
        'pymongo',
        'pyodbc',
        'matplotlib',
        'seaborn', 
        'reportlab'
    ],
)
