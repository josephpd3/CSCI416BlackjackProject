# CSCI416BlackjackProject

## Premise

The goal of this project was to program a simple casino game in two languages of my choice.

I chose the following:

* Javascript, specifically Ecmascript2015 or ES6
* Python 3.5

## Running Javascript

*NOTE: Commands may differ in Windows. Please refer to docs for node and grunt if there are issues, and remember to use the proper file-system directory separator.*

For Javascript you will need `npm` installed globally along with `grunt`.

Once you have both, you can just navigate to the javascript directory and type `grunt`--the scripts should handle the rest. It will install Babel, which will transpile the ES6 to standardized javascript, then run the script compiled in the `javascript/dist` folder.

## Running Python

*NOTE: Commands may differ in Windows. Please refer to docs for virtualenv if there are issues, and remember to use the proper file-system directory separator.*

For Python, you will need `Python 3.5` and its package manager, `pip`.

You will then need to install `virtualenv` which you can do easily with pip: `pip install virtualenv`.

Inside the python directory, run `virtualenv -p /path/to/Python3.5 venv` to create a virtual environment in `python/venv`.

From the python directory, you can run `source venv/bin/activate` to start up the virtual environment, which will hold the dependencies for the project, allowing you to keep it independent from your system-bound Python installation.

Finally, you can run `pip install -r requirements.txt` in the python directory to install `numpy`, allowing you use of it in the script. Then you can run `python blackjack.py` as you normally would, and the virtual environment will stand in as your python execution script with all its dependencies, as opposed to using the one native to your OS.
