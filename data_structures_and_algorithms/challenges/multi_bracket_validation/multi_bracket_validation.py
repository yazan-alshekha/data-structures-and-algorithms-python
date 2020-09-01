def multi_bracket_validation(input):
    '''
    function to ensure matching between opening (,{,[ and ],},)

    input-> '[(any value of string)]'
    output-> true if matching parentheses  or the reason of error

    '''

    brackets1=input.count('[')
    brackets2=input.count(']')

    curly1=input.count('{')
    curly2=input.count('}')
    
    parentheses1=input.count('(')
    parentheses2=input.count(')')

   
    
    if len(input)==0:
        return 'empty input'
    
    elif parentheses1 != parentheses2:
        if parentheses1> parentheses2:
            return 'error unmatched opening ( remaining.'
        else:
             return 'error unmatched closing )'     
 
 
    elif curly1 != curly2:
        if curly1>curly2:
            return 'error unmatched opening { remaining.'
        else:
            return  'error unmatched closing }'    
   
   
   
    elif brackets1 != brackets2:
        if brackets1>brackets2:
            return 'error unmatched opening [ remaining.'
        else:
            return 'error unmatched closing ]' 
    
   
    else:
        return True

if __name__ == "__main__":
    print(multi_bracket_validation('[(function should return true])'))

