import setuptools
import os

with open("README.md", "r") as fh:
    long_description = fh.read()

with open(os.path.join(os.path.dirname(__file__), "requirements.txt"), "r") as f:
    requirements = f.read().split("\n")

setuptools.setup(
    name="gadgethiServerUtils", # Replace with your own username
    version="0.3.39",
    author="Gadgethi Develop Team",
    author_email="developers@gadget-hitech.com",
    description="Gadgethi server maintenance package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/weitung/gadgethiServerUtils.git",
    license="AGPLv3+",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": ["gserver = gadgethiServerUtils.main:command_line_interface"]
    },
    install_requires=requirements,
    package_dir={"gadgethiServerUtils": "gadgethiServerUtils"},
    test_suite="gadgethiServerUtils.tests",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries ",
    ],
    python_requires='>=3.5',
)