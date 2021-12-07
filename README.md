## Documentation

### Setup

* Download python
* Activate virtual environment ..

### Directory organization
The following repository contains code and files organized as follows:

* `data` folder: in here the original `.fasta` files are stored
* `exercise.py` is the script contianing all exercise code. It can be run from the terminal with 

```python
python exercise.py text.dna4.short.fasta sampled_illumina_reads.fasta
```

* `results` in this folder we save the list of positions where the patterns were found, as well as the figures showing the results
* `logs` folder contains detailed log of the script execution, including run time for the different number of reads and other details