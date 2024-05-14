

.. _jackal_startup:

==============
Jackal Startup
==============

.. warning:: Jackal is a fast moving robotic platform. Please read the following notices carefully.

Before starting the :ref:`ClearPath Jackal` robot, read the documentation provided by ClearPath Robotics. The documentation provides important information about the robot's safety, operation, and maintenance. The documentation also provides information about the robot's hardware and software components.
Also we need to be familiar with the robot's Human-Machine Interface (HMI).
The HMI is shown in the :numref:`jackal_hmi` figure.

.. _jackal_hmi:

.. figure:: ../../../images/clearpath_jackal/jackal_hmi.png
   :align: center
   :scale: 70%
   :alt: ClearPath Jackal HMI

   ClearPath Jackal HMI

The HMI has the following components from left to right:

    #. **Motion Stop button**: LED is solid green when Jackal is able to drive and flashing green when the Jackal's motors are disengaged; pressing button toggles the motors between engaged and disengaged mode.
    #. **Comms indictor**: LED is solid green when communication between the MCU and computer has been established and LED is off otherwise.
    #. **Wi-Fi indicator**: LED is solid green when Wi-Fi is connected and LED is off otherwise.
    #. **Battery indicator**: LED is solid green when the battery level is ok, solid yellow when the battery level is getting low (should be charged soon), and solid red when the battery level is critical (should be charged immediately).
    #. **System Power button**: LED is solid blue when the system is powered on and running and the LED is flashing blue during the shutdown process; when the system is powered off, pressing the power button begins the power on process; when the system is powered on, a quick press of the power button begins a graceful shutdown and a prolonged press of the power button triggers and immediate power off of the system.


