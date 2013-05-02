# Balanced Docs

This project builds the following Balanced documentation:

- [Specification](https://github.com/balanced/balanced-api)
- [Reference](https://www.balancedpayments.com/docs/api)
- [Overiew](https://www.balancedpayments.com/docs/overview)

## Contributing

All contributions, even simple grammar fixes, are greatly apprecaited.

1. Check for open [issues](https://github.com/balanced/balanced-docs/issues) or
   [open](https://github.com/balanced/balanced-docs/issues/new) a fresh issue
   to start a discussion around a feature idea or a bug.
1. Fork the repository on Github to start making your changes to the develop branch (or branch off of it).
1. Send a pull request!

Make sure to add yourself to `CONTRIBUTORS`. We will showcase the `CONTRIBUTORS` file on our
[COMMUNITY PAGE](https://balancedpayments.com/community).

After your pull request, email support [@] balancedpayments.com with
your address and the link to your pull request with your address and
your t-shirt size so we can send you your very own 
[Balanced t-shirt!](https://twitter.com/damon_sf/status/266768984744017920/photo/1)

## Setup

You'll first need:

* python 2.6+
* [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)

And then you can setup your environment like this:

```bash
git clone git@github.com:balanced/balanced-docs.git
cd balanced-docs
mkvirtualenv balanced-docs
python setup.py develop
pip install -r requirements.txt
```

If you've done that before just do:

```bash
cd /path/to/balanced-docs
workon balanced-docs
```

## Build

Now that your environment is setup lets build the docuementation.

### Specification

To build the [specification](https://github.com/balanced/balanced-api) do:

```bash
cd spec
make clean all
```

### Overview

To build the [overview](https://balancedpayments.com/docs/overview) do:

```bash
cd overview
make clean all
```

To preview the generated overview, just open up the html path printed by the
`Makefile` in your local browser which typically looks like this 

```bash
Build finished. The HTML pages are in /path/to/balanced-docs/overview/html.
```

### Reference

To build the [reference](https://balancedpayments.com/docs/api) do:

```bash
cd api
make clean all
```

To preview the generated reference, just open up the html path printed by the
`Makefile` in your local browser which typically looks like this 

```bash
Build finished. The HTML pages are in /path/to/balanced-docs/api/html.
```

## rST

All of the documentation is written in r(e)S(tructured)T(ext) which you can read
about [here](http://docutils.sourceforge.net/docs/user/rst/quickstart.html).

## dcode

We've added a custom rST directive called `dcode` which uses external scripts to
generate rST content. For example:

```
.. dcode:: scenario credit_create_new_bank_account
```

Here we are asking docde to run the `credit_create_new_bank_account`. The
output for that `scenario` will end up in place of the directive.

You'll also see a corresponding `dcode-default directive`. For example:

```
.. dcode-default:: scenario
    :script: ../scenario.py -d ../scenarios -c scenario.cache
    :section-chars: ~^
    :lang: python ruby php
```

This just registers an external script for `scenario`.

