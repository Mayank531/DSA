
def is_valid_parenthesis(str):
    stack =[]
    for bracket in str:

        if(bracket=='(' or bracket=='{' or bracket=='['):
            stack.append(bracket)
        else:
            if(len(stack)==0):
                return False
            opening = stack.pop()
            if((opening=="("  and bracket==')') or (opening=='{' and bracket=='}') or (opening=='[' and bracket==']')):
                continue
            else:
                return False
            
    return len(stack)==0

print(is_valid_parenthesis("())(({})){[]}("))

    
