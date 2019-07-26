githook:
	find .git/hooks -type l -exec rm {} \;
	find .githooks -type f -exec ln -sf ../../{} .git/hooks/ \;


	chmod +x .git/hooks/pre-commit
	chmod +x .git/hooks/pre-push




