from setuptools import setup, find_packages
from control_tools import __version__

setup(
    name='control_tools',
    version=__version__,
    author='robobe',
    author_email='robobe2020@gmail.com',
    description='control rools',
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "control_tools=control_tools.app:main"
        ]
    }
)
