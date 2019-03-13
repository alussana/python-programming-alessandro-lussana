#!/usr/bin/python2

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import os, binascii

class Organism(object):
    def __init__(self, name, genome, coordinates):
        self.name = name
        self.genome = genome
        self.coordinates = coordinates

def spawn_organism(name, env_coord):
    genome = binascii.b2a_hex(os.urandom(15))
    organism = Organism(name, genome, coordinates)