#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 09:13:26 2023

@author: ethanpeacock
"""
my_file = open('power.txt', 'w')
print( " N \t\t2**N\t\t3**N" )                # print labels for columns.
print( "---\t\t----\t\t----")                 # print separator
my_file.write( " N \t\t2**N\t\t3**N\n" )        # write labels to file
my_file.write( "---\t\t----\t\t----\n")         # write separator to file
#%% Loop over integers from 0 to 10 and print/write results
for N in range(11):
    print( "{:d}\t\t{:d}\t\t{:d}".format(N, pow(2, N), pow(3, N)) )
    my_file.write( "{:d}\t\t{:d}\t\t{:d}\n".format(N, pow(2, N), pow(3, N)) )
my_file.close()
