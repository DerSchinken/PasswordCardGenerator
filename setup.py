from setuptools import setup, find_packages

# Get Long Description
with open("README.md", "r") as readme:
    long_description = readme.read().replace("Â", "")
# Get requirements
with open("requirements.txt", "r") as requirements:
    reqs = requirements.read().splitlines()

setup(
    name="PasswordCardGenerator",
    version="1.3.4",
    # Major version 1
    # Minor version 3
    # Maintenance version 4

    author="DerSchinken",
    maintainer="DerSchinken",
    description="A Password Card Generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license_files=["LICENSE"],
    packages=find_packages(),
    package_data={"PasswordCardGenerator": ["*.TTF"]},
    include_package_data=True,
    install_requires=reqs,
    python_requires=">= 3.6",
    project_urls={
        "Homepage": "http://index12.bplaced.net/",
        "Github": "https://github.com/DerSchinken/PasswordCardGenerator",
    },
    keyword=[
        "PasswordCardGenerator",
        "Password Card Generator",
        "Password",
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',

        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10"
    ],
)
