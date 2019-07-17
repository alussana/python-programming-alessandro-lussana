# NOTE this implementation of pattern matching is case sensitive
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

def twb(b):
    # count characters occurence and fm_index
    char = []
    occ = []
    fm_index = []
    for c in b:
        if c not in char:
            char.append(c)
            occ.append(1)
            fm_index.append(1)
        else:
            i = char.index(c)
            occ[i] += 1
            fm_index.append(occ[i])
    char_count = dict(zip(char, occ))

    # sort the char_count dictonary
    sorted_char = sorted(char_count)
    sorted_count = []
    for v in sorted_char:
        sorted_count.append(char_count[v])
    char_count = dict(zip(sorted_char, sorted_count))

    # retrieve the original sequence
    t = 0
    s = []
    for i in range(0, len(b) - 1):
        s.append(b[t])
        b_index = -1
        x = 0
        while b[t] != sorted_char[x]:
            b_index += char_count[sorted_char[x]]
            x += 1
        b_index += fm_index[t]
        t = b_index

    # translate _ with \s
    translated_s = []
    for i in range(0, len(s)):
        if s[i] != '_':
            translated_s.append(s[i])
        else:
            translated_s.append(' ')

    s= translated_s[::-1]
    s = ''.join(s)

    return(s)

if __name__ == '__main__':
    s = input('Insert string: ')
    transformed_s = bwt(s)
    print('BWT:', transformed_s)
    print('Deleting input string.')
    s = []
    print('Retrieving input string from the BWT.')
    s = twb(transformed_s)
    print('Recoded string:', s)

