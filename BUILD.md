
# Packaging for Distribution

The follow are general notes and commands for packaging and distributing this project from scratch.

## Homebrew

Install `pyenv` and create a virtualenv for the build:

```
brew install pyenv
pyenv install 2.7.15
pyenv virtualenv 2.7.15 aws-profile-gpg-2.7.15
```

Activate the virtualenv and install the dependencies:

```
pyenv local aws-profile-gpg-2.7.15
pip install -r requirements.txt
```

Make sure the script works:

```
./bin/aws-profile-gpg aws iam get-user
```

Install `poet` and generate Homebrew stanzas for dependent packages:

```
pip install homebrew-pypi-poet
```

```
poet botocore
poet PyGPGME

# or on macos
cat requirements.txt | cut -d ' ' -f 1 | xargs -Ixxx poet xxx
```

Tag and release a new version of this repo in GitHub:

- https://github.com/firstlookmedia/aws-profile-gpg/releases

Update the `version` and the dependencies stanzas in the Homebrew formula:

- https://github.com/firstlookmedia/homebrew-firstlookmedia/blob/stable/Formula/aws-profile-gpg.rb

Once the updates to the formula are committed, the following commands should install the new version on client machines:

```
brew update
brew upgrade aws-profile-gpg
```

#### Additional Reading

- https://docs.brew.sh/Python-for-Formula-Authors

## PyPi

Install `pyenv` and create a virtualenv for the build:

```
brew install pyenv
pyenv install 3.7.2
pyenv virtualenv 3.7.2 aws-profile-gpg-3.7.2
```

Activate the virtualenv and install the dependencies:

```
pyenv local aws-profile-gpg-3.7.2
pip install -r requirements.txt
```

Install required packaging tools:

```
pip install setuptools wheel
```

Update the version in `setup.py`:

```
version='0.0.2a',
```

Clean out old `dist/` and package the new one:

```
rm ./dist/*
python setup.py sdist bdist_wheel
```

Upload the new dist to *TestPyPI*:

```
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

Create a clean virtualenv and test the new distribution:

```
cd ~
pyenv virtualenv 3.7.1 clean-3.7.1
pyenv local clean-3.7.1
```

```
pip install \
  --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple \
  aws-profile-gpg
```

```
aws-profile-gpg aws iam get-user
```

If everything looks good, upload the new packages to production PyPi:

```
cd -
twine upload dist/*
```

#### Additional Reading

- https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives
- https://packaging.python.org/guides/using-testpypi/
