# Git Hooks

This repository stores git hooks, and to be used in other projects.
Under `./githooks`, you will see the supporting languages and their custom hooks.

## Python Repository Setup
1) include the following Makefile in your project root folder.

```
githooks:
    rm .git/hooks/pre-commit
    rm .git/hooks/pre-push

    curl -o .git/hooks/pre-commit https://raw.githubusercontent.com/BIAD/ctrp-githooks/master/.githooks/python/pre-commit.py
    curl -o .git/hooks/pre-push https://raw.githubusercontent.com/BIAD/ctrp-githooks/master/.githooks/python/pre-push.py

    chmod +x .git/hooks/pre-commit
    chmod +x .git/hooks/pre-push
```

2) Run `make githooks` from your command line.


