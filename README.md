
# aws-profile-gpg

A script for call the [aws-cli](https://github.com/aws/aws-cli) using a [GPG](https://www.gnupg.org/) encrypted credentials file, allowing you credentials safe at rest.

If you use an [OpenGPG card](https://en.wikipedia.org/wiki/OpenPGP_card) such as a [Yubikey](https://www.yubico.com/support/knowledge-base/categories/articles/use-yubikey-openpgp/) as a private key, you can then effectively use it as a hardware MFA device for your .

## Prerequisites

This guide assumes you are familiar GPG and are able to encrypt your credentials file.  If you are not familiar with GPG, there are a number of [good tutorials online](https://duckduckgo.com/?q=gpg+tutorial).

## Install

#### Using Homebrew ####

```
brew install jefforulez/aws-profile-gpg
```

#### Bash Shortcuts

Itreate a wrapper bash function such as:

```
$ cat ~/.bash_profile
...

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
usage: aws-profile-gpg [-h] [-v] command [command ...]

positional arguments:
  command        command passed to aws cli

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  verbose output
```

__Using the default configuration__

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

#### Note on Config Files

The `AWS_PROFILE` you use - even `default` - must be defined in your `AWS_CONFIG_FILE` file, e.g.

```
$ cat ~/.aws/config

[profile default]
region=us-east-1

[profile iam_leet]
region=us-east-1
```

If you try to use an undefined profile, you will see this error:
`Profile not found in config; profile=iam_leet`


#### Environmental Variables

* AWS_PROFILE_GPG_HOME
    * Path to `aws-profile-gpg` directory; Used to locate virtualenv and python script
    * Defaults to `/usr/local/opt/aws-profile-gpg`

* AWS_ENCRYPTED_CREDENTIALS_FILE
    * Path to GPG encrypted credentials file
    * Supports both plain `.gpg` and ascii-armored `.asc` files
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

* GNU Privacy Guard (GPG)
    * [https://www.gnupg.org](https://www.gnupg.org)

* PyGPGME
    * [https://launchpad.net/pygpgme](https://launchpad.net/pygpgme)
    * [https://pygpgme.readthedocs.io/en/latest/](https://pygpgme.readthedocs.io/en/latest/)

* Botocore
    * [https://github.com/boto/botocore](https://github.com/boto/botocore)

