def closing_parenthesis(sentence, opening_paren_index):
    open_nested_parens = 0

    for posiition in range(opening_paren_index + 1, len(sentence)):
        char = sentence[posiition]

        if char == '(':
            open_nested_parens +=1
        elif char == ')':
            if open_nested_parens == 0:
                return posiition
        else:
            open_nested_parens -= 1

    raise Exception