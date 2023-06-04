# Written by JasonMo on 2023.06.02
# Copyright (c) 2021-2025 JasonMo All Rights Reserved

from setuptools import *

setup(

    name="OwlShell",
    version="0.0.1",
    author="JasonMo",
    author_email="jasonmo2009@hotmail.com",
    description="A shell written by python",
    packages=['owl', 'owl.commands'],
    install_requires=['prettytable>=3.7.0'],
    tests_require=['prettytable>=3.7.0'],
    python_requires='>=3.10',

    classifiers = [
        # 发展时期,常见的如下
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # 开发的目标用户
        'Intended Audience :: Developers',

        # 许可证信息
        'License :: OSI Approved :: MIT License',

        # 目标 Python 版本
        'Programming Language :: Python :: 3.11',
    ]
)