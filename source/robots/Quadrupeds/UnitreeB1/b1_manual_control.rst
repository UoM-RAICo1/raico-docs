
.. _b1_manual_control:

==============
Manual Control
==============

To control the :ref:`Unitree_B1` robot manually, first of all you ned to turn the robot and remote control on. To know how to turn the robot and remote control on, please refer to the :ref:`b1_StartUp` section.

The B1 robot can be controlled in the following ways:

1) After powering on, the robot directly enters the ordinary walking mode, at this time you can push the joystick to control the robot forward and backward, shift side to side, in-place turning, etc. if you do not push the joystick, it will stop moving.
2) When the walking mode is stationary, press :guilabel:`SELECT -> to enter a static standing state`, at which point you can control the position through the joystick.
3) In static standing state, press :guilabel:`START -> into walking mode`.
4) In ordinary walking state, press :guilabel:`L2+START -> to switch obstacle mode`. At this point, the joystick can be pushed to control the robot to walk over obstacles and climb stairs, and if the joystick is not pushed, it will stop moving. Crossing the obstacle walking mode by pressing :guilabel:`L2+START can switch back to the normal walking mode`.
5) In any state, press :guilabel:`L2+A-> to lock the robot` and press :guilabel:`START to unlock the robot`.
6) After the robot locks, press :guilabel:`L2+A The robot is in a lying state`. :guilabel:`press L2+A 2 times, and the robot completes locking - lying down`
7) Press :guilabel:`L2+A to stand up in the lying state`, currently the robot is in a locked state, press :guilabel:`START to unlock the robot`. (That is, press :guilabel:`L2+A 3 times, and the robot completes the locking-lying down-standing in turn`.
8) In any state, :guilabel:`L2+B-> damping state/low-power state`, in which the robot will lie down and need to press :guilabel:`L2+A to make him stand up`.
9) :guilabel:`L1+L2: Lock the B1 remote control`, in which case the remote control will not be able to control B1. :guilabel:`Press L1+L2 to control B1 again`. This button requires B1 to be used with the Z1 robotic arm, and the remote control can be switched to the control robotic arm.

Remote Control Commands
-----------------------

+----------------------------------------+-----------------------------------------+
|               Key                      |                Effect                   |
+---------------+------------------------+-----------------------------------------+
| Left Rocker   | Push Forward/Backward  | Move back and forth/prone Position      |
|               +------------------------+-----------------------------------------+
|               | Push Left/Right        | Sideways Movement/Twist                 |
+---------------+------------------------+-----------------------------------------+
| Right Rocker  | Push Forward/Backward  | Head Up or Down/Pitch                   |
|               +------------------------+-----------------------------------------+
|               | Push Left/Right        | Left or Right Turn/Shake Head           |
+---------------+------------------------+-----------------------------------------+