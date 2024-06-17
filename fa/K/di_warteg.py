class DI_WARTEG:
    def __init__(self):
        self.TABLE = {
            "q1": {
                "d":    "q2",
                "i":    "q11",
                " ":    "q11",
                "w":    "q11",
                "a":    "q11",
                "r":    "q11",
                "t":    "q11",
                "e":    "q11",
                "g":    "q11",
                "other":"q11",
                "EOS":  "error"     
            },
            "q2": {
                "d":    "q11",
                "i":    "q3",
                " ":    "q11",
                "w":    "q11",
                "a":    "q11",
                "r":    "q11",
                "t":    "q11",
                "e":    "q11",
                "g":    "q11",
                "other":"q11",
                "EOS":  "error"   
            },
            "q3": {
                "d":    "q11",
                "i":    "q11",
                " ":    "q4",
                "w":    "q11",
                "a":    "q11",
                "r":    "q11",
                "t":    "q11",
                "e":    "q11",
                "g":    "q11",
                "other":"q11",
                "EOS":  "error"     
            },
            "q4": {
                "d":    "q11",
                "i":    "q11",
                " ":    "q11",
                "w":    "q5",
                "a":    "q11",
                "r":    "q11",
                "t":    "q11",
                "e":    "q11",
                "g":    "q11",
                "other":"q11",
                "EOS":  "error"     
            },
            "q5": {
                "d":    "q11",
                "i":    "q11",
                " ":    "q11",
                "w":    "q11",
                "a":    "q6",
                "r":    "q11",
                "t":    "q11",
                "e":    "q11",
                "g":    "q11",
                "other":"q11",
                "EOS":  "error"      
            },
            "q6": {
                "d":    "q11",
                "i":    "q11",
                " ":    "q11",
                "w":    "q11",
                "a":    "q11",
                "r":    "q7",
                "t":    "q11",
                "e":    "q11",
                "g":    "q11",
                "other":"q11",
                "EOS":  "error"       
            },
            "q7": {
                "d":    "q11",
                "i":    "q11",
                " ":    "q11",
                "w":    "q11",
                "a":    "q11",
                "r":    "q11",
                "t":    "q8",
                "e":    "q11",
                "g":    "q11",
                "other":"q11",
                "EOS":  "error"      
            },
            "q8": {
                "d":    "q11",
                "i":    "q11",
                " ":    "q11",
                "w":    "q11",
                "a":    "q11",
                "r":    "q11",
                "t":    "q11",
                "e":    "q9",
                "g":    "q11",
                "other":"q11",
                "EOS":  "error"   
            },
            "q9": {
                "d":    "q11",
                "i":    "q11",
                " ":    "q11",
                "w":    "q11",
                "a":    "q11",
                "r":    "q11",
                "t":    "q11",
                "e":    "q11",
                "g":    "q10",
                "other":"q11",
                "EOS":  "error"   
            },
            "q10": {
                "d":    "q11",
                "i":    "q11",
                " ":    "q11",
                "w":    "q11",
                "a":    "q11",
                "r":    "q11",
                "t":    "q11",
                "e":    "q11",
                "g":    "q11",
                "other":"q11",
                "EOS":  "accept"   
            },
            "q11": {
                "d":    "q11",
                "i":    "q11",
                " ":    "q11",
                "w":    "q11",
                "a":    "q11",
                "r":    "q11",
                "t":    "q11",
                "e":    "q11",
                "g":    "q11",
                "other":"q11",
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
            elif char == "w":
                state = self.TABLE[state]["w"]
            elif char == "a":
                state = self.TABLE[state]["a"]
            elif char == "r":
                state = self.TABLE[state]["r"]
            elif char == "t":
                state = self.TABLE[state]["t"]
            elif char == "e":
                state = self.TABLE[state]["e"]
            elif char == "g":
                state = self.TABLE[state]["g"]
            elif char == "#":
                state = self.TABLE[state]["EOS"]
            else:
                 state = self.TABLE[state]["other"]
            
            if state == "error":
                return False
            elif state == "accept":
                return True
        return False