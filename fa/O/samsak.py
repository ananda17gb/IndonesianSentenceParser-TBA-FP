class SAMSAK:
    def __init__(self):
        self.TABLE = {
            "q1": {
                "s":    "q2",
                "a":    "q8",
                "m":    "q8",
                "k":    "q8",
                "other":"q8",
                "EOS":  "error"     
            },
            "q2": {
                "s":    "q8",
                "a":    "q3",
                "m":    "q8",
                "k":    "q8",
                "other":"q8",
                "EOS":  "error"  
            },
            "q3": {
                "s":    "q8",
                "a":    "q8",
                "m":    "q4",
                "k":    "q8",
                "other":"q8",
                "EOS":  "error"    
            },
            "q4": {
                "s":    "q5",
                "a":    "q8",
                "m":    "q8",
                "k":    "q8",
                "other":"q8",
                "EOS":  "error"   
            },
            "q5": {
                "s":    "q8",
                "a":    "q6",
                "m":    "q8",
                "k":    "q8",
                "other":"q8",
                "EOS":  "error"    
            },
            "q6": {
                "s":    "q8",
                "a":    "q8",
                "m":    "q8",
                "k":    "q7",
                "other":"q8",
                "EOS":  "error"     
            },
            "q7": {
                "s":    "q8",
                "a":    "q8",
                "m":    "q8",
                "k":    "q8",
                "other":"q8",
                "EOS":  "accept"  
            },
            "q8": {
                "s":    "q8",
                "a":    "q8",
                "m":    "q8",
                "k":    "q8",
                "other":"q8",
                "EOS":  "error"    
            }
        }

    def valid(self, word):
        word += "#"  # Add EOS marker
        state = "q1"

        for char in word:
            if char == "s":
                state = self.TABLE[state]["s"]
            elif char == "a":
                state = self.TABLE[state]["a"]
            elif char == "m":
                state = self.TABLE[state]["m"]
            elif char == "k":
                state = self.TABLE[state]["k"]
            elif char == "#":
                state = self.TABLE[state]["EOS"]
            else:
                 state = self.TABLE[state]["other"]
            
            if state == "error":
                return False
            elif state == "accept":
                return True
        return False