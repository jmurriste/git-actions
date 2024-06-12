from setuptools import (
    find_packages,
    setup,
)

setup(
    name='packaging',
    version='0.1',
    # packages=['packaging'],
    packages=find_packages(),
    # include any addtional files needed by the package
    include_package_data=True,
    # specify the package metadata
    author='jorge',
    author_email='jorge@jorge.com',
    description='a simple package',
    license='MIT',
    install_requires=[""],
    setup_requires=["wheel"]
)
