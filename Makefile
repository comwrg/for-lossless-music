SETUP = python3 setup.py

all:
	@(python3 -c 'import for_lossless_music; print("for-lossless-music %s\n" % for_lossless_music.__version__)')

install:
	$(SETUP) install --user

release: clean
	$(SETUP) sdist bdist_wheel upload --sign

clean:
	-rm -r build/ dist/ *.egg-info/

# vim:ft=make
