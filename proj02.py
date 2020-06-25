# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 16:20:24 2020

@author: Benny
"""


dna= input('enter a DNA string: ')
dna2= input('enter another DNA string: ')
x = True
while x == True:
    command= input('what would you like to do?\na (add indel)\nd (delete indel)\ns (score alingment)\nq (quit): ')
    
    #add
    if command == 'a':
        stringchange= input('what string do you want to change?\n1\n2: ')
        if stringchange == '1':
            indexchange= input('at what index do you want to place the indel: ')
            if int(indexchange) >=0 and int(indexchange) < len(dna):
                dna= dna[:int(indexchange)] + '-' + dna[int(indexchange):len(dna)]
                dna2= dna2+ '-'
            else:
                print('error')
                     
        if stringchange == '2': 
            indexchange= input('at what index do you want to place the indel: ')
            if int(indexchange) >=0 and int(indexchange) < len(dna): 
                dna2= dna2[:int(indexchange)] + '-' + dna[int(indexchange):len(dna)]
                dna= dna + '-'
            else:
                print('error')
                
     #delete           
    elif command == 'd':
        deleteindel= input('what string do you want to delete from?\n1\n2: ')
        if deleteindel== '1':
            indexchange= input('what index do you want to delete from: ')
            if dna[int(indexchange)] == '-': 
                dna= dna[:int(indexchange)] + dna[int(indexchange)+1:len(dna)]
                dna2= dna2[:-1]
            else:
                print('error')
        if deleteindel== '2':
            indexchange= input('what index do you want to delete from: ')
            if dna2[int(indexchange)] == '-':
                 dna2= dna2[:int(indexchange)] + dna2[int(indexchange)+1:len(dna2)]
                 dna= dna[:-1]
            else:
                print('error')
    
    #score
    elif command == 's':
        matches= 0
        mismatches= 0
        while len(dna) != len(dna2):
            if len(dna) < len(dna2):
                dna= dna + '-'
            elif len(dna) > len(dna2):
                dna2= dna2 + '-'
        for i in range(len(dna)):
            if dna[i] != dna2[i]:
                mismatches= mismatches + 1
                dna= dna[:i] + dna[i].upper() + dna[i+1:]
                dna2= dna2[:i] + dna2[i].upper() + dna2[i+1:]  
            else:
                matches= matches + 1   
        print('matches:', matches)
        print('mismatches:', mismatches)
        print(dna)
        print(dna2)
    
    #quit
    elif command == 'q':
        print('end program')
        x = False
    else: 
        print('error')
        
        
                
                
                
        