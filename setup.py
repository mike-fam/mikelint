import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="mikelint",
    version="1.2.6",
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
        "astroid>=2.5.6,<3.0.0",
        "PyYAML==5.3.1",
    ],
    python_requires=">=3.8",
    # package_dir={"": ""}
)
