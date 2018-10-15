
# aws-profile-gpg

A script for calling the [aws-cli](https://github.com/aws/aws-cli) using [IAM Access Keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) from a [GPG](https://www.gnupg.org/) encrypted credentials file.

The script is inspired by the various [aws-profile](https://github.com/search?q=aws-profile) wrappers found on GitHub, plus a desire to keep credentials encrypted at rest.

## Benefits

1\. Your secret access keys are encrypted at rest on disk so if someone gains access to your machine, they still won't have access to your AWS credentials

2\. You can safely store your encrypted credentials in Dropbox or on a server so you can access the same config and credentials files from multiple machines

3\. Since the script works by decrypting the credentials file and adding `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` to the processes environment, you can use it with other apps the use these environment variables, e.g. [Terraform](https://www.terraform.io/docs/providers/aws/)

4\. If you use an [OpenGPG card](https://en.wikipedia.org/wiki/OpenPGP_card) such as a [Yubikey](https://www.yubico.com/support/knowledge-base/categories/articles/use-yubikey-openpgp/) as a private key, it will effectively act as a hardware MFA device for your access keys

_Details and use cases are outlined in __Usage__ below._

## Prerequisites

This guide assumes you are familiar GPG and are able to encrypt your credentials file.  If you are not familiar with GPG, there are a number of [good tutorials online](https://duckduckgo.com/?q=gpg+tutorial).

## Install

#### Using Homebrew ####

```
brew tap firstlookmedia/firstlookmediaa
brew install aws-profile-gpg
```

#### Bash Shortcuts

Creating shell functions is helpful for quickly invoking different profiles:

```
$ cat ~/.bash_profile

# optional
export AWS_ENCRYPTED_CREDENTIALS_FILE="${HOME}/Dropbox/aws/credentials.gpg"
export AWS_CONFIG_FILE="${HOME}/Dropbox/aws/config"

function aws-leet {
  AWS_PROFILE=iam_leet \
  aws-profile-gpg \
  aws \
  $@
}

function aws-terraform {
  AWS_PROFILE=terraform \
  aws-profile-gpg \
  aws \
  $@
}

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

__Storing config and credentials files in Dropbox__

```
AWS_CONFIG_FILE=${HOME}/Dropbox/etc/aws/config \
  AWS_ENCRYPTED_CREDENTIALS_FILE=${HOME}/Dropbox/aws/credentials.gpg \
  aws-profile-gpg aws s3 ls
```

__Using with terraform__

```
AWS_PROFILE=terraform \
  aws-profile-gpg terraform -plan
```


#### Note on Config Files

The `AWS_PROFILE` you use must be defined in your `AWS_CONFIG_FILE` file, e.g.

```
$ cat ~/.aws/config

[profile default]
region=us-east-1

[profile iam_leet]
region=us-east-1
```

This applies to the `default` profile too.

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
