"""Python setup.py for python_proj_template_1 package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("python_proj_template_1", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="python_proj_template_1",
    version=read("python_proj_template_1", "VERSION"),
    description="Awesome python_proj_template_1 created by jlcjohns",
    url="https://github.com/jlcjohns/python-proj-template-1/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="jlcjohns",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["python_proj_template_1 = python_proj_template_1.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
