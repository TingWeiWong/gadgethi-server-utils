import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gadgethiServerUtils", # Replace with your own username
    version="0.2.16",
    author="Gadgethi Develop Team",
    author_email="developers@gadget-hitech.com",
    description="Gadgethi server maintenance package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/weitung/gadgethiServerUtils.git",
    packages=setuptools.find_packages(),
    install_requires=[
        'pycryptodomex',
        'pyyaml==5.1',
        'psycopg2-binary'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)