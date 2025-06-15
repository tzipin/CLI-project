#!/usr/bin/env python3
import os
import click
from repository import Repository

repo = Repository(os.getcwd())


@click.group()
def cli():
    pass


@click.command()
def init():
    repo.wit_init()
    click.echo(f'Repository initialized at {repo.path}')


@click.command()
@click.argument('file_name')
def add(file_name):
    repo.wit_add(file_name)


@click.command()
@click.argument('message')
def commit(message):
    repo.wit_commit(message)


@click.command()
def log():
    repo.wit_log()


@click.command()
def status():
    repo.wit_status()


@click.command()
@click.argument('hash_code')
def checkout(hash_code):
    repo.wit_checkout(hash_code)


cli.add_command(init)
cli.add_command(add)
cli.add_command(commit)
cli.add_command(log)
cli.add_command(status)
cli.add_command(checkout)

if __name__ == '__main__':
    cli()
