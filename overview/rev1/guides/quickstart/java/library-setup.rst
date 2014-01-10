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