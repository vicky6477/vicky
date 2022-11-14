# wyf_class

## Virtual Environment
### Create a virtual environment
```
# python3 -m venv <venv-name>
python3 -m venv my_venv
```

### Activate venv
```
# source <venv-name>/bin/activate
source my_venv/bin/activate
```

# Basic Git

Check track/untracked files
```
git status

git add

git commit -m "<commit-message>"

```

## Sync local to remote

1. merge based approach
```
# load all changes from remote to local
git pull

# Now all changes are applied to local, push your local changes to remote
git push
```

2. rebase
```
git fetch origin main
git rebase
git push origin main --force
```
