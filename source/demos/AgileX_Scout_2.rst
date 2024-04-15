

AgileX Scout 2 Demo
===================

To get started, plug the USB to CAN adaptor into the right hand USB port of the T14s laptop and the top CAN port on the Scout 2.

Then, power on the Scout 2 by pressing the power button on the front of the device.


Demo1: Control the Scout 2 using the Keyboard
----------------------------------------------

Power on the Scout 2. You can use :ref:`start_up_scout_2` to know how powering on the Scout 2.

Then in laptop open two terminals. In one terminal run the following command to bring up the CAN interface and bring up
AgileX Scout 2 ROS driver.

In the first terminal:

    .. code-block:: bash

        $ sudo ip link set can0 type can bitrate 500000
        $ source ~/agilex_ws/devel/setup.bash
        $ roslaunch scout_bringup scout_minimal.launch

.. note:: if “scout_minimal.launch” is not found, try this command instead:

    .. code-block:: bash

        $ roslaunch scout_bringup scout_robot_base.launch

In the second terminal, run the following command to control the Scout 2 using the keyboard:

        .. code-block:: bash

            $ source ~/agilex_ws/devel/setup.bash
            $ roslaunch scout_bringup scout_teleop_keyboard.launch

.. note::

    Please adjust the middle left switch (second from the left) on the remote control unit (i.e., the joypad) to
    the forward position. Ensure that the second terminal above is active by clicking on it. Then, utilize the keyboard
    keys (u, i, o, etc.) as specified in the terminal to operate the robot.



Demo2: Gazebo Simulation
------------------------

Power on the Scout 2. You can use :ref:`start_up_scout_2` to know how powering on the Scout 2.

Then in laptop open two terminals. In one terminal run the following command to bring up the CAN interface and bring up
AgileX Scout 2 ROS driver.

In the first terminal:

    .. code-block:: bash

        $ sudo ip link set can0 type can bitrate 500000
        $ source ~/agilex_ws/devel/setup.bash
        $ roslaunch scout_bringup scout_minimal.launch

.. note:: if “scout_minimal.launch” is not found, try this command instead:

    .. code-block:: bash

        $ roslaunch scout_bringup scout_robot_base.launch

In the second terminal, run the following command to bring up the Gazebo simulation:

    .. code-block:: bash

        $ source ~/agilex_ws/devel/setup.bash
        $ roslaunch scout_bringup scout_base_gazebo_sim.launch

.. note:: If you notice that the robot remains stationary and there is a buzzing sound emanating from the rear of
    the :ref:`AgileX Scout 2` while operating the joypad, please verify if any of the Emergency buttons are engaged.
    If so, disengage these buttons and attempt to teleoperate the robot once more.