.. _AgileX Scout GitHub: https://github.com/agilexrobotics/scout_ros

.. _Scout 2 ROS:

ROS
===

This section will cover the setup of ROS for the :ref:`AgileX Scout 2` robot.

.. note:: Use the CAN to USB adaptor cable, the CAN plug can be plugged into either the top or rear of the :ref:`AgileX Scout 2` robot.

Follow the instructions on the `AgileX Scout GitHub`_ for setup of the ROS environment.

.. note:: make sure to use `$ catkin_make`. Do not use `$ catkin build` as the latter will not work.;

if during `$ catkin_make` you get an error Could not find the required component `tf2`, try:

.. code-block:: bash

    $ sudo apt install ros-noetic-tf2

most likely you have the base distribution of the ROS install, not the full.

.. note:: The ROS environment is already set up on the NNUF laptop 1, T14s
