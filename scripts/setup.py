import setuptools

long_description=open("README.md", "r").read()

setuptools.setup(
    name="factorial",
    version="0.0.1",
    author="Mr_Python",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="my_url",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
