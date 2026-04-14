from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'turtlebot4_beep'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/turtlebot4_beep']),
    ('share/turtlebot4_beep', ['package.xml']),
    (os.path.join('share', 'turtlebot4_beep', 'launch'), glob('launch/*.py')),
],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rokey',
    maintainer_email='jihong527079@naver.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    # entry_points={
    #     'console_scripts': [
    #         'beep_node = turtlebot4_beep.beep_node:main'
    #     ],
    # },
    entry_points={
    'console_scripts': [
        'beep_node = turtlebot4_beep.beep_node:main',
    ],
},
)
