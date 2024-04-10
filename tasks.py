import os
import sys

from invoke import task

PYTHON = "python" if sys.platform == "win32" else "python3"
PIP = "pip" if sys.platform == "win32" else "pip3"

SCOPE = "heiwa4126"
PACKAGE = "fizzbuzz"
PACKAGENAME = f"{SCOPE}-{PACKAGE}"


@task
def setup(c):
    """Setup virtual environment and install dependencies"""
    if not os.path.exists(".venv"):
        c.run(f"{PYTHON} -m venv .venv")
    c.run(".venv/bin/pip install -U -r requirements.txt")
    c.run(".venv/bin/pip install -U -r requirements-dev.txt")


@task
def example(c):
    """Run example code"""
    c.run(f"{PYTHON} {SCOPE}/{PACKAGE}/fizzbuzz.py")


@task
def test(c):
    """Run unit tests"""
    c.run(f"{PYTHON} -m unittest")


@task
def build(c):
    """Build project"""
    c.run(f"{PYTHON} -m build")


@task
def install(c):
    c.run(f"{PIP} install dist/*.whl")


@task
def ex1(c):
    c.run(f"{PYTHON} examples/ex1.py")


@task
def ex2(c):
    c.run(f"{PYTHON} examples/ex2.py")


@task
def uninstall(c):
    c.run(f"{PIP} uninstall {PACKAGENAME} --yes")


@task
def reinstall(c):
    c.run(f"{PIP} uninstall {PACKAGENAME} --yes")
    c.run(f"{PYTHON} -m build")
    c.run(f"{PIP} install dist/*.whl")


@task
def check(c):
    c.run("ruff check .")


@task
def fix(c):
    c.run("ruff check . --fix")
