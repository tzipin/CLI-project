import os
import click
from repository import Repository

# # !/usr/bin/env python
# os.chmod(r"C:\ציפי לימודים\python\python project\project", 0o644)


@click.command()
def init():
    """Initialize the repository in the current working directory."""
    routing = os.getcwd()  # Get the current working directory
    Repository.wit_init(routing)  # Initialize the repository on this directory
    click.echo(f'Repository initialized at {routing}')


# @click.command()
# @click.argument()
# def add(file_name):
#     routing = os.getcwd()
#     Repository.wit_add(routing, file_name)


if __name__ == '__main__':
    init()
