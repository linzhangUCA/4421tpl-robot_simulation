import os
from glob import glob
from setuptools import setup

package_name = 'diffbot_gazebo'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join("share", package_name, "urdf"), glob(os.path.join("urdf", "*"))),
        (os.path.join("share", package_name, "launch"), glob(os.path.join("launch", "*"))),
        (os.path.join("share", package_name, "rviz"), glob(os.path.join("rviz", "*"))),
        (os.path.join("share", package_name, "worlds"), glob(os.path.join("worlds", "*"))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='TODO',
    maintainer_email='todo@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
