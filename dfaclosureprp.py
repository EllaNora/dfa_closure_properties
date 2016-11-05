# -*- coding: utf-8 -*-
"""
Created on Thu Nov 03 23:40:35 2016

@author: EllaNora
"""

from demodfa import DFA

alphabet = set(['0', '1'])
m1 = DFA()
m1.setSigma(alphabet)
m1.setStates(set(['q0', 'q1', 'q2']))
m1.setStartState('q0')
m1.setFinalStates(set(['q1']))
m1.addTransition('q0', '0', 'q1')
m1.addTransition('q0', '1', 'q2')
m1.addTransition('q1', '0', 'q1')
m1.addTransition('q1', '1', 'q1')
m1.addTransition('q2', '0', 'q2')
m1.addTransition('q2', '1', 'q2')

m2 = DFA()
m2.setSigma(alphabet)
m2.setStates(set(['q0', 'q1', 'q2']))
m2.setStartState('q0')
m2.setFinalStates(set(['q2']))
m2.addTransition('q0', '0', 'q1')
m2.addTransition('q0', '1', 'q2')
m2.addTransition('q1', '0', 'q1')
m2.addTransition('q1', '1', 'q1')
m2.addTransition('q2', '0', 'q2')
m2.addTransition('q2', '1', 'q2')

def Complement(DFA):
    final = DFA.getFinalStates()
    states = DFA.getStates()
    temp=states.difference(final)
   # print temp
    m1.setFinalStates(temp)
    # print m1.getFinalStates()

def Union(dfa1, dfa2):
    newDFA = DFA()
   
    newDFA.setSigma(alphabet)
    newDFA.setStates(set(['q0', 'q1', 'q2']))
    A = dfa1.getDeltaTable()
    A.update(dfa2.getDeltaTable()
    newDFA.setDeltaTable(**A)   #ERROR
    f1 = dfa1.getFinalStates()
    f2 = dfa2.getFinalStates()
    dfafinal = (f1).union(f2)
    newDFA.setFinalStates(dfafinal)
    newDFA.printDFA()
    
Complement(m1)
Union(m1,m2)
m1.isIn("0111")