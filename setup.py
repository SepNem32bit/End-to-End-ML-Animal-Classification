import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    project_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-End-ML-Animal-Classification"
AUTHOR_USER_NAME = "SepNem32Bit"
SRC_REPO = "animal classifier"
AUTHOR_EMAIL = ""


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Animal Classifier App (Cat or Dog)",
    long_description=project_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)