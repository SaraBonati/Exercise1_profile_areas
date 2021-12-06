# Exercise 1 code (group: Skywalkers)

# possible links: https://pypi.org/project/shellinford/ (to create or use fm index)
# to load fasta data: https://www.biostars.org/p/710/ 
# for helper function sin python: https://nbviewer.org/gist/BenLangmead/6798379
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
from Bio import SeqIO


class Exercise1:

    def __init__(self,string_path):
        """
        Initialize exercise object with string that will be searched
        """
        if string_path.endswith('.txt'):
            with open(string_path, 'r') as file:
                self.string = file.read().replace('\n', '')
        else:
            self.string = SeqIO.read(string_path, "fasta")
        
        self.benchmarks={'find':[],'fm':[]}

    def find_simple(self,pattern_path):
        """
        This function searches for a pattern in a string using the find string method,
        we expect slow performance from this function
        """
        self.pattern = SeqIO.read(pattern_path, "fasta")
        logging.info(f"Found pattern occurrence at {string.find(self.pattern, string[0], string[-1])}")
        return string.find(self.pattern, string[0], string[-1])
        
    def fm_index(self):
        """
        This function returns the fm index of the input string and saves it in a separate file
        """

    def search_fm_index(self,query):
        """
        This function searches for a query pattern in the fm index previously saved
        """
    

if __name__ == "__main__":
    # get start time of the script:
    start = time.time()

    
    # script arguments    
    if len(sys.argv) > 1:
        string_file = sys.argv[1]
        pattern_file = sys.argv[2]
    else:
        string_file = 'simple_string.txt'
        pattern_file = 'simple_pattern.txt'
    
    # --------Specify paths--------------------------
    # Specify input directories and input files
    wdir = os.getcwd() # working directory (github repo)
    ddir = os.path.join(wdir,'data') # data directory
    exercise_string = os.path.join(ddir,string_file)
    exercise_pattern = os.path.join(ddir,pattern_file)
    ldir = os.path.join(wdir,'logs') # logs directory


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

    # ---------Start exercise (simple)-------------------------------
    Ex = Exercise1(exercise_string)

    start_simple = time.time()
    Ex.find_simple(exercise_pattern) 
    end_simple = time.time()
    time_simple = (end_simple-start_simple)/60 # time in minutes
    
    # ---------Start exercise (complex)------------------------------

    # ---------End exercise -----------------------------------------
    end = time.time()
    total_time = (end - start) / 60
    logging.info('------Stop logging------')
    logging.info('total running time: %0.2f minutes' % total_time)
    logging.shutdown()







