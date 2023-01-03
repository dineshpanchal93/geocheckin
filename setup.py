from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in geo_location/__init__.py
from geo_location import __version__ as version

setup(
	name="geo_location",
	version=version,
	description="employee check-in using geo location",
	author="Kishan Panchal",
	author_email="k.d.panchalntvofc@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
