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

@cli.command()
@click.argument('path')
@pass_config
def ls(config, path):
    """
    Similar to the 'ls' command at the Linux, please add 'gifs:' at the beginning of the path
    """

    if path.startswith('gifs:'):
        path = path[5:]
    else:
        click.echo('Please add "gifs:" at the beginning of the path')
        return
    try:
        files = helpers.list_files(config.repo, path)

        styles = {
            'dir': 'cyan',
            'file': 'white'
        }

        for file in files:
            click.secho(f'{file.name} ', fg=styles[file.type], nl=False)
        click.echo('')
    except:
        click.echo('An error occured')

@cli.command()
@click.argument('path')
@pass_config
def rm(config, path):
    """
    Remove a file on the Github repository, add 'gifs:' at the beginning of the path
    of the file

    Deleting a local file is not supported
    """

    if path.startswith('gifs:'):
        path = path[5:]
    else:
        click.echo('Please add "gifs:" at the beginning of the path')
        return
    try:
        helpers.delete_file(config.repo, path[5:])
        click.echo('File deleted successfuly')
    except:
        click.echo('An error occured')

@cli.command()
@click.argument('path')
@pass_config
def mkdir(config, path):
    """
    Creates a directory on the path
    """

    if path.startswith('gifs:'):
        path = path[5:]
    else:
        click.echo('Please add "gifs:" at the beginning of the path')
        return
    try:
        helpers.create_dir(config.repo, path)
        click.echo('Directory created successfuly')
    except:
        click.echo('An error occured')

@cli.command()
@click.argument('path')
@pass_config
def rmdir(config, path):
    """
    Deletes the directory on the path
    """

    if path.startswith('gifs:'):
        path = path[5:]
    else:
        click.echo('Please add "gifs:" at the beginning of the path')
        return
    try:
        helpers.delete_dir(config.repo, path)
        click.echo('Directory deleted successfuly')
    except:
        click.echo('An error occured')