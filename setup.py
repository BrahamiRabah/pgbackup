from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='brahami rabah',
    author_email='brahamirabah8@gmail.com',
    description='A utility for backing up PostgresSQL databases.',
    long_desription=long_description,
    long_description_content_type='test/markdown',
    url='http://github.com/brahamirabah/pgbackup',
    packages=find_packages('src')
)

