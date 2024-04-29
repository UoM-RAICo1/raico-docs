


==========================
Manipulation with ROS
==========================

This section describes how to manipulate :ref:`Kinova Gen3` with `ROS`.

.. note:: You can find the installed `ROS` packages in the NNUFhr laptop.

.. note:: If you want ti install the `ROS` packages, you can find the `ROS` and `ROS2` GitHub links for Kinova Gen3 in the :ref:`Kinova Gen3` page.


Gazebo Simulation
-----------------

To launch the Gazebo simulation, you can use the following command:

    .. code-block::

        $ source kinova_ws/devel/setup.bash
        $ roslaunch kortex_gazebo spawn_kortex_robot.launch

In RViz, you can visualize the robot by doing the following:
    - Change the Fixed Frame from `map` to `base_link`.
    - Add the robot model by clicking on `Add` and selecting `RobotModel`.
    - Add the `MoveIt!` plugin by clicking on `Add` and selecting `MotionPlanning`.

Now you can visualize the robot in RViz and Gazebo. You can also control the robot using the `MoveIt!` plugin.


.. _ros_example:

Full Control
------------

To full control the robot by `ROS` you can use the following command:

    .. code-block::

        $ source kinova_ws/devel/setup.bash
        $ roslaunch kortex_examples full_arm_movement_python.launch

or

    .. code-block::

        $ source kinova_ws/devel/setup.bash
        $ roslaunch kortex_examples moveit_example.launch

