def pyramids(n):
    floors = []
    print(" /\\\n/__\\\n")
    for i in range(1, n):
        outside = n - i
        inside = (i - 1) * 2
        floors.append(f"{' ' * outside}/{' ' * inside}\\\n")
    ground = (n - 1) * 2
    floors.append(f"/{'_' * ground}\\\n")
    return ''.join(floors)

# from codewars solutions

def pyramid(n):
    return '\n'.join("/{}\\".format(" _"[r==n-1] * r*2).center(2*n).rstrip() for r in range(n)) + '\n'

def pyramid(n):
    return "".join(f"{' ' * (n - i - 1)}/{(' ' if i < (n - 1) else '_') * i * 2}\\\n" for i in range(n))

pyramid = lambda n: "\n".join( (n-i-1)*' ' + '/' + 2*i*(' ' if i<n-1 else '_') + '\\' for i in range(n)) + '\n'

