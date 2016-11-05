# -*- coding: utf-8 -*-
"""
Created on Thu Nov 01 18:48:09 2016

@author: EllaNora
"""
# this dfa accepts strings starting with 0
#!/usr/bin/python
__metaclass__ = type
class DFA:
 def __init__(self):
     
     self.States=set()
     self.Sigma=set()
     self.DeltaTable={}
     self.StartState=''
     self.FinalStates=set()
     
 def setStates(self,S):
     self.States=S
     
 def setSigma(self,S):
      self.States=S
      
 def setStartState(self,s):
     self.StartState=s
     
 def setFinalStates(self,S):
     self.FinalStates=S
     
 def getStartState(self):
     return self.StartState;

 def getFinalStates(self):
     return self.FinalStates;
 
 def getStates(self):
     return self.States
     
 def getDeltaTable(self):
     return self.DeltaTable
 
 def setDeltaTable(self,delta):
     self.DeltaTable=delta
    

     
 def addTransition(self, from_state, symbol, end_state):
     if self.DeltaTable.has_key(from_state) :
        self.DeltaTable.get(from_state).add((symbol, end_state))
     else:
        self.DeltaTable[from_state] = set([(symbol, end_state)])

 def lookForToState(self, symbol, to_states):
     for s, q in to_states:
         if s == symbol:
             return q
         else:
             return None
         
 def delta(self, from_state, symbol):
     to_states = self.DeltaTable.get(from_state)
     ts = self.lookForToState(symbol, to_states)
     if ts == None:
         raise Exception('no transition on ' + symbol + ' from ' + from_state)
     else:
         return ts
         
 def isIn(self, x):
     curr_state = self.getStartState()
     for c in x:
         curr_state = self.delta(curr_state, c)
         return curr_state in self.getFinalStates()
 def printDFA(self):
     for x in self.DeltaTable:
         print(x),":" 
         for y in self.DeltaTable[x]:
             print "   ",('->'.join(y))
        
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

#Str = "011101"
#print "The passed string is: "+Str   
#print  "Result is ", m1.isIn(Str)
#print m1.DeltaTable
print m1.printDFA()

