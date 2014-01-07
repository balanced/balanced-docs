Using balanced.js
==================

Using ``balanced.js`` is essential in ensuring that you're PCI compliant.
When using balanced.js, sensitive data never touches your servers. As a result,
the burden of PCI compliance shifts to Balanced,
which is `PCI-DSS Level 1 Compliant`_.

.. note::
   :header_class: alert alert-tab
   :body_class: alert alert-gray

   Throughout this guide we'll be referencing this `jsFiddle example`_.
   For the sake of brevity, we'll also use `jQuery`_, but note that balanced.js
   itself doesn't rely on any Javascript framework.


.. _balanced-js.include:

Including balanced.js
-----------------------

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-gray

  This may not work on very old browsers. For more information on how to
  support older browsers, `quirksmode`_ provides a tutorial on how to get
  javascript ``<script>`` includes to play nicely.

.. code-block:: html

  <script type="text/javascript" src="https://js.balancedpayments.com/1.1/balanced.js"></script>


.. _balanced-js.initialize:

Initialize balanced.js
--------------------------

balanced.js needs to be initialized with the address of the Balanced API server
to which it should connect, as well as the revision of the API to use, in this
case, https://api.balancedpayments.com, and revision 1.1.

.. code-block:: javascript

  <script type="text/javascript">
    $(document).ready(function () {
      balanced.init({
        server: 'https://api.balancedpayments.com',
        revision: 1.1
      });
    });
  </script>


.. _balanced-js.collecting-card-info:

Collecting credit card information
----------------------------------

Before we can collect credit card information, we need a place where users can
ender it in, a form. The example below is extracted this `jsFiddle example`_.


.. code-block:: html

  <form role="form" class="form-horizontal">
    <div>
      <label>Card Number</label>
      <input type="text" id="cc-number" autocomplete="off" placeholder="4111111111111111" maxlength="16" />
    </div>
    <div>
      <label>Expiration</label>
      <input type="text" id="cc-ex-month" autocomplete="off" placeholder="01" maxlength="2" />
      <input type="text" id="cc-ex-year" autocomplete="off" placeholder="2013" maxlength="4" />
    </div>
    <div>
      <label>Security Code (CVV)</label>
      <input type="text" id="ex-csc" autocomplete="off" placeholder="453" maxlength="4" />
    </div>
    <a id="cc-submit">Tokenize</a>
  </form>


Now let's define our `callback`_, the block of code we want to execute after
having received a response for our tokenization request to the Balanced API.

.. code-block:: javascript

  function handleResponse(response) {
    if (response.status === 201 && response.href) {
      // Successful tokenization
      // Call your backend
      jQuery.post("/path/to/your/backend", {
        uri: response.href
      }, function(r) {
        // Check your backend response
        if (r.status === 201) {
          // Your successful logic here from backend ruby
        } else {
          // Your failure logic here from backend ruby
        }
      });
    } else {
      // Failed to tokenize, your error logic here
    }
  }


Now register a click event for the submit button. This is where we will place
our form field values into a payload object and submit it to the Balanced API.

.. code-block:: javascript

  $('#cc-submit').click(function (e) {
    e.preventDefault();

    var payload = {
      number: $('#cc-number').val(),
      expiration_month: $('#cc-ex-month').val(),
      expiration_year: $('#cc-ex-year').val(),
      security_code: $('#ex-csc').val()
    };

    // Tokenize credit card
    balanced.card.create(payload, handleResponse);
  });




.. _jsFiddle example: http://jsfiddle.net/amcf6/1/
.. _jsFiddle [tokenize credit cards]: http://jsfiddle.net/amcf6/1/
.. _PCI-DSS Level 1 Compliant: http://www.visa.com/splisting/searchGrsp.do?companyNameCriteria=Pound%20Payments
.. _quirksmode: http://www.quirksmode.org/js/placejs.html
.. _jQuery: http://www.jquery.com
.. _callback: https://en.wikipedia.org/wiki/Callback_(computer_programming)