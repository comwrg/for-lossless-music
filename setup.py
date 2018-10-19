from setuptools import setup
import for_lossless_music

with open('requirements.txt') as f:
    requires = f.readlines()

with open('README.rst') as f:
    readme = f.read()

setup(
    name='for-lossless-music',
    version=for_lossless_music.__version__,
    packages=['for_lossless_music'],
    url='https://github.com/comwrg/for-lossless-music',
    install_requires=requires,
    license='MIT',
    author='comwrg',
    author_email='xcomwrg@gmail.com',
    description='For lossless music!',
    long_description=readme,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Utilities',
        'Topic :: Internet :: WWW/HTTP',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={'console_scripts': ['for-lossless-music = for_lossless_music.__main__:main']},
)
