def compute_avg(numbers):
    summation = 0
    for i in numbers:
        summation = summation + float(i)
    return(summation / len(numbers))

def powah(a, b):
    return(a ** b)

def inverse_of(a):
    return(1 / float(a))

def quadratic_fun(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        return("negative delta, sorry bruh")
    else:
        x1 = (2 * b + delta) / 2
        x2 = (2 * b - delta) / 2
        return([x1,x2])

def quadratic_calc(a, b, c, x):
    return(a * x ** 2 + b * x + c)

def inv_quadratic_calc(a, b, c, x):
    inv_x = inverse_of(x)
    return(quadratic_calc(a, b, c, inv_x))

def reverse_complement(seq1, seq2):
    complement_dict = {"A": "T", "G": "C", "C": "G", "T": "A"}
    seq1 = seq1[::-1]
    complement = ""
    for nt in seq1:
        complement = complement + complement_dict[nt]
    return(complement == seq2)

def cov_calc(set1, set2):
    if len(set1) == len(set2):
        m1 = compute_avg(set1)
        m2 = compute_avg(set2)
        sq_devs = []
        N = len(set1)
        for i in range(N):
            sq_devs.append((float(set1[i]) - m1) * (float(set2[i]) - m2))
        return(sum(sq_devs) / N)
    else:
        return("let len(set1) == len(set2) be True. Please.")
        
def times_table(n):
    col1 = list(range(1,11))
    time_table = []
    for i in col1:
        row = [int(i), int(i) * float(n)]
        time_table.append(row)
    return(time_table)

def pairwise_substitution_log_odd(alignment_file_name):
    import numpy
    import math
    alignment_file = open(alignment_file_name)
    alignment = alignment_file.read()
    symbols = ["A","G","C","T"]
    alignment = alignment.split("\n")
    seq1 = alignment[0]
    seq2 = alignment[1]
    substitution_matrix = numpy.zeros((len(symbols),len(symbols)))
    catseq = seq1 + seq2
    for i in range(len(symbols)):
        for j in range(len(symbols)):
            substitutions = 0
            for a in range(len(seq1)):
                if seq1[a] == symbols[i] and seq2[a] == symbols[j]:
                    substitutions += 1
                if seq1[a] == symbols[j] and seq2[a] == symbols[i]:
                    substitutions += 1
            p_ij = substitutions / len(seq1)
            p_i_p_j = (catseq.count(symbols[i]) + catseq.count(symbols[j])) / 2 * len(seq1)
            if (p_ij > 0):
                substitution_matrix[i][j] =  math.log(p_ij / p_i_p_j)
            else:
                substitution_matrix[i][j] = -math.inf
    return(substitution_matrix)

# =================== #
# === compute_avg === #
#numbers = input("numbers separated by \s = ")
#numbers = numbers.strip() ## not needed, at least in python3
#numbers = numbers.split(" ")
#print(compute_avg(numbers))

# ===================== #
# === quadratic_fun === #
#a = input("a: ")
#b = input("b: ")
#c = input("c: ")
#print(quadratic_fun(float(a), float(b), float(c)))

# ========================== #
# === inv_quadratic_calc === #
#a = input("a: ")
#b = input("b: ")
#c = input("c: ")
#x = input("x: ")
#print(inv_quadratic_calc(float(a), float(b), float(c), float(x)))

# ========================== #
# === reverse_complement === #
#seq1 = input("seq1: ")
#seq2 = input("seq2: ")
#print(reverse_complement(seq1, seq2))

# ================ #
# === cov_calc === #
#set1 = input("set1 (numbers separated by \",\"): ")
#set2 = input("set2 (numbers separated by \",\"): ")
#set1 = set1.split(",")
#set2 = set2.split(",")
#print(cov_calc(set1, set2))

# ================== #
# === time_table === #
#n = input("n: ")
#tabula = times_table(n)
#print(tabula)
#for row in tabula:
#    print("%d     %f" %(row[0], row[1]))

# ===================================== #
# === pairwise_substitution_log_odd === #
file = input("alignment file: ")
print(pairwise_substitution_log_odd(file))
