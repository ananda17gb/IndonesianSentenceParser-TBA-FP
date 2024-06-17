class MEMBELI:
    def __init__(self):
        self.TABLE = {
            "q1": {
                "m":    "q2",
                "e":    "q9",
                "b":    "q9",
                "l":    "q9",
                "i":    "q9",
                "other":"q9",
                "EOS":  "error"     
            },
            "q2": {
                "m":    "q9",
                "e":    "q3",
                "b":    "q9",
                "l":    "q9",
                "i":    "q9",
                "other":"q9",
                "EOS":  "error"  
            },
            "q3": {
                "m":    "q4",
                "e":    "q9",
                "b":    "q9",
                "l":    "q9",
                "i":    "q9",
                "other":"q9",
                "EOS":  "error"     
            },
            "q4": {
                "m":    "q9",
                "e":    "q9",
                "b":    "q5",
                "l":    "q9",
                "i":    "q9",
                "other":"q9",
                "EOS":  "error"   
            },
            "q5": {
                "m":    "q9",
                "e":    "q6",
                "b":    "q9",
                "l":    "q9",
                "i":    "q9",
                "other":"q9",
                "EOS":  "error"     
            },
            "q6": {
                "m":    "q9",
                "e":    "q9",
                "b":    "q9",
                "l":    "q7",
                "i":    "q9",
                "other":"q9",
                "EOS":  "error"     
            },
            "q7": {
                "m":    "q9",
                "e":    "q9",
                "b":    "q9",
                "l":    "q9",
                "i":    "q8",
                "other":"q9",
                "EOS":  "error"     
            },
            "q8": {
                "m":    "q9",
                "e":    "q9",
                "b":    "q9",
                "l":    "q9",
                "i":    "q9",
                "other":"q9",
                "EOS":  "accept"     
            },
            "q9": {
                "m":    "q9",
                "e":    "q9",
                "b":    "q9",
                "l":    "q9",
                "i":    "q9",
                "other":"q9",
                "EOS":  "error" 
            }
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
            elif char == "e":
                state = self.TABLE[state]["e"]
            elif char == "l":
                state = self.TABLE[state]["l"]
            elif char == "i":
                state = self.TABLE[state]["i"]
            elif char == "#":
                state = self.TABLE[state]["EOS"]
            else:
                 state = self.TABLE[state]["other"]
            
            if state == "error":
                return False
            elif state == "accept":
                return True
        return False