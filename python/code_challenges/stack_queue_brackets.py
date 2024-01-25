
def multi_bracket_validation(input_string):
    # Initialize empty stack
    stack = []
    # define sets of brackets for matching the input
    opening_brackets = ['(', '[', '{']
    closing_brackets = {')' : '(', ']' : '[', '}' : '{'}
    # iterate through each character in the input
    for character in input_string:
        # check if the character is in the opening_brackets
        if character in opening_brackets:
            # if it is push it to the stack initialized above.
            stack.append(character)
        # check if the character is in the closing_brackets
        elif character in closing_brackets:
        # Check if the stack is not empty and the top of the stack matches the corresponding opening bracket
            if not stack or stack.pop() != closing_brackets[character]:
                return False

    return True




