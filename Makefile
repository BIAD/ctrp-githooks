githooks:
	rm .git/hooks/pre-commit
	rm .git/hooks/pre-push

	curl -o .git/hooks/pre-commit https://raw.githubusercontent.com/BIAD/ctrp-githooks/master/.githooks/python/pre-commit.py
	curl -o .git/hooks/pre-push https://raw.githubusercontent.com/BIAD/ctrp-githooks/master/.githooks/python/pre-push.sh

	chmod +x .git/hooks/pre-commit
	chmod +x .git/hooks/pre-push
