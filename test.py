import setuptools
import os.path

with open("README.md", "r") as fh:
    long_description = fh.read()

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setuptools.setup(
    name="your-project-id",
    version=get_version('version.txt'),
    author="<Author>",
    author_email="<Author email>",
    description="<Sample description>",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="<Github url for your project>",
    packages=setuptools.find_packages(),
    test_suite="tests",
    install_requires=['dependencies'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)