githooks:
	rm .git/hooks/pre-commit
	rm .git/hooks/pre-push

	wget https://raw.githubusercontent.com/BIAD/ctrp-githooks/master/.githooks/pre-commit.py -O .git/hooks/pre-commit
	wget https://raw.githubusercontent.com/BIAD/ctrp-githooks/master/.githooks/pre-push.py -O .git/hooks/pre-push

	chmod +x .git/hooks/pre-commit
	chmod +x .git/hooks/pre-push
