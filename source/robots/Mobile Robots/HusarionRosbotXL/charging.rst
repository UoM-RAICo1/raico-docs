

.. _Charging:

========
Charging
========

.. warning:: Ensure that the robot is turned off before charging.

.. warning:: Connect the cable of the charger to the robot before connecting the charger to the power source.

.. note:: For more information about the charging process, see the Husarion Rosbot XL Documentation at :ref:`Husarion Rosbot XL`.

The ROSbot XL includes an on-board battery charger.
The charging process begins automatically when the power adapter is connected and stops when the battery is fully charged.
A ``Low bat`` LED on the rear panel indicates a low battery level.

We strongly recommend using the power adapter provided with the robot.
However, it is also possible to use any adapter compatible with Power Delivery (PD2.0/PD3.0) that provides a 15V or 20V output with a minimum current of 3A (the current draw is internally limited to 2.8A).

The robot has four possible modes of operation:

    - Active, battery only.
    - Active, battery + power adapter. In this mode, the robot can be used and charged simultaneously. The battery is used only if the robot's current consumption exceeds the power adapter's maximum current.
    - Inactive (powered off), battery only. In this state, the robot does not draw current from the battery and can remain in this state for weeks. The battery should be checked every 6-8 weeks and recharged if the level is below 25%. For prolonged storage, the optimal battery level is 40-50%.
    - Inactive, battery + power adapter. In this state, the battery charges at maximum speed (2.5A maximum). The robot can be switched on at any time, transitioning to mode "b".

.. note:: The battery charging process in mode ``d`` should take approximately 5-6 hours to charge from 0% to 100%.


