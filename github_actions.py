import os
import requests

from github import Github
from github_path_parser import GithubPath 

def upload_file(github_client: Github, local_file: str, github_path: GithubPath):
    repo = github_client.get_repo(github_path.repo_path)
    with open(local_file, 'r') as f:
        content = f.read()
        repo.create_file(github_path.path, 'File uploaded by gifs', content)

def get_file_sha(github_client: Github, github_path: GithubPath):
    repo = github_client.get_repo(github_path.repo_path)
    content = repo.get_contents(github_path.path)
    return content.sha

def list_files(github_client: Github, github_path: GithubPath):
    repo = github_client.get_repo(github_path.repo_path)
    files = repo.get_contents(github_path.path)
    return files

def delete_file(github_client: Github, github_path: GithubPath):
    repo = github_client.get_repo(github_path.repo_path)
    sha = get_file_sha(github_client, github_path)
    repo.delete_file(github_path.path, "File deleted by gifs", sha)

def download_file(github_client: Github, github_path: GithubPath, fname = None):
    repo = github_client.get_repo(github_path.repo_path)
    file = repo.get_contents(github_path.path)
    r = requests.get(file.download_url, allow_redirects = True)
    if not fname:
        fname = file.name
    with open(fname, "wb") as f:
        f.write(r.content)
    return fname

def create_dir(github_client: Github, github_path: GithubPath):
    repo = github_client.get_repo(github_path.repo_path)
    repo.create_file(f'{github_path.path}/README.md', 'Directory created by gifs', '')

def delete_dir(github_client: Github, github_path: GithubPath):
    repo = github_client.get_repo(github_path.repo_path)
    contents = repo.get_contents(github_path.path)
    for content in contents:
        delete_file(github_client, github_path.with_file_path(content.path))

def move_file(github_client: Github, current_path: GithubPath, new_path: GithubPath):
    fname = download_file(github_client, current_path)
    delete_file(github_client, current_path)
    upload_file(github_client, fname, new_path)
    os.remove(fname)

def copy_file(github_client: Github, current_path: GithubPath, new_path: GithubPath):
    fname = download_file(github_client, current_path)
    upload_file(github_client, fname, new_path)
    os.remove(fname)
