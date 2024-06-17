class DI_PASAR:
    def __init__(self):
        self.TABLE = {
            "q1": {
                "d":    "q2",
                "i":    "q10",
                " ":    "q10",
                "p":    "q10",
                "a":    "q10",
                "s":    "q10",
                "r":    "q10",
                "other":"q10",
                "EOS":  "error"     
            },
            "q2": {
                "d":    "q10",
                "i":    "q3",
                " ":    "q10",
                "p":    "q10",
                "a":    "q10",
                "s":    "q10",
                "r":    "q10",
                "other":"q10",
                "EOS":  "error"   
            },
            "q3": {
                "d":    "q10",
                "i":    "q10",
                " ":    "q4",
                "p":    "q10",
                "a":    "q10",
                "s":    "q10",
                "r":    "q10",
                "other":"q10",
                "EOS":  "error"     
            },
            "q4": {
                "d":    "q10",
                "i":    "q10",
                " ":    "q10",
                "p":    "q5",
                "a":    "q10",
                "s":    "q10",
                "r":    "q10",
                "other":"q10",
                "EOS":  "error"     
            },
            "q5": {
                "d":    "q10",
                "i":    "q10",
                " ":    "q10",
                "p":    "q10",
                "a":    "q6",
                "s":    "q10",
                "r":    "q10",
                "other":"q10",
                "EOS":  "error"      
            },
            "q6": {
                "d":    "q10",
                "i":    "q10",
                " ":    "q10",
                "p":    "q10",
                "a":    "q10",
                "s":    "q7",
                "r":    "q10",
                "other":"q10",
                "EOS":  "error"       
            },
            "q7": {
                "d":    "q10",
                "i":    "q10",
                " ":    "q10",
                "p":    "q10",
                "a":    "q8",
                "s":    "q10",
                "r":    "q10",
                "other":"q10",
                "EOS":  "error"      
            },
            "q8": {
                "d":    "q10",
                "i":    "q10",
                " ":    "q10",
                "p":    "q10",
                "a":    "q10",
                "s":    "q10",
                "r":    "q9",
                "other":"q10",
                "EOS":  "error"   
            },
            "q9": {
                "d":    "q10",
                "i":    "q10",
                " ":    "q10",
                "p":    "q10",
                "a":    "q10",
                "s":    "q10",
                "r":    "q10",
                "other":"q10",
                "EOS":  "accept"   
            },
            "q10": {
                "d":    "q10",
                "i":    "q10",
                " ":    "q10",
                "p":    "q10",
                "a":    "q10",
                "s":    "q10",
                "r":    "q10",
                "other":"q10",
                "EOS":  "error"   
            },
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
            elif char == "p":
                state = self.TABLE[state]["p"]
            elif char == "a":
                state = self.TABLE[state]["a"]
            elif char == "s":
                state = self.TABLE[state]["s"]
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