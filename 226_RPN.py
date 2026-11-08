
# evaluate reverse polish notation.
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

def evalRPN(tokens: list[str]) -> int:

    def isOperator(token: str) -> bool:
        return token in "+-*/"
    
    def operate(value1: int|float, operator: str, value2: int|float) -> int|float:
        match operator:
            case "+":
                return value1 + value2
            case "-":
                return value1 - value2
            case "*":
                return value1 * value2
            case "/":
                return value1 / value2
    
    memory = []
    for token in tokens:

        # add a value in memory.
        if not isOperator(token):
            memory.append(int(token))
            continue

        # operate.
        value2 = memory.pop()
        value1 = memory.pop()
        memory.append(int(operate(value1, token, value2)))

    return memory[0]



print(evalRPN(["2","1","+","3","*"]))  # 9.
print(evalRPN(["4","13","5","/","+"]))  # 6.  (or 6.6 without round).
print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))  # 22.  (or 21.545454... without round).


# ------ example ------
#
#34+2×
#
#La lecture se fait ainsi :
#On lit 3 : on le mémorise.
#On lit 4 : on le mémorise également.
#On lit + : on additionne les deux derniers nombres, donc 3+4=7
#On lit 2 : on le mémorise.
#On lit × : on multiplie les deux derniers résultats, donc 7×2=14