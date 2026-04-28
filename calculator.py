a = input("")
def solve(expr):
    l = []
    p = []
    num = ""
    for ch in expr:
        if ch in ["+", "-", "*", "/", "="]:
            if num != "":
                l.append(int(num))
            num = ""
            p.append(ch)
        else:
            num += ch

    if num != "":
        l.append(int(num))

    if "=" in p:
        p.remove("=")

    i = 0
    while i < len(p):
        if p[i] == "/":
            val = l[i] / l[i+1]
            l[i:i+2] = [val]
            del p[i]
        elif p[i] == "*":
            val = l[i] * l[i+1]
            l[i:i+2] = [val]
            del p[i]
        else:
            i += 1

    i = 0
    while i < len(p):
        if p[i] == "-":
            val = l[i] - l[i+1]
            l[i:i+2] = [val]
            del p[i]
        elif p[i] == "+":
            val = l[i] + l[i+1]
            l[i:i+2] = [val]
            del p[i]
        else:
            i += 1

    return l[0]

while "(" in a:
    e = a.rindex("(")          
    f = a.index(")", e)        

    sub_expr = a[e+1:f]        
    result = solve(sub_expr)   

    a = a[:e] + str(result) + a[f+1:]   # replace

print(solve(a))