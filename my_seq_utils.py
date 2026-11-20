def calc_gc_content(seq):
    """Return the GC content of a DNA sequence as a proportion (0 to 1)."""
    seq = seq.upper()
    gc_count = seq.count("G") + seq.count("C")
    return gc_count / len(seq)


def calc_at_content(seq):
    """Return the AT content of a DNA sequence as a proportion (0 to 1)."""
    seq = seq.upper()
    at_count = seq.count("A") + seq.count("T")
    return at_count / len(seq)

# Step 4: top-level code in your module
# Test the functions with a simple example
## print(calc_gc_content('GGCC'))
# This prints the 1.0 but we dont want that so step 5 fix this, and line 16 should be removed

# Step 5: the fix, if __name__ == '__main__': From Lecture 8, slide 27
# Only run these tests when this file is run directly, not when it is imported
if __name__ == '__main__':
    print(calc_gc_content('GGCC'))