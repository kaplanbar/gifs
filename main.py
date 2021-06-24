from github import Github

import helpers

import click

class Config():

    def __init__(self):
        self.g = None
        self.repo = None

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.option(
    '--token',
    type=str,
    envvar='GIFS_TOKEN',
    required=True
)
@click.option(
    '--repo',
    type=str,
    envvar='GIFS_REPO',
    required=True
)
@pass_config
def cli(config, token, repo):
    config.g = Github(token)
    config.repo = config.g.get_repo(repo)

@cli.command()
@click.argument('src')
@click.argument('dest')
@pass_config
def cp(config, src, dest):
    """
    Copy a file from local to a Github repository or from a Github repository to local
    To use a path on a Github repository, you should add 'gifs:' at the beginning

    If the path is starts with 'gifs:' it will be treated as in the repository passed as --repo or in the GIFS_REPO env variable 
    """

    if src.startswith('gifs:') and dest.startswith('gifs:'):
        helpers.move_file(config.repo, src[5:], dest[5:])
    elif src.startswith('gifs'):
        helpers.download_file(config.repo, src[5:], dest)
    elif dest.startswith('gifs'):
        helpers.upload_file(config.repo, src, dest[5:])
    else:
        click.echo('Click does not support copying a local file to a local direction, add "gifs:" at the beginning of the path in repository')


if __name__ == '__main__':
    cli()
