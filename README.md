

# Git Hooks

This repository stores git hooks, and to be used in other projects.
Under `./githooks`, you will see the supporting languages and their custom hooks.

## Python Repository Setup
### For New Repo:
```
git pull && curl -o Makefile https://github.com/BIAD/ctrp-githooks/blob/master/Makefile && git add Makefile  && git commit --no-verify -m "added Makefile for githooks" && git push --no-verify
```

### For Existing Repo:

1) include the following Makefile in your project root folder.

```
githooks:
    curl -o .git/hooks/pre-commit https://raw.githubusercontent.com/BIAD/ctrp-githooks/master/.githooks/python/pre-commit.sh
    curl -o .git/hooks/pre-push https://raw.githubusercontent.com/BIAD/ctrp-githooks/master/.githooks/python/pre-push.sh
    curl -o pylintrc https://raw.githubusercontent.com/BIAD/ctrp-githooks/master/.githooks/python/pylintrc

    chmod +x .git/hooks/pre-commit
    chmod +x .git/hooks/pre-push

```

2) Run `make githooks` from your command line.


### PRE-COMMIT
When you run `git commit`, pylint check the quality of your python source code, and it will exclude these folders: venv,
env, lib. You can skip this hook using a no-verify flag: `git commit -n`

###  PRE-PUSH
When you run the `git push` command, it will trigger the test cases to run.
If the test cases fail, it will abort the push. The next step is to check the test coverage. If the test coverage is
below 95%, it will stop the push. You can skip this hook using: `git push --no-verify`



