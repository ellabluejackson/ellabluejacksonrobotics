from setuptools import find_packages, setup

package_name = 'lab1_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ella-blue-jackson',
    maintainer_email='ella-blue-jackson@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'talker = lab1_pkg.talker:main',
        'listener = lab1_pkg.listener:main',
        'counter = lab1_pkg.counter:main',
        'even_subscriber = lab1_pkg.even_subscriber:main',
    ],
},



)
