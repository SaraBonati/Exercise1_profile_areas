# Exercise 1 code (group: Skywalkers)
#----------------------------------------------------------
# general utility import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import glob
import os
import sys
import string
import logging
import time
import pickle
import itertools
import json
import re
from tqdm import tqdm

# bioninformatics specific tools
import Bio


class Exercise1:

    def __init__(self,string_path):
        """
        Initialize exercise object with string that will be searched
        """
        with open(string_path, 'r') as file:
            self.string = file.read().replace('\n', '')

    def find_simple(self,pattern_path):
        """
        This function searches for a pattern in a string using the find string method,
        we expect slow performance from this function
        """
        
    def fm_index(self):
        """
        This function returns the fm index of the input string and saves it in a separate file
        """

    def search_fm_index(self,query):
        """
        This function searches for a query pattern in the fm index previously saved
        """
    

if __name__ == "__main__":
    
    # script arguments    
    if len(sys.argv) > 1:
        string_file = sys.argv[1]
        pattern = sys.argv[2]
    else:
        string_file = 'Hello world'
        pattern = 'Hello'
    
    # --------Specify paths--------------------------
    # Specify input directories and input files
    wdir = os.getcwd() # working directory (github repo)
    ddir = os.path.join() # data directory
    simple_string = 
    simple_pattern = 
    exercise_string = 
    exercise_pattern = 
    ldir = os.path.join() # logs directory


    # -------Set-up logging---------------------
    logging_fn = os.path.join(ldir, f'exercise_{time.strftime("%Y_%m-%d_%H-%M-%S")}.log')
    # Get current data and time as a string:
    timestr = time.strftime("%Y_%m-%d_%H-%M-%S")
    # start logging:
    logging.basicConfig(filename=logging_fn, level=logging.DEBUG, format='%(asctime)s %(message)s',
                        datefmt='%d/%m/%Y %H:%M:%S')

    # Add basic script information to the logger
    logging.info("------Start Running exercise.py------")
    logging.info(f"Operating system: {sys.platform}\n")
    logging.info('')

    # ---------Start exercise (simple)------------------------------
    Ex = Exercise1(simple_string)




