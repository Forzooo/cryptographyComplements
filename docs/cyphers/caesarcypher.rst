Caesar Cypher
=============

This cypher uses the Caesar Cypher encryption. The number for the sequence is randomly selected, but if you prefer you can set it to 3 to match with the real Caesar one.

.. code-block:: python

    def CaesarCypher():
        "This functions generate the Caesar Cypher with a random sequence, or if enabled by the user in the script, the original one."
        import string, random
        elements = string.ascii_letters + string.digits + string.punctuation + "àèéìòù" + " "
        cypher = {elements[i]: None for i in range(len(elements))}

        # sequence = 3 # use this for the original Caesar Cypher
        sequence = random.randint(0, len(cypher)) # use this for a random Caesar Cypher

        modulo = int(len(cypher))
        for i in cypher.keys():
            index = sequence % modulo
            cypher[i] = elements[index]
            sequence += 1

        writeCypher(cypher)
        return cypher

Note: The generated cypher is written in a .txt file in the same folder where your Python script is located.
