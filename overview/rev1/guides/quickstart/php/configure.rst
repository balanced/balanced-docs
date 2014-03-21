If you're experimenting in an environment that doesn't
autoload gems from your Gemfile such as IRB or PRY be sure to do:

.. code-block:: ruby

  require 'balanced'

Configure Balanced with your API key so requests are authenticated as your
marketplace:

.. code-block:: ruby

  Balanced.configure('ak-test-2IfBSMHWXU55xtQ13j9lvtK8IRjsb804g')