# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:53:41 2019

@author: Simon Zhou
"""
from setuptools import setup, find_packages

setup(
    name='yima',
    version=0.1.0,
    author='Simon Zhou',
    author_email='yihua.zhou@outlook.com',
    description=(
        '<项目的简单描述>'
    ),
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/SimZhou/yima',
    packages=find_packages(),
    platforms=["all"],
    install_requires=[
        'time',
        'requests>=2.19.0',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)