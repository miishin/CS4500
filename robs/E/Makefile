all:	init install
init:
	chmod a+x xtcp
	python3 -m venv Other/E_env
install:
	( \
	source Other/E_env/bin/activate;\
	pip install -r Other/requirements.txt;\
	)

clean:
	rm -r Other/E_env