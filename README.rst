hms_logger, the logging microservice
####################################

This service simply log all messages passed to the RabbitMQ broker to a local
MongoDB collection, for monitoring and debugging purposes.

Requirements
------------

You need to have a working MongoDB server on the host that you are going to run
the program on.

Using
-----

Create a Python 3 virtualenv and install software::

    $ virtualenv -ppython3 venv
    $ source venv/bin/activate
    (venv) $ pip install .

Then start the bot inside the virtual env::

    (venv) $ hms_logger

License
-------

This project is brought to you under MIT license. For further information,
please read the provided ``LICENSE.txt`` file.