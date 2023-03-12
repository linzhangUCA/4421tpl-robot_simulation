# Robot Model Description 
Create a model for your robot using URDF. Tutorial: [URDF](https://docs.ros.org/en/humble/Tutorials/Intermediate/URDF/URDF-Main.html) 

## Instructions: 
1. (20%) Set up the package.
```bash
cd <your ros workspace>/src
git clone git@github.com:UCAEngineeringPhysics/a2-robot_model-<your github username>.git
cd ..
colcon build --packages-select diffbot_urdf
```
2. (80%) Create your robot's model by modifying the description file: `diffbot_urdf/urdf/diffbot.urdf.xacro`. You are encouraged to use [xacro](https://docs.ros.org/en/humble/Tutorials/Intermediate/URDF/Using-Xacro-to-Clean-Up-a-URDF-File.html) to ease the process. 

#### Hint:
After the first time you build the package, don't forget to source the overlay (your package) by `source <your ros workspace>/install/local_setup.bash`. You can automatically source it whenever you open a new terminal by adding the command to `~/.bashrc` (**only need to do this once**). `echo "source <your ros workspace>/install/local_setup.bash" >> ~/.bashrc` will get the job done. You'll replace <your ros workspace> with your actual ROS workspace name.
