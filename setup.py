import setuptools


__version__ = "0.0.1"

REPO_NAME = "mushroom_classification"
AUTHOR_USER_NAME = "Sou2002"
SRC_REPO = "src"
AUTHOR_EMAIL = "souravbnjee07@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for mushroom classification",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
