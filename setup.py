import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "text_Summarization"
AUTHOR_USER_NAME = "Sasank Tanikella"
SRC_REPO = "Summarization"
AUTHOR_EMAIL = "sasank.tanikella7@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text summarization using NLP",
    long_description=long_description,
    long_description_content="text/markdown",
    url="https://github.com/SasankTanikella99/text_Summarization.git",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)