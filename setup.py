from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = "My echo kernel"
LONG_DESCRIPTION = "Learning to write a Kernel for Jupyter which will echo!"

setup(
    name="echo_kernel",
    version=VERSION,
    author="rahul26goyal",
    description=DESCRIPTION,
    long_decription=LONG_DESCRIPTION,
    packages=['echo_kernel'],  # or use find_packages()
    install_requires=[],  # captured in requirements.yml
    keywords=['python', 'echo kernel', 'jupyter'],
    classifiers= [
        "Development Status :: Alpha-0",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X"
    ]
)
