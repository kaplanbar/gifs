# Gifs

Gifs is a command-line application that allows you to use commands like "cp, ls, rm, mkdir, rmdir" for Github repositories. 


## Usage/Examples

You have to add "gifs:" as a prefix to your paths if they are referring to a path in the repository.

```bash
gifs --token=token123 --repository=kaplanbar/repo123 cp main.cpp gifs:main.cpp

gifs --token=token123 --repository=kaplanbar/repo123 ls gifs:.

gifs --token=token123 --repository=kaplanbar/repo123 rm gifs:main.cpp

gifs --token=token123 --repository=kaplanbar/repo123 mkdir gifs:codes

gifs --token=token123 --repository=kaplanbar/repo123 rmdir gifs:codes
```

## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
  cd gifs
```

Run

```bash
  pip install --editable .
```

You are ready to use gifs

```bash
  gifs --help
```

  

  
## License

[MIT](https://choosealicense.com/licenses/mit/)

  