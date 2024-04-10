import os
import sys

import toml
from invoke import task
from packaging.version import Version
from packaging.version import parse

PYTHON = "py" if sys.platform == "win32" else "python3"
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
    c.run(".venv/bin/pip install -U packaging")
    c.run(".venv/bin/pip install -U -r requirements-dev.txt")


@task
def example(c):
    """Run example code"""
    c.run(f"{PYTHON} src/{SCOPE}/{PACKAGE}/fizzbuzz.py")


@task
def test(c):
    """Run unit tests"""
    c.run(f"{PYTHON} -m unittest")


@task
def build(c):
    """Build project"""
    if sys.platform == "win32":
        c.run("del /S /Q dist\\*")
    else:
        c.run("rm -rf dist/*")
    c.run(f"{PYTHON} -m build")


@task
def install(c):
    c.run(f"{PIP} install -U dist/*.whl")


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
    uninstall(c)
    build(c)
    install(c)


@task
def check(c):
    c.run("ruff check .")


@task
def fix(c):
    c.run("ruff check . --fix")


@task
def show(c):
    c.run(f"{PIP} show {PACKAGENAME}")


@task
def listwhl(c):
    c.run("zipinfo dist/*.whl")


@task
def listtarball(c):
    c.run("tar ztvf dist/*.tar.gz")


@task
def testpypi(c):
    c.run(f"{PYTHON} -m twine upload --repository testpypi dist/*")


@task
def release(c):
    """Release the project"""
    # Check if there are any uncommitted changes
    status = c.run("git status --porcelain", hide=True)
    if status.stdout:
        print("There are uncommitted changes. Please commit or stash them before releasing.")
        return

    # Read the current version from pyproject.toml
    with open("pyproject.toml", "r") as f:
        config = toml.load(f)
        current_version = parse(config["project"]["version"])

    # Increment the patch version
    new_version = Version(f"{current_version.major}.{current_version.minor}.{current_version.micro + 1}")

    # Commit the version change
    c.run(f"git commit -m 'Bump version to {new_version}' pyproject.toml")

    # Tag the commit with the new version
    c.run(f"git tag {new_version}")

    # Update the project version in pyproject.toml
    config["project"]["version"] = str(new_version)
    with open("pyproject.toml", "w") as f:
        toml.dump(config, f)
