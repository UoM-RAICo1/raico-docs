

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

    #. **Motion Stop button**: The LED displays a solid green when the Jackal is operational and shifts to flashing green when the motors are disengaged. Pressing the button toggles the motor function between engaged and disengaged.
    #. **Comms indictor**: The LED remains solid green to indicate a successful connection between the MCU and the computer. It is unlit when no communication is established.
    #. **Wi-Fi indicator**: A solid green LED signifies an active Wi-Fi connection. The LED is unlit when the connection is absent.
    #. **Battery indicator**: The LED shows solid green when the battery is adequately charged, transitions to solid yellow indicating a low charge that requires imminent recharging, and turns solid red to signal a critical battery level necessitating immediate charging.
    #. **System Power button**: The LED is solid blue when the system is powered on and operational. It flashes blue during the shutdown process. Pressing the power button when the system is off initiates the power-on sequence. A quick press while the system is on starts a graceful shutdown, whereas a prolonged press forces an immediate system power-off.


Powering on
-----------

Activate the system by pressing the ``power button`` located on the Jackal's HMI panel.
Observe the LEDs as they display a test pattern.
Following this, allow approximately 30 seconds for the internal computer to complete its booting process.
Once the booting is complete, the Comms indicator will illuminate green,
signifying that ROS has been successfully initiated on the computer and communication with the Jackal base has been established.


Safety Precautions
------------------

The ``Motion Stop button`` is situated on the HMI Panel at the rear of the Jackal unit.
To activate Stop Mode, depress the Motion Stop button once; observe the flashing green LED adjacent to the Motion Stop button,
along with the flashing red LEDs at all four corners.
To deactivate Stop Mode, press the Motion Stop button once more; all LEDs should revert to their standard settings.



Powering Off
------------

Upon completing your tasks with the Jackal, please press and release the ``power button`` to turn off the device.



