
ENV:=learning_echo_kernel
SA?=source activate

env:
	-conda env create --file requirements.yml --name ${ENV}

activate-env:
	-conda activate learning_echo_kernel
clean-env:
	- conda-env remove --name ${ENV}

dev-install:
		-pip install -e .

install-echo-kernel-spec:
	-jupyter kernelspec install --name echo_kernel ./kernel-spec
	-jupyter-kernelspec list

clean:
		-rm -rf dist
		-rm -rf build
		-rm -rf *.egg-info
		-find . -name __pycache__  -type d -exec rm -fr {} +

build:
		-python setup.py sdist bdist_wheel