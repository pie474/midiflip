__author__ = 'chinmay'

import midi
from midi import fileio

import pprint
x = midi.FileReader()
p = midi.read_midifile('mary.mid')
print p
raw_input()
midi.write('aa.mid', p)
p = midi.read('aa.mid')
print p
raw_input()
#midi.write('aaa.mid', p)
#p = midi.read('aaa.mid')