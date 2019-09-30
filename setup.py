# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="django-catalog",
    version=__import__('catalog').__version__,
    license="GPL",
    keywords="django catalog",

    author="Egor Slesarev",
    author_email="egor.slesarev@redsolution.ru",

    maintainer="Egor Slesarev",
    maintainer_email="egor.slesarev@redsolution.ru",

    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Natural Language :: Russian',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python:: 2.7',
        'Programming Language :: Python:: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
    ],
    packages=find_packages(),
    install_requires=['django-classy-tags<0.8', 'django-mptt==0.9.0',
                      "future==0.16.0"],
    include_package_data=True,
    zip_safe=False,
)
