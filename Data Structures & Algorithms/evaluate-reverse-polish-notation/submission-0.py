
class Solution:
    @staticmethod
    def add(x:int, y:int):
        return x + y
    @staticmethod
    def diff(x:int, y:int):
        return x - y
    @staticmethod
    def mult(x:int, y:int):
        return x * y
    @staticmethod
    def div(x:int, y:int):
        return int(x/y)
    
    def evalRPN(self, tokens: List[str]) -> int:
        # we can use a "stack" to append both elements that will be subject
        #   to  a given operator. Once the operator is complete
        #   we pop off those two elements and store the next 

        # We will use a list to track the two values that will be subject to
        # to each operator. We will also use a dictionary to store operations.

        # If we use a dictionary, we have to be careful with the 

        list_stack = []

        operator_dict = {"+": Solution.add, "-": Solution.diff, "*": Solution.mult, "/": Solution.div}

        for i in tokens:
            if i in operator_dict.keys():
                # .pop() removes the last argument of the list (LIFO)
                y = list_stack.pop()
                x = list_stack.pop()
                result = operator_dict[i](x,y)
                list_stack.append(result)
            else:
                list_stack.append(int(i))
                print(i)
        
        return list_stack[0]
        

