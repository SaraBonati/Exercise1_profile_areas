# Exercise 1 code (group: Skywalkers)

# possible links: https://pypi.org/project/shellinford/ (to create or use fm index)
# to load fasta data: https://www.biostars.org/p/710/ 
# for helper function sin python: https://nbviewer.org/gist/BenLangmead/6798379
# ----------------------------------------------------------
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
import pickle
from tqdm import tqdm
from memory_profiler import memory_usage
import shellinford

# bioninformatics specific tools
from Bio import SeqIO

reads = [100, 500, 1000, 5000] # [100, 500, 1000, 5000, 10_000, 100_000, 500_000, 1_000_000]

class Exercise1:
    def __init__(self, string_path, pattern_path):
        """
        Initialize exercise object with string that will be searched
        """
        if string_path.endswith('.txt'):
            with open(string_path, 'r') as file:
                self.string = file.read().replace('\n', '')
        else:

            self.string = next(SeqIO.parse(string_path, 'fasta'))  # one unique record, 1 chromosome
            logging.info("------Chromosome 1 (long string) loaded!------")
            logging.info(f'string id: {self.string.id}')
            logging.info(f'string length: {len(self.string)}')

            self.patterns = list(
                SeqIO.parse(pattern_path, "fasta"))  # multiple search patterns, 100000 records to be precise
            logging.info("------Patterns loaded!------")
            logging.info(f'Number of patterns: {len(self.patterns)}')

        self.benchmarks = {'find': {}, 'fm': {}}

    def find_simple(self, reads):
        """
        This function searches for a pattern in a string using the find string method,
        we expect slow performance from this function
        """
        index_found = []
        for n in tqdm(range(reads)):
            index_found.append(str(self.string.seq).find(str(self.patterns[n].seq)))
            # logging.info(f"For {reads} reads found {len(index_found)} pattern occurrences")
        return index_found

    def fm_index(self, file_path):
        """
        This function returns the fm index of the input string and saves it in a separate file
        """
        self.fm = shellinford.FMIndex()
        self.fm.build(self.string.seq, file_path)

    def search_fm_index(self, reads, make_index=False):
        """
        This function searches for a query pattern in the fm index previously saved
        """
        if make_index:
            startfm = time.time()
            self.fm = shellinford.FMIndex()
            self.fm.build(str(self.string.seq))
            endfm = time.time()
            logging.info(f'for fm index time : {np.round((endfm - startfm) / 60, 4)}')

        start = time.time()
        counts = 0
        for n in tqdm(range(reads)):
            for doc in self.fm.search(str(self.patterns[n].seq)):
                counts+=1
                #logging.info(f'doc_count: {doc.count}')
                #print('doc_id:', doc.doc_id)
                #print('count:', doc.count)
                #print('text:', doc.text)
        end = time.time()
        logging.info(f'doc_count: {counts}')
        logging.info(f'{r} reads : {np.round((end-start)/60,4)}')
        return np.round((end-start)/60,4)

    def plot_time_benchmarks(self):
        """
        This function plots the time benchmarks of the pattern search for find method and fm index
        """

        #reads = [100,500,1000] #,5000,10000]

        # define figure
        fig = plt.figure(figsize=(18,9))
        gs = gridspec.GridSpec(1,1)
        ax = {}
        
        x = np.arange(len(reads))  # the label locations
        width = 0.35  # the width of the bars

        ax[0] = fig.add_subplot(gs[0,0])
        ax[0].bar(x - width/2, list(self.benchmarks['find'].values()), width, label='String find method')
        ax[0].bar(x + width/2, list(self.benchmarks['fm'].values()), width, label='FM-index')
        ax[0].set_ylabel('Time (minutes)')
        ax[0].set_title('Time benchmarks')
        #ax[0].set_xticks(x, list(self.benchmarks['find'].keys()))
        ax[0].legend(loc='best')
        fig.tight_layout()
        plt.savefig(os.path.join(rdir,'time_plot.pdf'),dpi=300,format='pdf')
        plt.savefig(os.path.join(rdir,'time_plot.png'),dpi=300,format='png')


    def plot_memory_benchmarks(self,memory_results_simple,memory_results_fm):
        """
        This function plots the memory benchmarks of the pattern search for find method and fm index
        """
        #reads = [100,500,1000] #,5000,10000]
        
        cmb                 = plt.get_cmap('Blues')                            
        cmb_subsection      = np.linspace(.3,.9,len(reads))                             
        colorsb             = [cmb(x) for x in cmb_subsection[::-1]]

        # define figure
        fig = plt.figure(figsize=(20,12))
        gs = gridspec.GridSpec(2,1)
        ax = {}

        ax[0] = fig.add_subplot(gs[0,0])
        for r in range(len(reads)):
            ax[0].plot(memory_results_simple[reads[r]],color=colorsb[r],label=f'{reads[r]} reads')
        ax[0].set_xlabel('Time (s)')
        ax[0].set_ylabel('Memory consumption (MB)')
        ax[0].set_title('String find method')
        ax[0].legend(loc='best')

        ax[1] = fig.add_subplot(gs[1,0])
        for r in range(len(reads)):
            ax[1].plot(np.arange(0,100),color=colorsb[r],label=f'{reads[r]} reads')
        ax[1].set_xlabel('Time (s)')
        ax[1].set_ylabel('Memory consumption (MB)')
        ax[1].set_title('FM-index')
        ax[1].legend(loc='best')

        fig.tight_layout()
        plt.savefig(os.path.join(rdir,'memory_plot.pdf'),dpi=300,format='pdf')
        plt.savefig(os.path.join(rdir,'memory_plot.png'),dpi=300,format='png')
        

#-------------------------------------------------------------------
#-------------------------------------------------------------------

if __name__ == "__main__":
    # get start time of the script:
    start = time.time()
    
    # script arguments    
    if len(sys.argv) > 1:
        string_file = sys.argv[1]
        pattern_file = sys.argv[2]
    else:
        string_file = r'C:\Users\sarab\Desktop\profile_areas_2021\bioinformatics1\data\text.dna4.short.fasta'
        pattern_file = r'C:\Users\sarab\Desktop\profile_areas_2021\bioinformatics1\data\sampled_illumina_reads.fasta'
    
    # --------Specify paths--------------------------
    # Specify input directories and input files
    wdir = os.getcwd() # working directory (github repo)
    print(wdir)
    ddir = os.path.join(wdir,'data') # data directory
    print(ddir)
    exercise_string = os.path.join(ddir,string_file)
    exercise_pattern = os.path.join(ddir,pattern_file)
    ldir = os.path.join(wdir,'logs') # logs directory
    rdir = os.path.join(wdir,'results') # results directory


    # -------Set-up logging---------------------
    logging_fn = os.path.join(ldir, f'exercise_{time.strftime("%Y_%m-%d_%H-%M-%S")}.log')
    # Get current data and time as a string:
    timestr = time.strftime("%Y_%m-%d_%H-%M-%S")
    # start logging:
    logging.basicConfig(filename=logging_fn, level=logging.DEBUG, format='%(asctime)s %(message)s',
                        datefmt='%d/%m/%Y %H:%M:%S')
    logging.getLogger('matplotlib.font_manager').disabled = True

    # Add basic script information to the logger
    logging.info("------Start Running exercise.py------")
    logging.info(f"Operating system: {sys.platform}\n")
    logging.info('')

    # ---------Start exercise (simple)-------------------------------
    logging.info("------Start loading chromosome 1 (long string)------")
    Ex = Exercise1(exercise_string, exercise_pattern)

    # exercise parameters and result storage
    #reads = [100]  # ,500,1000,5000,10000]#, 5000, 10000]
    position_results_simple = {}
    memory_results_simple = {}

    for r in reads:
        start_simple = time.time()
        position_results_simple[r] = Ex.find_simple(r)
        end_simple = time.time()
        Ex.benchmarks['find'][r] = np.round((end_simple - start_simple) / 60, 4)

        memory_results_simple[r] = memory_usage((Ex.find_simple, (r,)))

        #    time_simple = (end_simple-start_simple)/60 # time in minutes

        logging.info(
            f'For {reads} reads the total running time is {np.round((end_simple - start_simple) / 60, 4)} minutes')

    # save position results
    with open(os.path.join(rdir, 'positions_simplefind_time_results.pickle'), 'wb') as handle:
        pickle.dump(position_results_simple, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # save memory results
    with open(os.path.join(rdir, 'memory_simplefind_time_results.pickle'), 'wb') as handle:
        pickle.dump(memory_results_simple, handle, protocol=pickle.HIGHEST_PROTOCOL)

    # ---------Start exercise (complex)------------------------------
    #reads = [100,500,1000] #,5000,10000]
    time_results_fm = {}
    memory_results_fm = {}

    for r in reads:
        if r==reads[0]:
            Ex.benchmarks['fm'][r] = Ex.search_fm_index(r,True) 
        else:
            Ex.benchmarks['fm'][r] = Ex.search_fm_index(r,False) 

    #for r in reads:
    #    if r==100:
    #        memory_results_fm[r] = memory_usage(Ex.search_fm_index,(r,))
    #    else:
    #        memory_results_fm[r] = memory_usage(Ex.search_fm_index,(r,))
        

    # save memory results
    with open(os.path.join(rdir,'fm_time_results.pickle'), 'wb') as handle:
        pickle.dump(memory_results_fm, handle, protocol=pickle.HIGHEST_PROTOCOL)
    

    #-----------------PLOT-------------------------------------------
    Ex.plot_time_benchmarks()
    Ex.plot_memory_benchmarks(memory_results_simple,memory_results_fm)
    # ---------End exercise -----------------------------------------
    end = time.time()
    total_time = (end - start) / 60
    logging.info('------Stop logging------')
    logging.info('total running time: %0.2f minutes' % total_time)
    logging.shutdown()

    print(Ex.benchmarks)
    print(memory_results_simple)


