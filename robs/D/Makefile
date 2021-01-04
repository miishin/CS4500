all:	init install
init:
	chmod a+x xgui
	python3 -m venv Other/D_env
install:
	( \
	source Other/D_env/bin/activate;\
	pip install -r Other/requirements.txt;\
	)

clean:
	rm -r Other/D_env
