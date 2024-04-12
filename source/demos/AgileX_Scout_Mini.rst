
.. _Teleop Twist Joy: https://github.com/ros-teleop/teleop_twist_joy

.. _AgileX_Scout_mini_Demo:

AgileX Scout Mini
=================

To get started, connect both the Nvidia Xavier and a remote laptop to the same wifi router that has a strong stable
signal, e.g. RAICo. Avoid using the mini-router because the signal is very weak.

Demo1 - Teleportation using Joystick
-------------------------------------

This demo will show how to control the robot using a joystick.

Do the following steps on the **Connected Laptop**:

First, install teleop_twist_joy


    .. code-block::

        $ sudo apt-get install ros-<distro-name>-teleop-twist-joy


You can use `Teleop Twist Joy`_ link to install from the source.

Make sure an appropriate configuration file exists for DS4:

    .. code-block::

        $ cd /opt/ros/noetic/share/teleop_twist_joy/config/
        $ sudo cp ps3.config.yaml ps4.config.yaml
        $ sudo vi ps4.config.yaml

make sure it all looks like this (the last 2 lines change content):


    .. code-block::

        axis_linear: 1
        scale_linear: 0.7
        scale_linear_turbo: 1.5

        axis_angular: 0
        scale_angular: 0.4

        enable_button: 6        # L2 shoulder button
        enable_turbo_button: 4  # L1 shoulder button


.. note:: Make sure ROS_IP and ROS_MASTER_URI are set correctly on `~/.bashrc`.

.. todo:: Add a section on how to set ROS_IP and ROS_MASTER_URI

Then launch

        .. code-block::

            $ roslaunch teleop_twist_joy teleop.launch joy_dev:=/dev/input/js1 joy_config:=ps4 scale_linear:=.1 (scale_angular:=1)

.. note:: To operate the robot, you will need to press and hold L1 button, while simultaneously moving the left joystick forward-backwards and/or left-right.


Now, do the following steps on the **Scout Mini**:

check the content of ROS_IP and ROS_MASTER_URI in .bashrc, then open a terminal:

    .. code-block::

        $ sudo ip link set can0 up type can bitrate 500000
        $ roslaunch scout_bringup scout_mini_robot_base.launch

Now, you should be able to control the robot using the joystick.


Demo2 - Teleportation using Keyboard
-------------------------------------

This demo will show how to control the robot using a keyboard.

Do the following steps on the **Scout Mini**:

Comment the content of ROS_IP and ROS_MASTER_URI in .bashrc, then open a terminal1:

    .. code-block::

        $ sudo ip link set can0 up type can bitrate 500000
        $ roslaunch scout_bringup scout_mini_robot_base.launch

Open a new terminal:

    .. code-block::

        $ roslaunch scout_bringup scout_mini_teleop_keyboard.launch

Now, you should be able to control the robot using the keyboard.