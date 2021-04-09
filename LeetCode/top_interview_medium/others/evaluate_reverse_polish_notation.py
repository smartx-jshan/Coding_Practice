class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    
        number_stack = []
        
        for token in tokens:
            if token == "+" or token == "*" or token == "/" or  token == "-": #계산해야하는 연산자가 들어오면
                
                second_operand = number_stack.pop() #두번째 피연산자를 꺼내기
                first_operand = number_stack.pop() #첫번째 피연산자 꺼내기
                if token == "+":
                    number_stack.append(first_operand + second_operand)
                elif token =="-":
                    number_stack.append(first_operand - second_operand)
                elif token =="*":
                    number_stack.append(first_operand * second_operand)
                elif token == "/":
                    number_stack.append(int(first_operand / second_operand))
        
            else: #피연산자들은 스택에 넣기
                number_stack.append (int(token))
                
        return number_stack.pop() #스택에 마지막에 남아있는것이 최종값
        
        
        
        
