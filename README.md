Hi

This github repository contains code changes to learn about writing a 
simple Jupyter Kernel called **MyEcho Kernel**. As the name suggests, 
the kernel will simply return whatever is passed from the Notebook UI.

## Structure of the Project
1. *echo_kernel* directory contains the actual python code for starting the kernel python process.
2. *kernel-spec* directory contains the Spec file which will be installed in Jupyter Environment.
3. *example* directory contains a sample notebook which can be used to test the kernel. \ 
   You are free to create a new notebook of your choice.
4. `Makefile` contains the handy commands which will to setup and test this project. 
5. `setup.py` is a standard setup file for installing the project.
6. `requirements.yml` is a standard conda requirements file which contains the python dependencies that are needed.  

## Pre-requisite
1. git clone this repository:
```python
git clone <>
cd echo-kernel
```

## Setting up the Env using Make Commands.
This is option 1 where we start fresh from creating a conda environment and installing \
all the libraries required to test this kernel on a Classic Jupyter Notebook UI.

1. Create a conda env: `make env`
2. Activate the env: `make activate-env` or `conda activate learning_echo_kernel`
3. Install the kernel library to environment. `make dev-install`
4. Install the kernel Spec to environment: `make install-echo-kernel-spec`
5. Verify the kernel spec is available : `jupyter-kernelspec list`
6. Install Classic Jupyter notebook: `pip instal notebook==6.4.6`
7.

## install the kernel to separate notebook env
This is option 2.
- Lets assume you have a different conda env `jupyter_notebook` where notebook run
- active the conda env: `conda acivate jupyter_notebook`
- install this Echo kernel to the same env: `make dev-install`
- install the kernel-spec to the jupyter env:
```python
make install-echo-kernel-spec
# verify the kernel is installed.
jupyter-kernelspec list
```
- start jupyter notebook : `jupyter notebook --debug`
- create a notebook by selecting "MyEchoKernel" or open the notebook present in the `example/` folder.
