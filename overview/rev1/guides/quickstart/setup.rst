.. _quickstart-configure-client:

Configure your Balanced client
===============================

This section explains how to obtain, set up, and prepare to integrate a client
library into an application. All official Balanced client libraries are
open source and stored on Github.

.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-persianBlue20 references

  .. cssclass:: mini-header

    API Reference

  - `Authentication </1.1/api/authentication/#authenticating-to-balanced>`_

|

Topic overview
-----------------

By the end of this topic, you should understand how to do following:

- Obtain the client library of your choice
- Install necessary prerequisites
- Configure the library for use in your application


Prerequisites
---------------

.. container:: section-bash

  cURL


.. container:: section-ruby

  Ruby >= 1.8.7


.. container:: section-python

  Python 2.x


.. container:: section-java

  .. cssclass:: list-noindent

    - Java 6 or newer
    - gson 2.2.2
    - httpclient 4.2.1
    - commons-lang 3.1
    - commons-codec 1.7

  These can be downloaded to target/dependency after obtaining the library by
  using:

  .. code-block:: java

    $ mvn dependency:copy-dependencies


.. container:: section-csharp

  .NET Framework 4.5


.. container:: section-php

  .. cssclass:: list-noindent

    - PHP >= 5.3 with cURL
    - RESTful == 1.0.0
    - Httpful >= 0.1


.. container:: section-node

  .. cssclass:: list-noindent

    - node
    - npm


Obtaining the library
----------------------

.. container:: section-bash

  None


.. container:: section-ruby

  Add this line to your application's Gemfile:

  .. code-block:: ruby

    gem 'balanced'

  And then execute:

  .. code-block:: ruby

    $ bundle

  Or install it yourself via rubygems:

  .. code-block:: ruby

    gem install balanced


.. container:: section-python

  Add this line to your application's requirements:

  .. code-block:: python

    balanced>=1.0

  **NOTE: You may also define a more specific version if desired. For example, 1.0.1**

  And then execute:

  .. code-block:: python

    $ pip install -r [requirements_file]

  Or install it yourself via pip:

  .. code-block:: python

    pip install balanced


.. container:: section-java

  Add this line to your application's `pom.xml` (be sure to set the appropriate version):

  .. code-block:: java

    <dependency>
        <groupId>com.balancedpayments</groupId>
        <artifactId>balancedpayments</artifactId>
        <version>X.X.X</version>
    </dependency>

  Now apply your pom changes:

  .. code-block:: java

    $ mvn dependency:resolve

  Alternatively you may build the JAR yourself and add it as a project dependency.


.. container:: section-csharp

  Add the following dependencies to your project via NuGet package management:

  .. cssclass:: list-noindent

    - Json.NET
    - Balanced


.. container:: section-php

  Two options are available for including balanced-php:

  |

  .. container:: header2

    Composer

  Set up Composer:

  .. code-block:: php

    $ curl -s https://getcomposer.org/installer | php

  Require balanced in your ``composer.json``:

  .. code-block:: javascript

    {
        "require": {
            "balanced/balanced": "1.*"
        }
    }

  **NOTE: You may also define a more specific version if desired. For example, 1.0.1**

  Refresh your dependencies:

  .. code-block:: php

    $ php composer.phar update

  Require the autoloader and initialize:

  .. code-block:: php

    <?php
    require(__DIR__ . '/vendor/autoload.php');

    \Httpful\Bootstrap::init();
    \RESTful\Bootstrap::init();
    \Balanced\Bootstrap::init();
    ?>

  |

  .. container:: header2

    Source

  Download Httpful source:

  .. code-block:: php

    $ curl -s -L -o httpful.zip https://github.com/nategood/httpful/zipball/v0.2.3;
    $ unzip httpful.zip; mv nategood-httpful* httpful; rm httpful.zip

  Download RESTful source:

  .. code-block:: php

    $ curl -s -L -o restful.zip https://github.com/matthewfl/restful/zipball/master;
    $ unzip restful.zip; mv matthewfl-restful* restful; rm restful.zip

  Download the balanced-php source:

  .. code-block:: php

    $ curl -s -L -o balanced.zip https://github.com/balanced/balanced-php/zipball/master
    $ unzip balanced.zip; mv balanced-balanced-php-* balanced; rm balanced.zip

  Require all bootstrap files:

  .. code-block:: php

    <?php
    require(__DIR__ . "/httpful/bootstrap.php");
    require(__DIR__ . "/restful/bootstrap.php");
    require(__DIR__ . "/balanced/bootstrap.php");

    \Httpful\Bootstrap::init();
    \RESTful\Bootstrap::init();
    \Balanced\Bootstrap::init();
    ?>


.. container:: section-node

  .. code-block:: node

    npm install balanced-official


Configuring the Client
-----------------------

To communicate with the Balanced API, the Balanced client library needs to
be configured with your marketplace API key secret.

.. container:: section-bash

  There is no client library for curl. To "configure", just supply your
  API key secret as basic auth (-u) in the header of each request as follows:

  .. code-block:: bash

    curl https://api.balancedpayments.com/ \
         -H "Accept: application/vnd.api+json;revision=1.1" \
         -u ak-test-2aTAxvFwPKI8rhEpoVuRAXXnmgX1mLDm9:


.. container:: section-ruby

  If you're experimenting in an environment that doesn't
  autoload gems from your Gemfile such as IRB or PRY be sure to do:

  .. code-block:: ruby

    require 'balanced'

  Configure Balanced with your API key so requests are authenticated as your
  marketplace:

  .. code-block:: ruby

    Balanced.configure('ak-test-2IfBSMHWXU55xtQ13j9lvtK8IRjsb804g')


.. container:: section-python

  Import the Balanced library:

  .. code-block:: python

    import balanced

  Configure Balanced with your API key so requests are authenticated as your
  marketplace:

  .. code-block:: python

    balanced.configure("ak-test-1p1Tsac7gHeMQowL2seB7ieliuAJAufyq");


.. container:: section-java

  Configure Balanced with your API key so requests are authenticated as your
  marketplace:

  .. code-block:: java

    Balanced.configure("ak-test-1p1Tsac7gHeMQowL2seB7ieliuAJAufyq");


.. container:: section-csharp

  Use the Balanced namespace:

  .. code-block:: csharp

    using Balanced;

  Configure Balanced with your API key so requests are authenticated as your
  marketplace:

  .. code-block:: csharp

    Balanced.Balanced.configure('ak-test-2IfBSMHWXU55xtQ13j9lvtK8IRjsb804g')


.. container:: section-php

  Configure Balanced with your API key so requests are authenticated as your
  marketplace:

  .. code-block:: php

    <?php
    Balanced\Settings::$api_key = "ak-test-22IOkhevjZlmRP2do6CZixkkDshTiOjTV";
    ?>


.. container:: section-node

  Begin by requiring balanced:

  .. code-block:: node

    var balanced = require('balanced-official');


  Configure Balanced with your API key so requests are authenticated as your
  marketplace:

  .. code-block:: node

    balanced.configure('ak-test-1p1Tsac7gHeMQowL2seB7ieliuAJAufyq');


Checkpoint
-----------

You should understand how to do following:

.. cssclass:: list-noindent list-style-none

  - ✓ Obtain the client library of your choice
  - ✓ Install necessary prerequisites
  - ✓ Configure the library for use in your application

Ensure you have met these points before proceeding.


.. container:: box-right

 .. read-more-widget::
   :box-classes: box box-block box-blue right
   :icon-classes: icon icon-arrow

   :doc:`Charging Funding Instruments <charging-funding-instruments>`

|
