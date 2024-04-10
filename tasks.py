import sys

from invoke import task

PYTHON = "python" if sys.platform == "win32" else "python3"


@task
def example(c):
    """Run example code"""
    c.run(f"{PYTHON} heiwa4126_fizzbuzz/fizzbuzz.py")


@task
def test(c):
    """Run unit tests"""
    c.run(f"{PYTHON} -m unittest")


@task
def build(c):
    """Build project"""
    c.run(f"{PYTHON} -m build")
