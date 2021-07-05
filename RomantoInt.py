# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 16:04:49 2020

@author: mecqu
"""
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """

    ans = 0 
    prev = len(s) - 2 
    after = len(s) - 1
    
    
    for n in range(len(s)-1,-1,-1):
        
        if s[n] == 'I' and (s[after] != 'V' and s[after] != 'X')  :
            ans += 1
         
    
        elif s[n] == 'I' and (s[after] == 'V' and s[after] == 'X')  : 
            continue 
            
        elif s[n] == 'V' and s[prev] == 'I':
            ans += 4
            
        elif s[n] == 'V':
            ans += 5
        
        elif s[n] == 'X' and s[prev] == 'I':
            ans += 9
        
        elif s[n] == 'X' and (s[after] != 'L' and s[after] != 'C')  :
            ans += 10
        
        elif s[n] == 'X' and (s[after] == 'L' and s[after] == 'C')  :
            
            continue 
        
        elif s[n] == 'L' and s[prev] == 'X':
            ans += 40
            
        elif s[n] == 'L':
            ans += 50
        
        elif s[n] == 'C' and s[prev] == 'X':
            ans += 90
    
        elif s[n] == 'C' and (s[after] != 'D' and s[after] != 'M')  :
            ans += 100
        
        elif s[n] == 'C' and (s[after] == 'D' and s[after] == 'M')  :
            
            continue 
        
        elif s[n] == 'D' and s[prev] == 'C':
            ans += 400
            
        elif s[n] == 'D':
            ans += 500
        
        elif s[n] == 'M' and s[prev] == 'C':
            ans += 900
        elif s[n] == 'M':
            ans += 1000
    
        
# My checks
        
        if n == len(s)-1:
            prev -= 1
        else:
            after -= 1
            prev -= 1
        
        if prev < 0:
            prev = 0
        
    return ans
            

print(romanToInt('MMMCDXC'))
            