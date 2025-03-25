while True:
    sentence = input()
    if sentence == '.':
        break

    stack = []
    is_valid = True

    for ch in sentence:
        if ch in '([':
            stack.append(ch)
        elif ch in ')]':
            if not stack:
                is_valid = False
                break
            top = stack.pop()
            if (ch == ')' and top != '(') or (ch == ']' and top != '['):
                is_valid = False
                break
    
    if is_valid and not stack:
        print('yes')
    else:
        print('no')
