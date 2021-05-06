"""
You must not import any modules.
PLEASE REMOVE print functions, if any,
while passing to the next question and evaluating.
The usage of input(), map(), reduce(), filter() functions is strictly forbidden.
The usage of iteration (for, while, and list/set comprehension) is strictly forbidden.
If need be,  you can use dir and help functions to look at the available functions and their
descriptions for each data type.
"""
def decode_and_execute(mem,ins):
    instructions = ["CLRMEM","SUB","LOAD","SUBI","DIVI"]
    ls = ins.split()
    instr = ls[0]
    if instr not in instructions:
        return ["UNKNOWN INSTRUCTION"]
    elif instr == "CLRMEM":
        mem = [0] * 10
        return ["NO ERROR"]
    elif instr == "SUB":
        num1 = ls[1][:-1]
        num2 = ls[2]
        errors = []
        if num1.isdigit() == False or int(num1) < 0 or int(num1) > 9:
            errors.append("INVALID ADDRESS")
        if num2.isdigit() == False or int(num2) < 0 or int(num2) > 9:
            errors.append("INVALID ADDRESS")
        if (num1.isdigit() == True and int(num1) >= 0 and int(num1) <= 9) and (num2.isdigit() == True and int(num2) >= 0 and int(num2) <= 9):
            errors.append("NO ERROR")
            mem[int(num1)] -= mem[int(num2)]
        return errors
    elif instr == "LOAD":
        num1 = ls[1][:-1]
        num2 = ls[2]
        errors = []
        if num1.isdigit() == False or int(num1) < 0 or int(num1) > 9:
            errors.append("INVALID ADDRESS")
        if num2.isdigit() == False:
            errors.append("NOT A NUMBER")
        if (num1.isdigit() == True and int(num1) >= 0 and int(num1) <= 9) and (num2.isdigit() == True):
            errors.append("NO ERROR")
            mem[int(num1)] = int(num2)
        return errors
    elif instr == "SUBI":
        num1 = ls[1][:-1]
        num2 = ls[2]
        errors = []
        if num1.isdigit() == False or int(num1) < 0 or int(num1) > 9:
            errors.append("INVALID ADDRESS")
        if num2.isdigit() == False:
            errors.append("NOT A NUMBER")
        if (num1.isdigit() == True and int(num1) >= 0 and int(num1) <= 9) and (num2.isdigit() == True):
            errors.append("NO ERROR")
            mem[int(num1)] -= int(num2)
        return errors
    elif instr == "DIVI":
        num1 = ls[1][:-1]
        num2 = ls[2]
        errors = []
        if num1.isdigit() == False or int(num1) < 0 or int(num1) > 9:
            errors.append("INVALID ADDRESS")
        if num2 == "0":
            errors.append("DIVISION BY ZERO")
        if num2.isdigit() == False:
            errors.append("NOT A NUMBER")
        if (num1.isdigit() == True and int(num1) >= 0 and int(num1) <= 9) and (num2.isdigit() == True and num2 != "0"):
            errors.append("NO ERROR")
            mem[int(num1)] = mem[int(num1)] / int(num2)
        return errors