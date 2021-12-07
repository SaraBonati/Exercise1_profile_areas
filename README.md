## Documentation

## Setup

### Install dependencies
This code runs on a linux environment with conda.

First, check if conda is already installed by running the following in your terminal:

    conda --version

If you don't have conda, you first need to install it on Linux using the terminal:

Download the latest shell script,
make the miniconda installation script executable and
run miniconda installation script:
    
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    chmod +x Miniconda3-latest-Linux-x86_64.sh
    ./Miniconda3-latest-Linux-x86_64.sh

Follow the installation instructions given in the terminal.

Now make sure you are in the main directory of this project and install the dependencies to execute the code by creating a conda environment:

    conda create --name pa_p6 python=3.8.8
    conda activate pa_p6

You should now be in the (pa_p6) environment.
To get a specific library (shellinford) running, execute these two lines:
    
    conda install gcc_linux-64
    conda install gxx_linux-64
    
Lastly install the requirements by executing:

    pip3 install -r requirements.txt

Use this environment to run the next steps.

### Directory organization
The following repository contains code and files organized as follows:

* `data` folder: in here the original `.fasta` files are stored
* `exercise.py` is the script contianing all exercise code. It can be run from the terminal with 

```python
python exercise.py text.dna4.short.fasta sampled_illumina_reads.fasta
```

* `results` in this folder we save the list of positions where the patterns were found, as well as the figures showing the results
* `logs` folder contains detailed log of the script execution, including run time for the different number of reads and other details