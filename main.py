from github import Github

def upload_file(repo, local_file, path):
    try:
        with open(local_file, 'r') as f:
            content = f.read()
            repo.create_file(path, "File upload using cpl", content)
        print('File uploaded successfuly')
    except FileNotFoundError:
        print(f'{local_file} could not be found in the current directory')

def main():
    g = Github('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')
    repo = g.get_repo('kaplanbar/test-repo')
    upload_file(repo, 'test.txt', 'test.txt')

if __name__ == '__main__':
    main()