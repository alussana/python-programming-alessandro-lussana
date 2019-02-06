## pseudo code Baum-Welch, one training sequence
## =================================================================================
## setup:
##      store the model's initial parameters:
##          states: list of state names, order is consistent with t,e,startp,endp
##          t: matrix of transition prob; t[from][to] (K states)
##          e: dictionary of emission prob; e[state][character]
##          startp: list of starting prob; startp[state]
##          endp: list of ending prob; endp[state]
##          symbols: list, alphabet, order is consistend with e[x]
##      data:
##          seq: a string, the sequence of N symbols; seq[0] is the first position; len(seq) = N
##      build the backward matrix B with
##          N columns (from position 1 to position N) 
##          K rows (one row for each state)
##
## import backward as bw
## import forward as fw
## 
## define compute_n_t: to compute the expected number of transitions given parameters and seq 
## define compute_n_e: to compute the expected number of emissions given parameters and seq
##
## define update_t: to compute for each state the updated transitions probabilities
## define update_startp: to compute for each state the updated starting probabilities
## define update_endp: to compute for each state the updated ending probabilities
##
## define update_e: to compute for each state the updated emission probabilities
##
## set delta_min, a minimum delta for the optimization step
##
## recursion
##      while delta_max > delta_min:
##
##          compute backward matrix B, total_prob
##          compute forward matrix F, total_prob
##          
##          initialize an empty list, expected_n_startp
##          for each state k:
##              append to expected_n_startp the returning value of compute_n_startp( k, startp, e,\
##                                                                                  total_prob, B)
##
##          initialize an empty list, expected_n_endp
##          for each state k:
##              append to expected_n_endp the returning value of compute_n_endp(k, endp, e, total_prob, F)
##
##          initialize an empty list, expected_n_t
##          for each state k:
##              append to expected_n_t the returning value of compute_n_t(k, t, e, total_prob, B, F)
##
##          initialize an empty list, expected_n_e
##          for each symbol c:
##              append to expected_n_e the returning value of compute_n_e(c, total_prob, B, F)
##
##          initialize delta, list of errors
##
##          for each k in t:
##              for each l in t[k]:
##                  new_value = update_t(k, l, expected_n_t)
##                  append sqrt((t[k][l] - new_value)^2) to delta
##                  t[k][l] = new_value
##
##          for each k in startp:
##              new_value = update_startp(k, expected_n_startp)
##              append sqrt((startp[k] - new_value)^2) to delta
##              startp[k] = new_value
##
##          for each k in endp:
##              new_value = update_endp(k, expected_n_endp)
##              append sqrt((endp[k] - new_value)^2) to delta
##              endp[k] = new_value
##
##          for each k in e:
##              for each c in symbols:
##                  new_value = update_e(k, c, expected_n_e)
##                  append sqrt((e[k][c] - new_value)^2) to delta
##                  e[k][c] = new_value
##
##          delta_max = max(delta)
## =================================================================================

if __name__ == '__main__':
    ## dummy data:
    ## dummy sequence
    seq = "ATCGCGAA"    ## length is 8
    ## dummy parameters
    ## states and symbols order are consistent with t and e
    states = ["Y","N"]
    t = [[0.7,0.3],[0.3,0.7]]                       ## starting parameters for transition probabilities
    e = [{"A":0.25,"T":0.25,"C":0.25,"G":0.25},\
        {"A":0.25,"T":0.25,"C":0.25,"G":0.25}]      ## starting parameters for emission probabilities
    startp = [0.5,0.5]                              ## starting parameters for probabilities
    endp = [0.5,0.5]                                ## starting parameters for ending probabilities