# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import setuptools

with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="ecs_vpc",
    version="0.0.1",
    description="CDK Python app implementing VPC",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="author",
    package_dir={"": "ecs_vpc"},
    packages=setuptools.find_packages(where="ecs_vpc"),
    install_requires=[
        "aws-cdk.core==1.68.0",
        "aws-cdk.aws_ec2==1.68.0",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
)