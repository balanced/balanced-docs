# Balanced Docs

This is the framework that we use to run Balanced's documentation against against our API servers and generate
the documentation in html form.

This is how our documentation is generated!

## Contributing

Any minor contributions, even a simple grammar fix are greatly
apprecaited.

1. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
1. Fork the repository on Github to start making your changes to the develop branch (or branch off of it).
1. Send a pull request!

Make sure to add yourself to `CONTRIBUTORS`. We will showcase the
`CONTRIBUTORS` file on our
[COMMUNITY PAGE](https://balancedpayments.com/community).

After your pull request, email support [@] balancedpayments.com with
your address and the link to your pull request with your address and
your t-shirt size so we can send you awesome
[Balanced t-shirt!](https://twitter.com/damon_sf/status/266768984744017920/photo/1)

## Getting Started

### Installing

* `mkvirtualenv balanced-docs`
* `python setup.py develop`
* `pip install -r requirements.txt`
* `make clean`

#### Generating

To generate the [API reference](https://balancedpayments.com/docs/api), just issue a:

```bash
make api
```

To generate the [overview](https://balancedpayments.com/docs/overview) reference, just issue a:

```bash
make overview
```

##### How do I preview?

To preview the generated `api` or `overview` reference, just open up
the html path printed by the `Makefile` in your local browser. It
typically looks like:

    Build finished. The HTML pages are in ${SOME_ABSOLUTE_PATH}/balanced-docs/overview/html

OR

    Build finished. The HTML pages are in ${SOME_ABSOLUTE_PATH}/balanced-docs/api/html


## How do I add some new documentation for the reference?

At a high level, works by having various reStructuredText
files that are included in the main `index.rst`. The `index.rst` file then
just includes the various endpoint documentation and renders them through
the various directives.

### How do these directives work?

#### What is the layout for every example?

Before we start, we should discuss the layout we're attempting to achieve.

The ultimate end goal is that all examples follow this structure:

```html
<div class="method-section">
  <div class="method-description">
  <!-- includes the request form, if any -->
  </div>
  <div class="method-example">
  <!-- includes defintion, example, and response -->
  </div>
</div>
```

Let's take for example the `Creating a New Bank Account` endpoint. I will now
work through an entire example:

```rst
.. cssclass:: method-section

creating a new bank account
---------------------------

Creates a new bank account.

.. container:: method-description

  .. fields that are required or optional for the endpoint

.. container:: method-examples

  .. dcode:: bank_account_create
```

#### Breakdown

```rst
.. cssclass:: method-section

creating a new bank account
---------------------------

Creates a new bank account.
```

What you see above is us creating the section header that will render into a
http permalink, so links can directly point to the section of interest. This is
useful in particular to stuff like table of contents or navigation. Notice that
we have to specifically add the `cssclass` directive with the class name
`method-section`. This is so we can have pretty and standard styling. Again,
we're trying to match the HTML layout above.

```rst
  .. container:: method-description

    .. fields that are required or optional for the endpoint

```

Our left side, the actual input that we use to parse the request body when
posted to this endpoint.

```rst
  .. container:: method-examples

    .. dcode:: bank_account_create
```

This is where the magic happens, to render the right side of the documentation,
from here on out refered to as the example code snippet, we need to have three
things come back:

* Definition  - Usually a template string, e.g. `PUT https://.../v1/credits`
* Example Request - A fully executable example, that can be copied and pasted
into a shell for execution. It is important to note that the request **MUST**
demonstrate the corresponding fields on the left hand side of the documentation.
* Example Response - The response that comes back.

The `dcode` directive stands for **(d)**ynamic **(cod)**e
**(e)**executor. What happens here, is that a scenario, named
`bank_account_create`, which is located under the `scenarios`
directory, is executed and the results that are rendered return the
three things we mentioned above.

### Can you elaborate a bit more on how the `dcode` directive works?

The `dcode` directive is the `dcode.py` file that executes the
scenarios located in the `scenarios` directory.

#### The `dcode-default` directive

To avoid copy-pasting a lot of options, most dcode options are set to their
defaults in all the reference's `index.rst`. You may find a snippet that looks
like this:

```rst
.. dcode-default::
    :section-chars: ~
    :section-depth: 1
    :script: scripts/dcode-scenario -d scenarios
    :directive: code-block
    :nospec: True
```

This sets several `dcode` directives to sensible defaults so we can have
succinct options.

### What is cache.json?

`cache.json` is essentially Balanced's cached endpoint responses to allow
our documentation to reuse certain parameters to ensure parameters are
successful. It also allows us to lazily resolve endpoint dependencies.

For clarification, the example demonstrating retrieving a created
credit card requires that the scenario for creating a credit card is
executed before executing the example demonstrating retrieving a
created credit card.

Sounds simple, right? You're right! It is.

### How can I test the language code actually works correctly?

Here's the language scenarios currently supported:

* `php-scenario`
* `ruby-scenario`
* `python-scenario`

The `php-scenario` script actually executes the
`./scripts/dcode-scenario`, so executing the `bank_account_create`
scenario is similar to executing a snippet like this:

```bash
./scripts/dcode-scenario \
    -l debug  \
    --execute-lang php  \
    --disable-lang python  \
    --disable-lang ruby  \
    -d scenarios bank_account_create
```

#### PHP

```bash
./scripts/php-scenario bank_account_create
```

#### Ruby

```bash
./scripts/ruby-scenario bank_account_create
```

#### Python

```bash
./scripts/python-scenario bank_account_create
```

