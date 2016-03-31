import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-emojione',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='Wrapper for emojione to use in django.',
    long_description=README,
    url='https://github.com/phuong/django-emojione',
    download_url='https://github.com/phuong/django-emojione/archive/master.zip',
    author='Phuong',
    author_email='boingonline@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
        "emojipy>=0.1",
    ],
)
