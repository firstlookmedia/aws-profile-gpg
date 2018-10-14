
from distutils.core import setup

setup(
    name='aws-profile-gpg',
    version='0.0.1a',
    description='call aws-cli using access keys from an encrypted credentials file',
    long_description=open('README.md').read(),
    url='https://github.com/jefforulez/aws-profile-gpg',
    python_requires='~=2.7',
    scripts=['bin/aws-profile-gpg'],
)
