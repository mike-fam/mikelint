import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="mikelint",
    version="1.0.6",
    description="Linter used for CSSE1001 at UQ",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/mike-fam/mikelint",
    author="Mike Pham",
    author_email="mikepham1207@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["mikelint"],
    include_package_data=True,
    install_requires=[
        "astroid>=2.5",
        "docstring-parser>=0.7",
        "isort>=5.8",
        "lazy-object-proxy>=1.6",
        "mccabe>=0.6",
        "PyYAML>=5.4",
        "toml>=0.10",
        "wrapt>=1.12"
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "run=run:main",
        ]
    },
    # package_dir={"": ""}
)
