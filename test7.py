#! /usr/bin/env python
#coding:utf-8
from __future__ import division
import math

def quadratic_equation(a,b,c):
    if a==0:
        if b==0:
            if c==0:
                print("Nothing needs to be solved")
            else:
                print("Invalid equation!")    
        else:
            return str(-c)+'/'+str(b)
    else:
        delta=b*b-4*a*c
        if delta<0:
            x11=str(-b)+'+i*'+str(-delta)+'^(1/2)'
            x1='('+x11+')'+'/'+str(2*a)
            x21=str(-b)+'-i*'+str(-delta)+'^(1/2)'
            x2='('+x21+')'+'/'+str(2*a)
            return x1, x2
        elif delta==0:
            x='-'+str(b)+'/'+str(2*a)
            return x
        else:
            x11=str(-b)+'+'+str(delta)+'^(1/2)'
            x1='('+x11+')'+'/'+str(2*a)
            x21=str(-b)+'-'+str(delta)+'^(1/2)'
            x2='('+x21+')'+'/'+str(2*a)
            return x1, x2

if __name__=='__main__':
    print('a quadratic equation:x^2+x+1=0')
    coefficients=(8,4,1)
    roots=quadratic_equation(*coefficients)
    print('the result is:',roots)
