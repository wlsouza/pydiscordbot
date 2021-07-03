from setuptools import setup, find_packages


def read_file(file_path):
    with open(file_path) as file:
        return [line.strip() for line in file.readlines()]

setup(
    name="pydiscordbot",
    version="0.1.0",
    description="Implementation of a multipurpose discord bot in python.",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_file("requirements.txt")
)

