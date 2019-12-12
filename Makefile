# .PHONY: test apidoc test-functions deploy daemon

help:	## Help to run
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

build:	## Build docker container
	docker build -t sentiment-docker .

dev:	## run docker container in dev mode
	docker run -p 6001:6001 -it -v $(shell pwd):/home/sentiment sentiment-docker /bin/bash
