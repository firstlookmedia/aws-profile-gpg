
from setuptools import setup

setup(
    name='aws-profile-gpg',
    author="jeff oconnell",
    author_email="jeff.oconnell@firstlook.media",
    license="MIT",

    url='https://github.com/firstlookmedia/aws-profile-gpg',

    version='0.0.2',

    description='call aws-cli using access keys from an encrypted credentials file',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    scripts=['bin/aws-profile-gpg'],

    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, <4',

    install_requires=[
       'botocore>=1.12,<2',
       'PyGPGME>=0.3,<1',
    ],

    classifiers=(
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Topic :: Security :: Cryptography",
        "Topic :: System :: Systems Administration"
    )
)
