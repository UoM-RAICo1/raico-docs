

.. _z1_ros:

=============
SDK Operation
=============

ROS Simulation
--------------

1. Set ros workspace


If the user is not familiar with the path setting,
please create the folder named ``unitree_ws/src`` and move folder ``unitree_ros`` folder in it,
which should be ``~/unitree_ws/src/unitree_ros``.
Then download the folder `unitree_legged_msgs`, move it to ``~/unitree_ws/src/``.

You can also use the following commands to set the ros workspace.

.. code-block::

    mkdir -p ~/unitree_ws/src
    mv unitree_ros ~/unitree_ws/src/
    mv unitree_legged_msgs ~/unitree_ws/src/

Then set the ros workspace like this:

.. code-block::

    cd ~/unitree_ws
    catkin_make
    echo "source ~/unitree_ros/devel/setup.bash">>~/.bashrc
    source ~/.bashrc

Now, run roslaunch ``unitree_gazebo z1.launch``, if successfully configured, the simulation interface of Gazebo will be displayed.

.. code-block::

    roslaunch unitree_gazebo z1.launch

.. note::
    After entering `RosLaunch Z`, press tap to check whether the terminal will automatically complete.
    If rosLaunch is successfully programmed, that means the path setting is successful.


2. CMakeLists Configuration


Open the ``CMakeLists.txt`` in the z1_controller folder and change the compilation conditions as follows.

.. code-block::

    # set(COMMUNICATION UDP)             #UDP
    set(COMMUNICATION ROS)               #ROS


3. Compile

Now, compile the project.

.. code-block::

    mkdir build
    cd build
    cmake ..
    make

Execute the executable file ``./z1_ctrl`` in folder build. The default control mode is SDK,
if you need to use keyboard control, use ``./z1_ctrl k``
When executing this command, the terminal will continuously print statements, such as
:guilabel:`[WARNING] UDPPort::recv, unblock version, wait time out`,
this is normal because we have not started the robotic arm SDK to communicate with the robotic arm controller.

.. note::
    Various information will be printed in this window, please observe the content of this window.

4. Open folder z1_SDK and create folder build in it (open the third terminal).

.. code-block::

    mkdir build
    cd build
    cmake ..
    make

Execute the executable file in folder build.
There are two executable files generated, ``example_lowcmd_send`` and ``bigdemo``.
This time we run ``bigdemo``.

.. code-block::

    ./bigdemo_basic

.. note::

    Keyboard Operation:The specific keys will be introduced in state machine section.

First press ``2`` on the keyboard and then press key ``0``,
the robotic arm will enter the label operation state machine.
Input forward at the prompt, then click enter, the robotic arm will run forward.
Press ``~`` again, return to the origin.
After returning to the origin, it will automatically enter the joint control mode.
At this time, the rotation of the robotic arm can be controlled by long press according to the following keys.

+------------+----------+--------------------+
| Joint ID   | Keyboard | Joint Action       |
|            |          | (right hand)       |
+============+==========+====================+
| 0          | Q/A      | positive/negative  |
+------------+----------+--------------------+
| 1          | W/S      | positive/negative  |
+------------+----------+--------------------+
| 2          | D/E      | positive/negative  |
+------------+----------+--------------------+
| 3          | R/F      | positive/negative  |
+------------+----------+--------------------+
| 4          | T/G      | positive/negative  |
+------------+----------+--------------------+
| 5          | Y/H      | positive/negative  |
+------------+----------+--------------------+
| Gripper    | up/down  | positive/negative  |
+------------+----------+--------------------+

Now, we have completed the simulation operation.

The whole process is: :guilabel:`Run ROS–>Run z1_ctrl–>Run` SDK instance.


Multiple robots control
-----------------------

1. open the directory z1_controller, set :guilabel:`Communication in CMakeLists.txt to UDP`.
2. copy the directory z1_controller, named as z1_controller_111.
3. open the directory z1_controller_111.

In main.cpp:

    set UDP port (Line51) as shown in the following example:

    .. code-block::

        ctrlComp->cmdPanel = new ARMSDK(events, emptyAction, "127.0.0.1", 8074, 8073, 0.002);

In config.xml:

    set IP to ``192.168.123.111``, set Port to ``8882``.

In unitreeArmTools.py

    set the second robotic arm IP to ``192.168.123.111``.

As described previously, proceed as follows:

    execute z1_ctrl in z1_controller at the first terminal, which communicates with the robotic arm 110.
    execute z1_ctrl in z1_contrller_111 at the second terminal, which communicates with the robotic arm 111.
    execute lowcmd_multirobots in z1_sdk at the third terminal.

And then we can see that the Joint1 of both robotic arm has turned at an angle.





