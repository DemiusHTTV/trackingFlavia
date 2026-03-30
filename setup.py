from pathlib import Path
from setuptools import setup

ROOT = Path(__file__).resolve().parent
README_PATH = ROOT / "README.md"
long_description = README_PATH.read_text(encoding="utf-8") if README_PATH.exists() else ""

setup(
    name='mtracker_jflavia',
    version='0.1.3',
    packages=['mtracker_jflavia'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    license_files=("LICENSE",),
    install_requires=[
        'pytest',
    ],
    description='A package for tracking memory usage of the Josephus problem implementation.',
    author='Dmitry Trubachev',  
    author_email='babygreenyoda@yandex.ru',
    url='https://github.com/DemiusHTTV/trackingFlavia',
)
