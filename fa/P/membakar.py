class MEMBAKAR:
    def __init__(self):
        self.TABLE = {
            "q1": {
                "m":    "q2",
                "e":    "q10",
                "b":    "q10",
                "a":    "q10",
                "k":    "q10",
                "r":    "q10",
                "other":"q10",
                "EOS":  "error"
            },
            "q2": {
                "m":    "q10",
                "e":    "q3",
                "b":    "q10",
                "a":    "q10",
                "k":    "q10",
                "r":    "q10",
                "other":"q10",
                "EOS":  "error"    
            },
            "q3": {
                "m":    "q4",
                "e":    "q10",
                "b":    "q10",
                "a":    "q10",
                "k":    "q10",
                "r":    "q10",
                "other":"q10",
                "EOS":  "error"    
            },
            "q4": {
                "m":    "q10",
                "e":    "q10",
                "b":    "q5",
                "a":    "q10",
                "k":    "q10",
                "r":    "q10",
                "other":"q10",
                "EOS":  "error"    
            },
            "q5": {
                "m":    "q10",
                "e":    "q10",
                "b":    "q10",
                "a":    "q6",
                "k":    "q10",
                "r":    "q10",
                "other":"q10",
                "EOS":  "error"    
            },
            "q6": {
                "m":    "q10",
                "e":    "q10",
                "b":    "q10",
                "a":    "q10",
                "k":    "q7",
                "r":    "q10",
                "other":"q10",
                "EOS":  "error"     
            },
            "q7": {
                "m":    "q10",
                "e":    "q10",
                "b":    "q10",
                "a":    "q8",
                "k":    "q10",
                "r":    "q10",
                "other":"q10",
                "EOS":  "error"     
            },
            "q8": {
                "m":    "q10",
                "e":    "q10",
                "b":    "q10",
                "a":    "q10",
                "k":    "q10",
                "r":    "q9",
                "other":"q10",
                "EOS":  "error"    
            },
            "q9": {
                "m":    "q10",
                "e":    "q10",
                "b":    "q10",
                "a":    "q10",
                "k":    "q10",
                "r":    "q10",
                "other":"q10",
                "EOS":  "accept"     
            },
            "q10": {
                "m":    "q10",
                "e":    "q10",
                "b":    "q10",
                "a":    "q10",
                "k":    "q10",
                "r":    "q10",
                "other":"q10",
                "EOS":  "error"    
            },
        }

    def valid(self, word):
        word += "#"  # Add EOS marker
        state = "q1"

        for char in word:
            if char == "m":
                state = self.TABLE[state]["m"]
            elif char == "e":
                state = self.TABLE[state]["e"]
            elif char == "b":
                state = self.TABLE[state]["b"]
            elif char == "a":
                state = self.TABLE[state]["a"]
            elif char == "k":
                state = self.TABLE[state]["k"]
            elif char == "r":
                state = self.TABLE[state]["r"]
            elif char == "#":
                state = self.TABLE[state]["EOS"]
            else:
                 state = self.TABLE[state]["other"]
            
            if state == "error":
                return False
            elif state == "accept":
                return True
        return False