# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 18:20:40 2022

@author: shubham joshi
data structure :Linked List 
"""

class Node :
    def __init__(self,value=None ):
        self.next=None 
        self.value=value 
      
class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def __iter__(self):
        """
        function to iterate over all the nodes
        """
        node=self.head
        while node:
            yield node # https://www.machinelearningplus.com/python/what-does-yield-keyword-do/
            node=node.next
            
    def insertLL(self,value,location):
        newNode=Node(value)
        
        if self.head==None:
            self.head=newNode
            self.tail=newNode
            
        else:
            if location ==0: # here the 0 represents at the beginning of the Linked list
                newNode.next=self.head 
                self.head=newNode
            
            elif location==-1: #here the 0 represents at the end of the Linked list
                self.tail.next=newNode
                newNode.next=None
                self.tail=newNode
                
                
            else:
                # To add node to a given location 
                tempNode=self.head 
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                    
                nextNode=tempNode.next 
                tempNode.next=newNode
                newNode.next=nextNode
                
                
                
    
Listobj=Linkedlist()   
Listobj.insertLL(1, -1) #[ 1]
Listobj.insertLL(2, -1) #[1,2]
Listobj.insertLL(3, -0) #[3,2,1]
Listobj.insertLL(4, 2)#[3,1,4,2]

print([node.value for node in Listobj])

 
        