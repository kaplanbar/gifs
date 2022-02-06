# Gifs

Gifs is a command-line application that allows you to use commands like "cp, ls, rm, mkdir, rmdir, mv" for Github repositories. 


## Usage/Examples

You have to add "gifs:" as a prefix to your paths if they are referring to a path in a repository. The path should start with `<org-name>/<repository-name>/`

```bash
export GIFS_TOKEN=<github-token>

gifs mkdir gifs:kaplanbar/gifs/testdir

gifs cp gifs.py gifs:kaplanbar/gifs/testdir/gifs.py

gifs cp gifs:kaplanbar/gifs2/gifs.py gifs:kaplanbar/gifs/testdir/gifs.py

gifs ls gifs:kaplanbar/gifs/.

gifs ls gifs:kaplanbar/gifs/testdir

gifs rm gifs:kaplanbar/gifs/testdir/gifs.py

gifs rmdir gifs:kaplanbar/gifs/testdir
```

## Run Locally

Clone the project

```bash
  git clone https://github.com/kaplanbar/gifs.git
```

Go to the project directory

```bash
  cd gifs
```

Run

```bash
  pip install .
```

You are ready to use gifs

```bash
  gifs --help
```

  

  
## License

[MIT](https://choosealicense.com/licenses/mit/)

  