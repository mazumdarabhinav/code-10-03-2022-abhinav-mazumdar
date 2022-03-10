from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import setup
from setuptools import find_packages

setup(
    name="vamster_bmi_service",
    version="1.0.1",
    author="Abhinav Mazumdar",
    classifiers = [
        'Programming Language :: Python :: 3.8'
    ],

packages=find_packages('src'),
package_dir={'': 'src'},
py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
include_package_data=True,

description="VAMSTER BMI SERVICE",
python_requires='>=3.8.*',

# Dependent packages (distributions)
install_requires=[
    'wheel',
    'pandas==1.4.1',
    'tabulate',
    'pytest'
],
setup_requires=[
        'pytest-runner'
    ],
test_suite="tests", 
)