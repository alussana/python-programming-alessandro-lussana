# NOTE this implementation of pattern matchin is case sensitive
# Every count is zero-based

def bwt(s):
    s = s + '$'
    s = s.replace(' ', '_')
    last_i = len(s) - 1
    suffixes = []
    
    # create unsorted suffix array made of strings
    for i in range(last_i, -1, -1):
        suffixes.append(s[i::])
    
    # create unsorted suffix array made of indeces
    indeces = [i for i in range(last_i,-1,-1)]
    
    # create a dictionary to link every string to an index
    d = dict(zip(suffixes, indeces))

    # sort the suffixes
    suffixes = sorted(suffixes)

    # use the sorted suffixes to generate the proper suffix array
    sa = []
    for suffix in suffixes:
        sa.append(d[suffix])

    # use the suffix array to create the BWT
    transformed_list = []
    for i in sa:
        j = (i - 1) % (last_i + 1)
        transformed_list.append(s[j])
    transformed_s = ''.join(transformed_list)

    return(transformed_s)

def twb(s):
    # retrive the original string from the BWT
    pass

if __name__ == '__main__':
    s = 'All work and no play makes Jack a dull boy'
    print(s)
    transformed_s = bwt(s)
    print(transformed_s)
