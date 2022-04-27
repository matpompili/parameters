from setuptools import setup

with open("requirements.txt") as installation_requirements_file:
    requirements = installation_requirements_file.read().splitlines()

setup(
    name="parameters",
    version="0.2.0",
    packages=["parameters"],
    url="https://github.com/matpompili/parameters",
    author="Matteo Pompili",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description="TODO",
    install_requires=requirements,
    test_suite="tests",
    package_data={"": ["LICENSE"]},
)
