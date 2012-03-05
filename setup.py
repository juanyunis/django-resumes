from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


README = read('README.rst')

setup(
    name = "django-resumes",
    packages = find_packages(),
    version = "0.1",
    author = "Juan C. Yunis",
    author_email = "juanyunis@juanyunis.com",
    url = "https://github.com/juanyunis/django-resumes",
    description = "Django App to create/generate resumes in HTML/PDF",
    long_description = "\n".join([README, ]),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords = ["resumes", "cv"],
)
