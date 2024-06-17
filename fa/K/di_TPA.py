class DI_TPA:
    def __init__(self):
        self.TABLE = {
            "q1": {
                "d":    "q2",
                "i":    "q8",
                " ":    "q8",
                "T":    "q8",
                "P":    "q8",
                "A":    "q8",
                "other":"q8",
                "EOS":  "error"     
            },
            "q2": {
                "d":    "q8",
                "i":    "q3",
                " ":    "q8",
                "T":    "q8",
                "P":    "q8",
                "A":    "q8",
                "other":"q8",
                "EOS":  "error"  
            },
            "q3": {
                "d":    "q8",
                "i":    "q8",
                " ":    "q4",
                "T":    "q8",
                "P":    "q8",
                "A":    "q8",
                "other":"q8",
                "EOS":  "error"    
            },
            "q4": {
                "d":    "q8",
                "i":    "q8",
                " ":    "q8",
                "T":    "q5",
                "P":    "q8",
                "A":    "q8",
                "other":"q8",
                "EOS":  "error"   
            },
            "q5": {
                "d":    "q8",
                "i":    "q8",
                " ":    "q8",
                "T":    "q8",
                "P":    "q6",
                "A":    "q8",
                "other":"q8",
                "EOS":  "error"    
            },
            "q6": {
                "d":    "q8",
                "i":    "q8",
                " ":    "q8",
                "T":    "q8",
                "P":    "q8",
                "A":    "q7",
                "other":"q8",
                "EOS":  "error"     
            },
            "q7": {
                "d":    "q8",
                "i":    "q8",
                " ":    "q8",
                "T":    "q8",
                "P":    "q8",
                "A":    "q8",
                "other":"q8",
                "EOS":  "accept"  
            },
            "q8": {
                "d":    "q8",
                "i":    "q8",
                " ":    "q8",
                "T":    "q8",
                "P":    "q8",
                "A":    "q8",
                "other":"q8",
                "EOS":  "error"    
            }
        }

    def valid(self, word):
        word += "#"  # Add EOS marker
        state = "q1"

        for char in word:
            if char == "d":
                state = self.TABLE[state]["d"]
            elif char == "i":
                state = self.TABLE[state]["i"]
            elif char == " ":
                state = self.TABLE[state][" "]
            elif char == "T":
                state = self.TABLE[state]["T"]
            elif char == "P":
                state = self.TABLE[state]["P"]
            elif char == "A":
                state = self.TABLE[state]["A"]
            elif char == "#":
                state = self.TABLE[state]["EOS"]
            else:
                 state = self.TABLE[state]["other"]
            
            if state == "error":
                return False
            elif state == "accept":
                return True
        return False