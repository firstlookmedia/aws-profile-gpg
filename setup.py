
from distutils.core import setup

setup(
    name='aws-profile-gpg',
    version='0.0.1',

    url='https://github.com/jefforulez/aws-profile-gpg',

    description='call aws-cli using access keys from an encrypted credentials file',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    scripts=['bin/aws-profile-gpg'],

    python_requires='~=2.7',
    install_requires=[
       'botocore>=1.4,<2',
       'PyGPGME>=0.3,<1',
    ]
)
