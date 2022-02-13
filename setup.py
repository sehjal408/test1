from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in student_mentor/__init__.py
from student_mentor import __version__ as version

setup(
	name="student_mentor",
	version=version,
	description="Student Mentor Data",
	author="SK",
	author_email="sehjal021220@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
