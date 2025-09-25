# Queue practical 1
from collections import deque
q = deque(["P1","P2","P3","P4","P5","P6","P7"])
print("Initial queue:", list(q))

# Serve 4 people (dequeue 4 times)
for _ in range(4):
    q.popleft()

print("Queue after serving 4:", list(q))
print("Who is at front now?", q[0])

#Queue practical 2 
from collections import deque
q = deque(["C1","C2","C3","C4","C5"])
print("Initial queue:", list(q))

first = q.popleft()
second = q.popleft()

print("First served:", first)
print("Second served:", second)
