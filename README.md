# Robot Gazebo Simulation
Upgrade URDF in previous assignment to introduce the robot model to Gazebo simulation. 

## Instructions: 
1. (10%) Set up the package.
```bash
cd <your ros workspace>/src
git clone git@github.com:UCAEngineeringPhysics/a3-robot_simulation-<your github username>.git
cd ..
colcon build --packages-select diffbot_gazebo
```
2. (10%) Create your robot's model by modifying the description file: `diffbot_gazebo/urdf/diffbot.urdf.xacro`. You can start from the URDF that were created in the previous assignment.
3. (30%) Include physical properties (`<collision>` and `<inertial>`) for all the links. 
4. (20%) Use `<gazebo reference>` tag to mark the links that need additional properties in Gazebo. **Make sure the caster wheels are correctly configured.**
5. (30%) Add [`gazebo_diff_drive`](https://github.com/ros-simulation/gazebo_ros_pkgs/wiki/ROS-2-Migration:-Diff-drive) plugin to your URDF, so that your robot can be controlled by **`/cmd_vel`** topic (using `geometry_msgs/Twist` messages) in Gazebo.

#### Hints:
- Example repository: [linzhanguca/homeplater](https://github.com/linzhangUCA/homeplater.git).
- Remember to build your package in `<your ros workspace>` and `source ~/<your ros workspace>/install/local_setup.bash` after the first time you build the package.
- To drive the robot in Gazebo, you can `ros2 run teleop_twist_keyboard teleop_twist_keyboard` to do so.
- You can save rviz configs.
- You are welcome to use a Gazebo world.
