
# aws-profile-gpg

A script for generating [aws-cli](https://github.com/aws/aws-cli) auth tokens from a [GPG](https://www.gnupg.org/) encrypted file allowing you to keep your credentials safe at rest.

If you use an [OpenGPG card](https://en.wikipedia.org/wiki/OpenPGP_card) such as a [Yubikey](https://www.yubico.com/support/knowledge-base/categories/articles/use-yubikey-openpgp/) as a private key, you can then effectively use it as a hardware MFA device.

## Prerequisites

This guide assumes you are familiar GPG and are able to encrypt your credentials file.

If you are not familiar with GPG, there are a number of [good tutorials online](https://duckduckgo.com/?q=gpg+tutorial).

#### MacOS

__Homebrew__

- _Follow instruction at [https://brew.sh](https://brew.sh)_

__Python, virtualenv__

- ```brew install python```

- ```pip install virtualenv```

__[GnuPG Made Easy (GPGME)](https://www.gnupg.org/related_software/gpgme/)__

- ```brew install gpgme```


## Setup and Install

Download the code:

```
git clone https://github.com/firstlookmedia/aws-profile-gpg.git
cd ./aws-profile-gpg
```

Create a virtualenv:

```
virtualenv venv
source venv/bin/activate
```

Install requirements:

```
pip install -r requirments.txt
```

There are two options documented here for making the script's virtualenv easily accessible:

1\. Move the provided wrapper script to a directory in the $PATH:

- Add `AWS_PROFILE_GPG_HOME` to `~/.bash_profile`:

```
$ vim ~/.bash_profile
...
$ grep ^AWS ~/.bash_profile
export AWS_PROFILE_GPG_HOME=~/local/aws-profile-gpg
```

- Copy virtualenv wrapper to $PATH:

```
cp ./aws-profile-gpg /usr/local/bin

$ which aws-profile-gpg
/usr/local/bin/aws-profile-gpg
```

2\. Create a wrapper bash function such as:

```
$ cat ~/.bash_profile
...

# required aws-profile-gpg env
export AWS_PROFILE_GPG_HOME="${HOME}/local/aws-profile-gpg"

# optional
export AWS_ENCRYPTED_CREDENTIALS_FILE="${HOME}/Dropbox/aws/credentials.gpg"
export AWS_CONFIG_FILE="${HOME}/Dropbox/aws/config"

# optional
export AWS_DEFAULT_PROFILE=default
export AWS_DEFAULT_REGION=ca-central-1

function aws-profile-gpg {
    $AWS_PROFILE_GPG_HOME/venv/bin/python \
    $AWS_PROFILE_GPG_HOME/aws-profile-gpg.py \
    $@
}

...
```


## Usage

__Basic usage__

```
usage: aws-profile-gpg.py [-h] [-v] command [command ...]

positional arguments:
  command        command passed to aws cli

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  verbose output
```

__Using default configuration__

```
aws-profile-gpg aws s3 ls
```

__Specifying an aws profile__

```
AWS_PROFILE=iam_leet \
aws-profile-gpg aws s3 ls
```

__Using with terraform__

```
AWS_PROFILE=terraform \
aws-profile-gpg terraform -plan
```

__Specifying an alternative credentials file__

```
AWS_ENCRYPTED_CREDENTIALS_FILE=/path/to/shared/aws/credentials.asc \
aws-profile-gpg aws s3 ls
```

__Specifying an alternative config file__

```
AWS_CONFIG_FILE=/path/to/shared/aws/config \
aws-profile-gpg aws s3 ls
```

Note: If you use an alternative `AWS_CONFIG_FILE`, any profile you use must be defined in specified config, including `default`.

If you try to use an undefined profile, you will see this error:
`Profile not found in config; profile=iam_leet`


#### Environmental Variables

* AWS_PROFILE_GPG_HOME
    * Path to `aws-profile-gpg` directory; Used to locate virtualenv and python script
    * Defaults to `/usr/local/opt/aws-profile-gpg`

* AWS_ENCRYPTED_CREDENTIALS_FILE
    * Path to GPG encrypted credentials file
    * Defaults to `~/.aws/credentials.gpg`

* AWS_CONFIG_FILE
    * See [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-environment)
    * Defaults to `~/.aws/config`
    * _Note:_ If you change this, you must define all profiles in the custom config file

* AWS_DEFAULT_PROFILE
    * See [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-environment)
    * Defaults to `default`



## Related Links

* Various version of `aws-profile` on GitHub
    * [https://github.com/search?q=aws-profile](https://github.com/search?q=aws-profile)

* Botocore
    * [https://github.com/boto/botocore](https://github.com/boto/botocore)

* PyGPGME
    * [https://launchpad.net/pygpgme](https://launchpad.net/pygpgme)
    * [https://pygpgme.readthedocs.io/en/latest/](https://pygpgme.readthedocs.io/en/latest/)

* GNU Privacy Guard (GPG)
    * [https://www.gnupg.org](https://www.gnupg.org)
