class DI_PLAZA:
    def __init__(self):
        self.TABLE = {
            "q1": {
                "d":    "q2",
                "i":    "q10",
                " ":    "q10",
                "p":    "q10",
                "l":    "q10",
                "a":    "q10",
                "z":    "q10",
                "other":"q10",
                "EOS":  "error"     
            },
            "q2": {
                "d":    "q10",
                "i":    "q3",
                " ":    "q10",
                "p":    "q10",
                "l":    "q10",
                "a":    "q10",
                "z":    "q10",
                "other":"q10",
                "EOS":  "error"   
            },
            "q3": {
                "d":    "q10",
                "i":    "q10",
                " ":    "q4",
                "p":    "q10",
                "l":    "q10",
                "a":    "q10",
                "z":    "q10",
                "other":"q10",
                "EOS":  "error"     
            },
            "q4": {
                "d":    "q10",
                "i":    "q10",
                " ":    "q10",
                "p":    "q5",
                "l":    "q10",
                "a":    "q10",
                "z":    "q10",
                "other":"q10",
                "EOS":  "error"     
            },
            "q5": {
                "d":    "q10",
                "i":    "q10",
                " ":    "q10",
                "p":    "q10",
                "l":    "q6",
                "a":    "q10",
                "z":    "q10",
                "other":"q10",
                "EOS":  "error"      
            },
            "q6": {
                "d":    "q10",
                "i":    "q10",
                " ":    "q10",
                "p":    "q10",
                "l":    "q10",
                "a":    "q7",
                "z":    "q10",
                "other":"q10",
                "EOS":  "error"       
            },
            "q7": {
                "d":    "q10",
                "i":    "q10",
                " ":    "q10",
                "p":    "q10",
                "l":    "q10",
                "a":    "q10",
                "z":    "q8",
                "other":"q10",
                "EOS":  "error"      
            },
            "q8": {
                "d":    "q10",
                "i":    "q10",
                " ":    "q10",
                "p":    "q10",
                "l":    "q10",
                "a":    "q9",
                "z":    "q10",
                "other":"q10",
                "EOS":  "error"   
            },
            "q9": {
                "d":    "q10",
                "i":    "q10",
                " ":    "q10",
                "p":    "q10",
                "l":    "q10",
                "a":    "q10",
                "z":    "q10",
                "other":"q10",
                "EOS":  "accept"   
            },
            "q10": {
                "d":    "q10",
                "i":    "q10",
                " ":    "q10",
                "p":    "q10",
                "l":    "q10",
                "a":    "q10",
                "z":    "q10",
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
            elif char == "l":
                state = self.TABLE[state]["l"]
            elif char == "a":
                state = self.TABLE[state]["a"]
            elif char == "z":
                state = self.TABLE[state]["z"]
            elif char == "#":
                state = self.TABLE[state]["EOS"]
            else:
                 state = self.TABLE[state]["other"]
            
            if state == "error":
                return False
            elif state == "accept":
                return True
        return False