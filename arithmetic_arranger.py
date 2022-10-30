def arithmetic_arranger(problems, display_answer=False):
    total_prob = len(problems)
    
    if total_prob > 5:
        return "Error: Too many problems."

    prob_lst = [problem.split() for problem in problems]

    op1_lst = [problem[0] for problem in prob_lst]
    operators = [problem[1] for problem in prob_lst]
    op2_lst = [problem[2] for problem in prob_lst]

    for operator in operators:
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."

    try:
        int_op1 = [int(op) for op in op1_lst]
        int_op2 = [int(op) for op in op2_lst]
    except:
        return "Error: Numbers must only contain digits."

    op1_digits = [len(op) for op in op1_lst]
    op2_digits = [len(op) for op in op2_lst]

    if max(op1_digits + op2_digits) > 4:
        return "Error: Numbers cannot be more than four digits."
    
    spacing = [max(op1_digits[i], op2_digits[i]) + 1 for i in range(total_prob)]

    row1 = "    ".join([' ' + op1_lst[i].rjust(spacing[i]) for i in range(total_prob)]) 

    row2 = "    ".join([operators[i] + op2_lst[i].rjust(spacing[i]) for i in range(total_prob)]) 

    row3 = "    ".join(['-' * (spacing[i] + 1) for i in range(total_prob)])

    arranged_problems = '\n'.join([row1, row2, row3])

    if display_answer:
        answers = [int_op1[i] + int_op2[i] if operators[i] == '+' else int_op1[i] - int_op2[i] for i in range(total_prob)] 
        row4 = "    ".join([' ' + str(answers[i]).rjust(spacing[i]) for i in range(total_prob)]) 
        arranged_problems = '\n'.join([arranged_problems, row4])
    
    return arranged_problems
