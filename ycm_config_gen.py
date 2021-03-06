#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate a configuration file for YouCompleteMe.

When running in a virtual environment, YouCompleteMe required a configuration
file in the root of the project, that tells YCM the path to the Python
interpreter the projects virtual environment uses. This script quickly creates
this file.

Example:
    $ python ycm_config_gen.py

Run the above command in the root of the virtual env project.
NOTE! Make sure that you run this script from the activated virtualenvironment,
otherwise it'll se the interpreter_path to your system Python.

"""

from os import path
from subprocess import run, CalledProcessError
import sys


def check_virtualenv():
    """Check if the current cwd is run in a virtual environment.

    Returns: True if yes, False if not.

    """
    return hasattr(sys, 'real_prefix')


def get_venv_path():
    """Search and return the path to the Python interpreter.

    Returns: Path to the Python interpreter.

    """
    try:
        process = run(['which', 'python'], check=True, capture_output=True,
                      encoding='utf-8',)
        interpreter_path = process.stdout
        interpreter_path = interpreter_path[0:-1]
        return interpreter_path
    except CalledProcessError as ex:
        raise ex
    return ''


def sala(nimi: str) -> str:
    """Function

    Args:
    function (TODO): TODO

    Returns: TODO

    """
    return nimi * 2

def write_config_file():
    """Write the config file for the directory."""
    int_path = get_venv_path()
    comment = "# Config file automatically generated by ycm_config_gen.py"
    to_file = (
        f"{comment}\n\n"
        f"def Settings(**kwargs):\n"
        f"    return {{\n"
        f"        'interpreter_path': '{int_path}'\n"
        f"        }}"
    )
    try:
        with open('.ycm_extra_conf.py', 'w') as out_file:
            out_file.write(to_file)
        if path.exists('.ycm_extra_conf.py'):
            print("Config file succesfully generated!")
            return
        print("Not able to find file! Please check the directory.")
    except EnvironmentError as ex:
        print("Problem with file handling: " + ex.strerror)


def main():
    """Execute when ran from the command line."""
    if not check_virtualenv():
        print("No virtual environment active! Have you tried activating it?")
        return
    write_config_file()

