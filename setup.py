# This file is used if we want to create a package of our project but since we don't want to, we will only 
    #create local package as of now

import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

__version__ = '0.0.0'

REPO_NAME = "TextSummarizer"
AUTHOR_USER_NAME = "shivdatta"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL = "shivdattaredekar@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)












