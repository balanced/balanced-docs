# Balanced Docs

This project generates Balanced documentation:

- [Specification](https://github.com/balanced/balanced-api)
- [Overiew](https://www.balancedpayments.com/docs/overview)
- [Reference](https://www.balancedpayments.com/docs/api)

## Contributing

Any minor contributions, even simple grammar fixes, are greatly apprecaited.

1. Check for open [issues](https://github.com/balanced/balanced-docs/issues) or
   [open](https://github.com/balanced/balanced-docs/issues/new) a fresh issue
   to start a discussion around a feature idea or a bug.
1. Fork the repository on Github to start making your changes to the develop branch (or branch off of it).
1. Send a pull request!

Make sure to add yourself to `CONTRIBUTORS`. We will showcase the `CONTRIBUTORS` file on our
[COMMUNITY PAGE](https://balancedpayments.com/community).

After your pull request, email support [@] balancedpayments.com with
your address and the link to your pull request with your address and
your t-shirt size so we can send you awesome
[Balanced t-shirt!](https://twitter.com/damon_sf/status/266768984744017920/photo/1)

### Installing

You'll first need
* python 2.6+
* [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/install.html)

And then you can setup your environment like this:

```bash
git clone git@github.com:balanced/balanced-docs.git
mkvirtualenv balanced-docs
python setup.py develop
pip install -r requirements.txt
```

If you've done that before just do:

```bash
cd /path/to/balanced-docs
workon balanced-docs
```

### Generating

Now that your environment is setup lets generate the docuementation.

#### Specification

To generate the [specification](https://github.com/balanced/balanced-api) do:

```bash
cd spec
make clean all
```

#### Overview

To generate the [overview](https://balancedpayments.com/docs/overview) do:

```bash
cd overview
make clean all
```

To preview the generated overview, just open up the html path printed by the
`Makefile` in your local browser which typically looks like this 

```bash
Build finished. The HTML pages are in ${SOME_ABSOLUTE_PATH}/balanced-docs/api/html.
```

#### Reference

To generate the [reference](https://balancedpayments.com/docs/api) do:

```bash
cd api
make clean all
```

To preview the generated reference, just open up the html path printed by the
`Makefile` in your local browser which typically looks like this 

```bash
Build finished. The HTML pages are in ${SOME_ABSOLUTE_PATH}/balanced-docs/api/html.
```

### Contributing

TODO

#### rST

TODO

#### dcode

TODO

#### Specification

TODO

#### Reference

TODO

#### Overview

TODO

