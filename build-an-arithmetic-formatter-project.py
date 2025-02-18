def arithmetic_arranger(problems, show_answers=False):
    # Check if the number of problems is within the limit
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    first_line = []
    second_line = []
    dashes = []
    answers = []
    
    for problem in problems:
        parts = problem.split()
        if len(parts) != 3:
            return 'Error: Invalid problem format.'
        
        num1, operator, num2 = parts
        
        # Check if operator is valid
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        
        # Check if numbers are valid digits
        if not (num1.isdigit() and num2.isdigit()):
            return 'Error: Numbers must only contain digits.'
        
        # Check if numbers are within length limit
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        # Calculate the width needed
        width = max(len(num1), len(num2)) + 2
        
        # Prepare formatted strings
        first_line.append(num1.rjust(width))
        second_line.append(operator + num2.rjust(width - 1))
        dashes.append('-' * width)
        
        # Compute the answer if required
        if show_answers:
            result = str(eval(problem))  # Safe because input is validated
            answers.append(result.rjust(width))
    
    # Construct the arranged problems
    arranged_problems = '    '.join(first_line) + '\n' + '    '.join(second_line) + '\n' + '    '.join(dashes)
    
    if show_answers:
        arranged_problems += '\n' + '    '.join(answers)
    
    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
