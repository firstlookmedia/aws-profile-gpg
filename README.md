
# aws-profile-gpg

Wrapper for calling [aws-cli](https://github.com/aws/aws-cli) for access keys from an encrypted credentials file.

## Prerequisites

#### MacOS

__Homebrew__

- _Follow instruction at [https://brew.sh](https://brew.sh)_

__Python, virtualenv__

- ```brew install python```

- ```pip install virtualenv```

__[GnuPG Made Easy (GPGME)](https://www.gnupg.org/related_software/gpgme/)__

- ```brew install gpgme```

## Install

#### From Source

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

Add `AWS_PROFILE_GPG_HOME` to `~/.bashrc`, for example:

```
$ vim ~/.bashrc
...
$ grep ^AWS ~/.bashrc
export AWS_PROFILE_GPG_HOME=~/local/aws-profile-gpg
```

Copy virtualenv wrapper to $PATH, for example:

```
cp ./aws-profile-gpg /usr/local/bin

$ which aws-profile-gpg
/usr/local/bin/aws-profile-gpg
```


## Running

__Using default configuration:__

```
aws-profile-gpg aws <command>
```

__Specifying an aws profile, for example:__

```
AWS_PROFILE=iam_leet \
aws-profile-gpg aws s3 ls
```

_Note:_ Profiles must be defined in the `AWS_CONFIG_FILE` or you will see this error:

`Profile not found in config; profile=iam_leet`


__Specifying alternative config and credentials files, for example:__

```
AWS_ENCRYPTED_CREDENTIALS_FILE=/path/to/shared/aws/credentials.asc \
AWS_CONFIG_FILE=/path/to/shared/aws/config \
aws-profile-gpg aws s3 ls
```

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

* AWS_DEFAULT_PROFILE
    * See [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-environment)
    * Defaults to `default`


## Related Links

* PyGPGME
    * [https://launchpad.net/pygpgme](https://launchpad.net/pygpgme)
    * [https://pygpgme.readthedocs.io/en/latest/](https://pygpgme.readthedocs.io/en/latest/)

* Inspred by the various version of `aws-profile` on GitHub
    * [https://github.com/search?q=aws-profile](https://github.com/search?q=aws-profile)

