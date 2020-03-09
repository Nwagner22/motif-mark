# motif-mark

### Usage:
To run motif-mark use the command **python motif_mark.py** in combination with the flags below.


### Flags:
* -f: Use to specify the file path to TWO LINE fasta file  REQUIRED
* -m: Use to specify the file path to the file that contains the desired motifs to look for REQUIRED
* -o: Use to specify the .svg output file name and path.  DEFAULT: motif_output.svg
* -h: Help

### Required packages:
* re (regular expressions)
* os (operating system)
* argparse
* math
* cairo
* pycairo

**Example:**
```
python3 motif_mark.py -f ../Data/Figure_1_converted.fasta -m ../Data/Fig_1_motifs.txt
```

