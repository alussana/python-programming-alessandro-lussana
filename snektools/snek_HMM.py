### Simple Hidden Markov Model implementation in pandas
### Main features:
### Hmm object are built using parameters stored in external files (csv)
### An existing model can be trained with Baum-Welsch algorithm using TrainingSet objects
### Sequence objects are build from external files (fasta or plain text)
### Optimal hidden paths given a sequence and a model can be found with viterbi decoding
### Sequences can be generated given a model and a path
### Work is in progress

import numpy as np
import pandas as pd

## models are Hmm objects
class Hmm(object):
    
    def __init__(self, transitions_matrix, emissions_matrix, starting_prob, ending_prob):
        self.states = list(transitions_matrix.columns)
        self.alphabet = list(emissions_matrix.index)
        self.transitions = transitions_matrix
        self.emissions = emissions_matrix
        self.endingp = ending_prob
        self.startingp = starting_prob

## sequences with or without known paths or symbols are Sequence objects
class Sequence(object):

    def __init__(self, sequence = "unknown", path = "unknown", tag = "unknown"):
        self.sequence = sequence
        self.path = path
        self.tag = tag

## build a Sequence object with information stored in external files (fasta or plain text)
## at least one arg should be given
def import_sequence(sequence_fasta_file = False, path_fasta_file = False):
    
    sequence = "unknown"
    path = "unknown"
    tag = "unknown"

    ## store the symbols if they exist
    ## store the fasta header as the tag if it exists
    if sequence_fasta_file != False:
        
        sequence = "-"
        with open(sequence_fasta_file) as sequence_fasta:
            line = sequence_fasta.readline()
            line = line.strip()
            if line[0] == ">":
                tag = line[1:len(line)]
            else:
                sequence = sequence + line
            for line in sequence_fasta:
                line = line.strip()
                sequence = sequence + line
        sequence = sequence + "-"
    
    ## store the path if it exists
    ## store the fasta header as a tag if it exists and if tag was not defined
    if path_fasta_file != False:
        
        path = "B"
        with open(path_fasta_file) as path_fasta:
            line = path_fasta.readline()
            line = line.strip()
            if line[0] == ">":
                if tag == "":
                    tag = line[1,len(line)]
            else:
                path = path + line
            for line in path_fasta:
                line = line.strip()
                path = path + line
        sequence = sequence + "E"
    
    return(Sequence(sequence, path, tag))

## build a Hmm object with parameters stored in external files (csv)
def import_model(transitions_matrix_file, emissions_matrix_file, starting_prob_file, ending_prob_file):
    
    ## import transitions matrix
    ## MEMO trasitions are intended from columns states to rows states (col -> rows) 
    transitions_matrix = pd.read_table(transitions_matrix_file, header=0, index_col=0, sep=",")

    ## import emissions matrix
    ## MEMO emissions: from states in rows to symbols in columns
    emissions_matrix = pd.read_table(emissions_matrix_file, header=0, index_col=0, sep=",")
    emissions_matrix = emissions_matrix.T

    ## import starting probabilities
    starting_prob = pd.read_csv(starting_prob_file)

    ## import ending probabilities
    ending_prob = pd.read_csv(ending_prob_file)

    ## build model object
    starting_model = Hmm(transitions_matrix, emissions_matrix, starting_prob, ending_prob)

    return(starting_model)

## helper function for viterbi
def find_max(scores, states):
    ## states order must be consistent with scores order
    max_states = []
    uniq_max = max(scores)
    for i in range(len(scores)):
        if scores[i] == uniq_max:
            max_states.append(states[i])

    return(uniq_max, max_states)

## helper function for viterbi
def decode_paths(viterbi_matrix):

    ## initialize the list of optimal paths
    P = []

    all_path_decoded = 0

    ## decoding
    while all_path_decoded == 0:
        
        multipath = 0

        ## initialize a new reversed path
        path = ["E"]

        ## determine the last state
        num_of_pos = len(viterbi_matrix.columns)-1
        state_index = len(viterbi_matrix[num_of_pos][0][1]) - 1

        if state_index != 0:
            multipath = 1

        state = viterbi_matrix[num_of_pos][0][1][state_index]
        path.append(state)

        if state_index > 0:
            viterbi_matrix[num_of_pos][0][1].pop(state_index)

        ## decode all the other states
        for position in list(viterbi_matrix.columns)[len(viterbi_matrix.columns)-2:1:-1]:
            
            state_index = len(viterbi_matrix[position][state][1]) - 1
            
            state = viterbi_matrix[position][state][1][state_index]
            path.append(state)

            if state_index != 0:
                viterbi_matrix[position][0][1].pop(state_index)
                multipath = 1

        ## add the path to the list of the optimal paths
        path.append("B")
        path = path[::-1]
        P.append(path)

        if multipath == 0:
            all_path_decoded = 1

    return(P)

def viterbi(model, sequence):
    
    ## initialiaze the viterbi matrix V
    V = pd.DataFrame(index=model.states,columns=[i for i in range(len(sequence.sequence))])
    V[0] = 1.0 

    ## fill the first column (the first position in the sequence)
    position = 1
    column_scores = []
    for state in V.index:
        score = float(model.startingp[state] * model.emissions[state][sequence.sequence[position]])
        column_scores.append([score,"B"])
    V[1] = column_scores

    ## iteration:
    for position in V.columns[2:len(V.columns) - 1]:
        column_scores = []
        
        for position_state in model.states:
            scores = []
            
            for previous_state in model.states:
                score = V[position - 1][previous_state][0]
                scores.append(score * model.transitions[previous_state][position_state])
            
            ## maximize score, find optimal states
            max_score,max_paths = find_max(scores, model.states)
            ## multiply for the emission probability
            max_score = max_score * model.emissions[position_state][sequence.sequence[position]]
            ## fill the column
            column_scores.append([max_score,max_paths])

        ## update the viterbi matrix
        V[position] = column_scores

    ## termination
    position = position + 1
    column_scores = []

    for position_state in model.states:
        scores = []

        for previous_state in model.states:
            score = V[position - 1][previous_state][0]
            scores.append(score * float(model.endingp[state]))

        ## maximize score, find optimal states
        max_score,max_paths = find_max(scores, model.states)
        ## fill the last column
        column_scores.append([max_score,max_paths])

    ## update the viterbi matrix
    V[position] = column_scores
    
    ## decode all the optimal paths
    P = decode_paths(V)
    return(P)

######################################
### Test This for Viterbi Decoding ###
'''
import snek_HMM as snek
import pandas as pd
import numpy as np
transitions_matrix_file = "transitions_matrix.txt"
emissions_matrix_file = "emissions_matrix.txt"
starting_prob_file = "starting_probabilities.txt"
ending_prob_file = "ending_probabilities.txt"
sequence_fasta_file = "CpG.fa"
model = snek.import_model(transitions_matrix_file, emissions_matrix_file, starting_prob_file, ending_prob_file)
sequence = snek.import_sequence(sequence_fasta_file = sequence_fasta_file)
V = snek.viterbi(model, sequence)
'''
