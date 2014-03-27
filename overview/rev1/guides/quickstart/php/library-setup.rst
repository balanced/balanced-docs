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
  require(__DIR__ . "/httpful/bootstrap.php")
  require(__DIR__ . "/restful/bootstrap.php")
  require(__DIR__ . "/balanced/bootstrap.php")

  \Httpful\Bootstrap::init();
  \RESTful\Bootstrap::init();
  \Balanced\Bootstrap::init();
  ?>