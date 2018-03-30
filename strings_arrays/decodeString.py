def decodeString(s):
    curr_str_list = []
    idx = 0
    while idx < len(s):
        # might be an unrepeated letter
        if ord('a') <= ord(s[idx]) <= ord('z'):
            curr_str_list.append(s[idx])
            idx += 1
        # must be a number
        else:
            # built the number
            curr_num_list = []
            while ord('0') <= ord(s[idx]) <= ord('9'):
                curr_num_list.append(s[idx])
                idx += 1
            # have built the number, will currently be on an opening bracket
            curr_num = int("".join(curr_num_list))
            # begin with the opening bracket
            curr_expr_bracket_count = 1
            full_expr = [s[idx]]
            idx += 1
            while curr_expr_bracket_count > 0:
                if s[idx] == "[":
                    curr_expr_bracket_count += 1
                elif s[idx] == "]":
                    curr_expr_bracket_count -= 1
                full_expr += s[idx]
                idx += 1
            # exclude the brackets and evaluate
            inner_expr_str = decodeString("".join(full_expr[1:-1]))
            curr_str_list.append(curr_num * inner_expr_str)
    return "".join(curr_str_list)

print(decodeString("3[a]2[bc]"))