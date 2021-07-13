from setuptools import setup, find_packages

# Get Long Description
with open("README.md", "r") as readme:
    long_description = readme.read().replace("Â", "")
with open("requirements.txt", "r") as requirements:
    reqs = requirements.read().splitlines()

setup(
    name="PasswordCardGenerator",
    version="1.0.1",
    # Major version 1
    # Minor version 0
    # Maintenance version 0

    author="DerSchinken",
    description="A Password Card Generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=reqs,
    python_requires=">=3.7",
    url="https://GitHub.com/DerSchinken/PasswordCardGenerator",
    keyword=[
        "PasswordCardGenerator",
        "Password Card Generator",
        "Password",
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',

        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10"
    ],
)
