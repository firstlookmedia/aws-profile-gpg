
from distutils.core import setup

setup(
    name='aws-profile-gpg',
    version='0.0.1a',
    description='call aws-cli using access keys from an encrypted credentials file',
    long_description=open('README.md').read(),
    url='https://github.com/jefforulez/aws-profile-gpg',
    python_requires='~=2.7',
    entry_points={
        'console_scripts': [
            'aws-profile-gpg=aws-profile-gpg.__main__:main',
        ],
    },
)
