class PARSER:
    def __init__(self):
        self.stack = []

    def push(self, sym):
        self.stack.append(sym)
        return self.stack

    def pop(self):
        if len(self.stack) == 0:
            return "The stack is empty"
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return "The stack is empty"
        return self.stack[-1]

    def valid(self, tokens):
        for token in tokens:
            if token == "error":
                return False
        
        self.stack = []
        self.stack.append("@")
        self.stack.append("S")

        top = self.peek()

        subjects = ["1", "2", "3", "4", "5"]
        predicates = ["6", "7", "8", "9", "10"]
        objects = ["11", "12", "13", "14", "15"]
        adverbs = ["16", "17", "18", "19", "20"]

        idx = 0
        sym = tokens[idx]

        # ["Ana", "membaca", "sampul", "di plaza"]

        while top != "@":
            if top == "S":
                if sym in subjects:
                    self.pop()
                    self.push("PP")
                    self.push("SU")
                else:
                    return False
            elif top == "SU":
                if sym in subjects:
                    self.pop()
                    self.push(sym)
                else:
                    return False
            elif top == "PP":
                if sym in predicates:
                    next_sym = tokens[idx + 1] if idx + 1 < len(tokens) else None
                    next_sym_2 = tokens[idx + 2] if idx + 2 < len(tokens) else None
                    if next_sym in objects and next_sym_2 in adverbs:
                        self.pop()  
                        self.push("K")  
                        self.push("O")  
                        self.push("P") 
                    elif next_sym in objects:
                        self.pop()  
                        self.push("O")  
                        self.push("P")  
                    elif next_sym in adverbs:
                        self.pop()  
                        self.push("K")  
                        self.push("P") 
                    else:
                        self.pop()  
                        self.push("P")  
                else:
                    return False

            elif top == "P":
                if sym in predicates:
                    self.pop()
                    self.push(sym)
                else:
                    return False
            elif top == "O":
                if sym in objects:
                    self.pop()
                    self.push(sym)
                else:
                    return False
            elif top == "K":
                if sym in adverbs:
                    self.pop()
                    self.push(sym)
                else:
                    return False
            else:
                lterm = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
                for term in lterm:
                    if top == term:
                        if top == sym:
                            self.pop()
                            idx += 1
                            sym = tokens[idx] if idx < len(tokens) else None
                        else:
                            return False         
            top = self.peek() 
            
            if top == "@":
                if sym != "#":
                    return False
                else:
                    state = "Finished"
        return state