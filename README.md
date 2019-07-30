# Git Hooks

This repo stores git hooks, to be used in other projects. 
Under `./githooks`, you will see the supporting languages. 

## Python Repo Setup 
1) include the folllwing Makef file in your project folder. 

```buildoutcfg
githooks:
	rm .git/hooks/pre-commit
	rm .git/hooks/pre-push

	wget https://raw.githubusercontent.com/BIAD/ctrp-githooks/master/.githooks/python/pre-commit.py -O .git/hooks/pre-commit
	wget https://raw.githubusercontent.com/BIAD/ctrp-githooks/master/.githooks/python/pre-push.py -O .git/hooks/pre-push

	chmod +x .git/hooks/pre-commit
	chmod +x .git/hooks/pre-push
```

2) Run `make githooks` from your command line. 


