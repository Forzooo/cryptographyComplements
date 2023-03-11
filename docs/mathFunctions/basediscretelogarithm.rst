Base Discrete Logarithm
=======================

This function calculates the discrete logarithm from a given base, congruence, and modulo.

.. warning::
    The function won't stop even if there isn't a number that can resolve the discrete logarithm.

.. code-block:: python

   def baseDiscreteLogarithm(base: int, congruence: int, modulo: int):
       """
       Calculate, from given base, congruence and modulo, the discrete logarithm.
       Warning: The function won't stop even if there isn't a number that can resolve the discrete logarithm.
       """
       if not isNumber(base, congruence, modulo):
           return None
       
       BASE, CONGRUENCE, MODULO = int(base), int(congruence), int(modulo)
       power = 0

       while True:
           number = base**power
           if number % MODULO == CONGRUENCE % MODULO:
               print(f"log{BASE} {power} \u2261 {CONGRUENCE} (mod {MODULO})")
               logarithm = [BASE, power, CONGRUENCE, MODULO]
               # return BASE, power, CONGRUENCE, MODULO
               return logarithm

           power += 1

Note: ``isNumber`` function checks if the input entered is a number.
``isNumber`` can be found in Tools functions section.