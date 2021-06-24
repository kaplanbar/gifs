from github import Github

def main():
    g = Github('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')
    repo = g.get_repo('kaplanbar/test-repo')
    


if __name__ == '__main__':
    main()