from setuptools import setup

setup(
    name='mtracker_jflavia',
    version='0.1',
    packages=['mtracker_jflavia'],
     long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
     license='MIT',
     license_files=("LICENSE",).
    install_requires=[
        'pytest',
    ],
    description='A package for tracking memory usage of the Josephus problem implementation.',
    author='Dmitry Trubachev',  
    author_email='babygreenyoda@yandex.ru',
    url='https://github.com/DemiusHTTV/culture_of_develop_trubachev/tree/main/mtackerJFlavia',
)