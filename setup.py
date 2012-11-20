from setuptools import setup
from torrent_stream import __version__

long_description = ""
try:
    readme = open("README.rst")
    long_description = str(readme.read())
    readme.close()
except:
    pass

setup(
    name='django-torrent-stream',
    version=__version__,
    description="Wraps the Torrent Stream http://torrentstream.org/",
    long_description=long_description,
    keywords='django, torrent, torrent stream',
    author='Mikhail Andreev',
    author_email='x11org@gmail.com',
    url='http://github.com/adw0rd/django-torrent-stream',
    license='BSD',
    packages=['torrent_stream', ],
    install_requires=['requests', ],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Programming Language :: Python",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
