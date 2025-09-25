 # S stands for Stack
# append is push (adds to top)
# pop (removes from top)
# Start empty stack
S = []             # Stack = []

# Push sequence
S.append("A")      # push "A" Stack = ["A"]
S.append("B")      # push "B" Stack = ["A","B"]
S.append("C")      # push "C" Stack = ["A","B","C"]
S.append("D")      # push "D" Stack = ["A","B","C","D"]   D is top

# Pop twice
S.pop()            # removes "D", S = ["A","B","C"]
S.pop()            # removes "C", S = ["A","B"]

# Result: Top now is "B"; remaining stack is ["A","B"].
