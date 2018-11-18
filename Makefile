SETUP = python3 setup.py

all:
	@(python3 -c 'import for_lossless_music; print("for-lossless-music %s\n" % for_lossless_music.__version__)')

install:
	$(SETUP) install --user

release: clean
	-git tag v$(shell make | grep -o '\d\.\d\.\d') && git push --tags
	$(SETUP) sdist bdist_wheel upload --sign
	@echo "\n\n\n"
	@git log --oneline --no-decorate --graph $(shell git tag --sort=-creatordate | sed -n '2p')..$(shell git tag --sort=-creatordate | sed -n '1p') | cat

clean:
	-rm -r build/ dist/ *.egg-info/

# vim:ft=make
