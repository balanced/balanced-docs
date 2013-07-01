.. The entry point to the documentation, this is where all the table of
   content files are generated (and as a consequence displayed on the left
   hand side of our navigation menu)

.. dcode-default::
    :cache: dcode.cache

.. dcode-default:: scenario
    :script: scripts/lang-scenario.py -d scenarios -c scenario.cache
    :section-include: request
    :section-chars: ~^
    :lang: python ruby php node java

.. dcode-default:: form
    :script: scripts/rst.py form

.. the table of content tree is hidden here because we want to control its
   layout by using the global toctree function provided by sphinx to the
   Jinja2 templates. You can check this out in _templates/layout.html
.. toctree::
  :hidden:
  :maxdepth: 3

  introduction
  getting_started
  payouts