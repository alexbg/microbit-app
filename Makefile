PIP = .env/bin/pip
UFS = .env/bin/ufs

all: main lantern paint

main:
	@$(UFS) put main.py

lantern:
	@$(UFS) put lantern.py

paint:
	@$(UFS) put paint.py

install: virtualenv
	@$(PIP) install -Ur requirements.txt

virtualenv:
	@if ! [ -d ".env" ]; then\
		virtualenv .env;\
	fi
