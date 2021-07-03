from setuptools import setup, find_packages


def read_file(file_path):
    with open(file_path) as file:
        return [line.strip() for line in file.readlines()]

setup(
    name="starbot",
    version="0.1.0",
    description="Star bot",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_file("requirements.txt")
)

