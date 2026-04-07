from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'SANDEEP BADHAN'
SRC_REPO = 'src'

LIST_OF_REQUIREMENTS = [
    'streamlit',
    'scikit-learn',
    'pandas',
    'numpy'
]

setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='badhansandeep619@gmail.com',
    description='A small example package for sms or email spam detector',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),   # ✅ FIXED
    python_requires='>=3.7',
    install_requires=LIST_OF_REQUIREMENTS,
)