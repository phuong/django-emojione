import os
from setuptools import find_packages, setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-emojione',
    version='0.1.5',
    packages=find_packages(),
    py_modules=['django_emojione'],
    include_package_data=True,
    license='BSD License',
    description='Wrapper for emojione to use in django.',
    url='https://github.com/phuong/django-emojione',
    download_url='https://github.com/phuong/django-emojione/archive/master.zip',
    author='Phuong',
    author_email='boingonline@gmail.com',
    classifiers=[
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
