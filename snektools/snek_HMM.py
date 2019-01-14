import numpy as np
import pandas as pd

class hmm(object):
    
    def __init__(self, transitions_matrix, emissions_matrix):
        self.states = list(transitions_matrix.columns)
        self.transitions = transitions_matrix
        self.emissions = emissions_matrix
    
    #def show_emissions(self):
    #    print("Emissions for model ", self, "\n")
    #    for key in self.emissions.columns:
    #        print("State: ", key)
    #        for symbol in self.emissions.key.index:
    #            print("Symbol: ", symbol, "\tEmission probability: ", self.emissions.key[symbol])
    #            print("")
    
    #def show_transitions(self):
    #    print("Transitions for model ", self, "\n")
    #    for state in transitions_matrix.columns:
    #        print("Transitions for model ", self, "\n")
    #        for other_state in transitions_matrix.state:
    #            print(state, " --> ", other_state, ": ", transitions_matrix.state[other_state])
    #        print("")

def build_starting_model(transitions_matrix_file_name, emissions_matrix_file_name):
    
    ## import transitions matrix
    ## MEMO trasitions are intended from columns states to rows states (col -> rows) 
    transitions_matrix = pd.read_table(transitions_matrix_file_name, header=0, index_col=0, sep=",")

    ## import emissions matrix
    emissions_matrix = pd.read_table(emissions_matrix_file_name, header=0, index_col=0, sep=",")
    emissions_matrix = emissions_matrix.T

    ## build model object
    starting_model = hmm(transitions_matrix, emissions_matrix)

    return(starting_model)


## test this:
'''
import snek_HMM as snek
transitions_matrix_file_name = "transitions_matrix.txt"
emissions_matrix_file_name = "emissions_matrix.txt"
my_model = snek.build_starting_model(transitions_matrix_file_name, emissions_matrix_file_name)
'''
