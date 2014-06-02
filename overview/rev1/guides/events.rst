Events
=============

There are times where operations are not immediate, or sometimes you'd like your systems
to be notified of activity in Balanced. For these cases, Balanced provides Events. This
guide will describe the Callback and Events resources and give a detailed walkthrough of
their usage and best practices.


.. admonition:: References
  :header_class: alert alert-tab full-width alert-tab-persianBlue60
  :body_class: alert alert-persianBlue20

  .. cssclass:: mini-header

    API Specification

  .. cssclass:: list-noindent

    - `Callbacks Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/callbacks.json>`_
    - `Callback Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/callback.json>`_
    - `Events Collection <https://github.com/balanced/balanced-api/blob/master/fixtures/events.json>`_
    - `Event Resource <https://github.com/balanced/balanced-api/blob/master/fixtures/_models/event.json>`_

  .. cssclass:: mini-header
  
    API Reference

  .. cssclass:: list-noindent

    - `Create a Callback </1.1/api/callbacks/#create-a-callback>`_
    - `Event Types </1.1/api/events/>`_
  
  .. cssclass:: mini-header

    Code Libraries

  .. cssclass:: list-noindent

    - `balanced-spectator <https://github.com/remear/balanced-spectator>`_
    - `Cloverleaf <https://github.com/remear/cloverleaf>`_


Callbacks
-------------

Callbacks are a means of registering to receive payloads of information
to a specific URL of your choice. Each marketplace may have only one callback.

To begin receiving events, we first need to create a Callback and specify the ``url``
where we'll be listening. Optionally, we can also specify the ``method`` by which
we'd like to receive event payloads, one of: ``GET``, ``POST`` (default), or ``PUT``.

.. literalinclude:: examples/curl/callback-create.sh
   :language: bash

.. literalinclude:: examples/python/callback-create.py
   :language: python

.. literalinclude:: examples/ruby/callback-create.rb
   :language: ruby

.. literalinclude:: examples/php/callback-create.php
   :language: php

.. literalinclude:: examples/java/callback-create.java
   :language: java

.. literalinclude:: examples/node/callback-create.js
   :language: node


Now that we have a ``Callback``, we'll start receiving event payloads from Balanced
for activity in the marketplace.


Events
-------------

An ``Event`` resource represents Balanced systemic events to which applications may
subscribe via a ``Callback``. In the event that a 20x response is not received when
the payload is sent to the callback URL, the callback will be retried up to 10 times
with an initial retry delay of 10 minutes which will increase exponentially with each
failure for the next 7 days.

.. note::
  :header_class: alert alert-tab
  :body_class: alert alert-green

  Events from Balanced will originate from the IP addresses: ``50.18.199.26``, ``50.18.204.103``

  While these IPs have remained the same for a long time and are not expected to change,
  any changes will be reflected here.

An ``Event`` payload consists of an Events collection with an entity collection
containing the GET response of the object after actions have been applied.

This is an example event payload for creating a ``Debit`` (``debit.created``):

.. code-block:: javascript

  {
    "events": [
      {
        "links": {},
        "occurred_at": "2014-05-28T20:40:59.693000Z",
        "uri": "/events/EV602b7d14e6a811e3a95a061e5f402045",
        "entity": {
          "debits": [
            {
              "status": "succeeded",
              "transaction_number": "W556-608-3086",
              "description": "Some descriptive text for the debit in the dashboard",
              "links": {
                "customer": null,
                "source": "CC2HR1joTg9o19Qe5K3IhB6V",
                "order": null,
                "dispute": null
              },
              "created_at": "2014-05-28T20:40:59.120716Z",
              "updated_at": "2014-05-28T20:40:59.693844Z",
              "failure_reason": null,
              "currency": "USD",
              "amount": 5000,
              "href": "/debits/WD2VbQlTst3jmFTgRnZmhi29",
              "meta": {},
              "failure_reason_code": null,
              "appears_on_statement_as": "BAL*Statement text",
              "id": "WD2VbQlTst3jmFTgRnZmhi29"
            }
          ],
          "links": {
            "debits.customer": "/customers/{debits.customer}",
            "debits.dispute": "/disputes/{debits.dispute}",
            "debits.source": "/resources/{debits.source}",
            "debits.order": "/orders/{debits.order}",
            "debits.refunds": "/debits/{debits.id}/refunds",
            "debits.events": "/debits/{debits.id}/events"
          }
        },
        "href": "/events/EV602b7d14e6a811e3a95a061e5f402045",
        "type": "debit.created",
        "id": "EV602b7d14e6a811e3a95a061e5f402045"
      }
    ],
    "links": {}
  }


To simplify event handling in your systems, Balanced recommends using balanced-spectator,
a Ruby Rack middleware. See the balanced-spectator section for more information.


balanced-spectator
-------------------------

balanced-spectator is a Rack middleware to enqueue Balanced events to RabbitMQ. It
rejects requests from IPs that do not match the ``balanced/hooker/[version]`` user-agent
and Balanced event server IPs or authorized IPs. Requests that pass this criteria are processed
and the payload is sent to a durable queue, ``balanced_event_incoming`` by default. In this
section we'll describe how to set up balanced-spectator as a stand-alone application so it
processes event requests separate from your application.

**balanced-spectator requires Balanced API v1.1**


Begin by creating a ``Gemfile`` containing:

.. code-block:: ruby-nohide

  gem 'balanced-spectator', github: 'remear/balanced-spectator'


Next, create ``config.ru`` containing:

.. code-block:: ruby-nohide

  require 'bundler/setup'
  Bundler.require(:default)

  run Balanced::Spectator::Base.new

|

Available options:

.. cssclass:: dl-horizontal dl-params dl-param-values dd-noindent dd-marginbottom

  ``authorized_ips``
    Array of strings of allowed request IPs. This is added to ``127.0.0.1`` and the current Balanced IPs.
  ``ignored_event_types``
    Array of strings of Balanced Event types to ignore and not pass to RabbitMQ.
  ``rabbitmq_queue_name``
    Name of the RabbitMQ queue to use. Defaults to ``balanced_event_incoming``.


Example usage:

.. code-block:: ruby-nohide

  run Balanced::Spectator::Base.new(
    authorized_ips: ['xxx.xxx.xxx.xxx', 'xxx.xxx.xxx.xxx'],
    ignored_event_types: ['debit.succeeded', 'debit.failed', 'credit.succeeded'],
    rabbitmq_queue_name: 'balanced_event_incoming'
  )


While there are several ways to run a Rack application, a common way is to use Puma.
Be sure to add puma to your Gemfile, bundle, then run:

.. code-block:: html

  puma config.ru -p 9293


To daemonize:

.. code-block:: html

  puma -d config.ru -p 9293


Since applications that use Balanced vastly differ, the method of processing events
out of the RabbitMQ queue are left up to your discretion. We've created
`Cloverleaf <https://github.com/remear/cloverleaf>`_ as a simple,
extensible example. See the cloverleaf section for more information.


.. _cloverleaf:

Cloverleaf
-----------------

Cloverleaf is a simple, extensible example that demonstrates the basics of processing
Balanced events out of a RabbitMQ queue. It is intended to work in conjunction with
balanced-spectator.

**Cloverleaf requires Balanced API v1.1**

Clone the project:

.. code-block:: html

  git clone https://github.com/remear/cloverleaf.git


For each event type you wish to process, add a method in the ``EventHandler`` class.

.. code-block:: ruby-nohide

  require 'bunny'
  require 'json'

  class EventHandler
    # define a method for each event type you wish to process. return true/false

    def self.debit_failed(payload)
      true
    end

    def self.credit_succeeded(payload)
      true
    end

    def self.credit_failed(payload)
      true
    end

    # catch undefined event type methods and log a warning
    def self.method_missing(method, *args, &block)
      $stderr.puts "WARNING: #{method} handler method is not defined"
    end
  end


While there are several ways to run a Rack application, a common way is to use Puma.

.. code-block:: html

  puma config.ru -p 9294


To daemonize:

.. code-block:: html

  puma -d config.ru -p 9294


Security
~~~~~~~~~~~

Many applications that use Balanced become internally driven by Events. This highlights
a security concern. What if a malicious user sent a manually constructed payload to your
event handling application. Potentially this could be very problematic as a malicious event
payload could be sent to the application, and affect system integrity and stability.

Requests from Balanced will:

- \- Originate from the IP addresses: ``50.18.199.26``, ``50.18.204.103``
- \- Have an user agent of ``balanced/hooker/[version]`` (note: user-agent strings can be manually set and are not secure)
- \- Conform to the `Events collection specification`_ and the `Event resource specification`_

balanced-spectator checks the originating IP against the Balanced IPs and any additionally
configured allowed IPs. It also verifies the user-agent string. If you're manually
implementing an event listener application, be sure it at least performs these checks.

As an added safety precaution to ensure event validity, you may also manually fetch the
changed entity resource and compare it with records in your system before processing any
changes.





.. _Events collection specification: https://github.com/balanced/balanced-api/blob/master/fixtures/events.json
.. _Event resource specification: https://github.com/balanced/balanced-api/blob/master/fixtures/_models/event.json