powers = {"w": 4, "p": 3, "b": 2, "s": 1, "m": -4, "q": -3, "d": -2, "z": -1}

def alphabet_war_1(fight):
    outcome = sum(powers[char] for char in fight)
    return 'Left side wins!' if outcome > 0 else 'Right side wins!' if outcome < 0 else 'Let\'s fight again!'

# Some interesting solutions to look at

# An interesting return statement taking the value where the key is true
def alphabet_war_2(fight):
    d = {'w':4,'p':3,'b':2,'s':1,
        'm':-4,'q':-3,'d':-2,'z':-1}
    r = sum(d[c] for c in fight if c in d)
    
    return {r==0:"Let's fight again!",
            r>0:"Left side wins!",
            r<0:"Right side wins!"
            }[True]

# This is great. result uses the index of each char, e.g. z would give 0 - -1 == 1, s => -1 - 0 == -1, b => -1 - 1 == -2, etc.
# The return is interesting too using format to conditional a single statement for any win.
def alphabet_war(fight):
    result = sum("zdqm".find(c) - "sbpw".find(c) for c in fight)
    return "{} side wins!".format("Left" if result < 0 else "Right") if result else "Let's fight again!"

print(alphabet_war("z"))
print(alphabet_war("zdqmwpbs"))
print(alphabet_war("zzzzs"))
print(alphabet_war("wwwwwwz"))