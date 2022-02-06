from github import Github
import github_actions
from github_path_parser import parse_github_path
import click

class Config():
    def __init__(self):
        self.github_client = None

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.option(
    '--token',
    type=str,
    envvar='GIFS_TOKEN',
    required=True
)
@pass_config
def cli(config, token):
    config.github_client = Github(token)

@cli.command()
@click.argument('src')
@click.argument('dest')
@pass_config
def cp(config, src, dest):
    """
    Copy a file from local to a Github repository or from a Github repository to local
    To use a path on a Github repository, you should add 'gifs:' at the beginning

    If paths start with gifs: they should be files in Github and they should start with org/repository (example: gifs:kaplanbar/gifs/setup.py)
    """

    if src.startswith('gifs:') and dest.startswith('gifs:'):
        github_actions.copy_file(config.github_client, parse_github_path(src[5:]), parse_github_path(dest[5:]))
    elif src.startswith('gifs'):
        github_actions.download_file(config.github_client, parse_github_path(src[5:]), dest)
    elif dest.startswith('gifs'):
        github_actions.upload_file(config.github_client, src, parse_github_path(dest[5:]))
    else:
        click.echo('Click does not support copying a local file to a local direction, add "gifs:" at the beginning of the path in repository')

@cli.command()
@click.argument('src')
@click.argument('dest')
@pass_config
def mv(config, src, dest):
    """
    Move a file in Github to destination

    Both of the paths should start with gifs: and they should start with org/repository (example: gifs:kaplanbar/gifs/setup.py)
    """

    if src.startswith('gifs:') and dest.startswith('gifs:'):
        github_actions.copy_file(config.github_client, parse_github_path(src[5:]), parse_github_path(dest[5:]))
    elif src.startswith('gifs'):
        github_actions.download_file(config.github_client, parse_github_path(src[5:]), dest)
    elif dest.startswith('gifs'):
        github_actions.upload_file(config.github_client, src, parse_github_path(dest[5:]))
    else:
        click.echo('Click does not support copying a local file to a local direction, add "gifs:" at the beginning of the path in repository')

@cli.command()
@click.argument('path')
@pass_config
def ls(config, path):
    """
    Similar to the 'ls' command at the Linux, please add 'gifs:' at the beginning of the path

    If paths start with gifs: they should be files in Github and they should start with org/repository (example: gifs:kaplanbar/gifs/setup.py)
    """

    if path.startswith('gifs:'):
        path = path[5:]
    else:
        click.echo('Please add "gifs:" at the beginning of the path')
        return
    try:
        files = github_actions.list_files(config.github_client, parse_github_path(path))

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
    of the file. Deleting a local file is not supported

    If paths start with gifs: they should be files in Github and they should start with org/repository (example: gifs:kaplanbar/gifs/setup.py)
    """

    if path.startswith('gifs:'):
        path = path[5:]
    else:
        click.echo('Please add "gifs:" at the beginning of the path')
        return
    try:
        github_actions.delete_file(config.github_client, parse_github_path(path))
        click.echo('File deleted successfuly')
    except Exception as e:
        print(e)
        click.echo('An error occured')

@cli.command()
@click.argument('path')
@pass_config
def mkdir(config, path):
    """
    Creates a directory on the path


    If paths start with gifs: they should be files in Github and they should start with org/repository (example: gifs:kaplanbar/gifs/exampledir)
    """

    if path.startswith('gifs:'):
        path = path[5:]
    else:
        click.echo('Please add "gifs:" at the beginning of the path')
        return
    try:
        github_actions.create_dir(config.github_client, parse_github_path(path))
        click.echo('Directory created successfuly')
    except:
        click.echo('An error occured')

@cli.command()
@click.argument('path')
@pass_config
def rmdir(config, path):
    """
    Deletes the directory on the path

    If paths start with gifs: they should be files in Github and they should start with org/repository (example: gifs:kaplanbar/gifs/exampledir)
    """

    if path.startswith('gifs:'):
        path = path[5:]
    else:
        click.echo('Please add "gifs:" at the beginning of the path')
        return
    try:
        github_actions.delete_dir(config.github_client, parse_github_path(path))
        click.echo('Directory deleted successfuly')
    except:
        click.echo('An error occured')