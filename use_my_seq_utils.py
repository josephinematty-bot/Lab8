# Way 1: Import the whole module
# This way calculates both GC and AT contents
import Lab8.my_seq_utils as my_seq_utils

seq = 'ATGC'
print(my_seq_utils.calc_gc_content(seq))
print(my_seq_utils.calc_at_content(seq))

# Way 2: import only the functions you need
# This way of import only calculates GC contents only
from Lab8.my_seq_utils import calc_gc_content

seq = 'ATGC'
print(calc_gc_content(seq))

## Print out: 
# line 2 - Gives access to every function in my_seq_utils, e.g. GC and AT content
# line 10: # Gives access to calc_gc_content only, so AT content can't be used here



        