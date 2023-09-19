from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in arc/__init__.py
from arc import __version__ as version

setup(
	name="arc",
	version=version,
	description="ARC For Zawya",
	author="arc",
	author_email="arc@ly.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
