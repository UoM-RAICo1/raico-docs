

========================
Kortex API [Without ROS]
========================

This is a simple API to communicate with the :ref:`Kinova Gen3` robot arm without using ROS via ``Python``.

Python Example
--------------------------

Follow the steps below to run the example:

1. Connect to the robot arm via the Ethernet cable [See :ref:`Kinova_Gen3_pc_connection`]
2. Run the command below to in the terminal:

.. code-block::

    $ cd ~/kinova_ws/koortex/api_python/examples

Select the example you want to run e.g. ``102-Movement_high_level``

.. code-block::

    $ cd 102-Movement_high_level
    $ python3 01-move_angular_and_cartesian.py

