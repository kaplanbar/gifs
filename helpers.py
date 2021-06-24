import os
import requests

def upload_file(repo, local_file, path):
    try:
        with open(local_file, 'r') as f:
            content = f.read()
            repo.create_file(path, 'File uploaded by github-fs', content)
        print('File uploaded successfuly')
    except FileNotFoundError:
        print(f'{local_file} could not be found in the current directory')

def get_file_sha(repo, path):
    content = repo.get_contents(path)
    return content.sha

def delete_file(repo, path):
    sha = get_file_sha(repo, path)
    repo.delete_file(path, "File deleted by github-fs", sha)

def download_file(repo, path, fname = None):
    file = repo.get_contents(path)

    r = requests.get(file.download_url, allow_redirects = True)

    if not fname:
        fname = file.name

    with open(fname, "wb") as f:
        f.write(r.content)

    return fname

def create_dir(repo, path):
    repo.create_file(f'{path}/README.md', 'Directory created by github-fs', '')

def delete_dir(repo, path):
    contents = repo.get_contents(path)
    for content in contents:
        delete_file(repo, content.path)

def move_file(repo, path, new_path):
    fname = download_file(repo, path)
    delete_file(repo, path)
    upload_file(repo, fname, new_path)
    os.remove(fname)
