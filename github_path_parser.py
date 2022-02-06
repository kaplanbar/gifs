class GithubPath:
    def __init__(self, org: str, repo: str, path: str):
        self.org = org
        self.repo = repo
        self.path = path

    @property 
    def repo_path(self):
        return f"{self.org}/{self.repo}"
    
    def with_file_path(self, path: str):
        self.path = path
        return self


class InvalidGithubPathError(Exception):
    pass

def parse_github_path(path: str):
    if len(path) < 2:
        raise InvalidGithubPathError
    
    if path[0] == "/":
        path = path[1:]

    if path[-1] == "/":
        path = path[:-1]

    org_idx = path.find("/")
    if org_idx  == -1:
        raise InvalidGithubPathError
    repo_idx = path.find("/", org_idx + 1) 
    if repo_idx  == -1:
        raise InvalidGithubPathError
    return GithubPath(path[:org_idx], path[org_idx + 1:repo_idx], path[repo_idx+1:]) 
