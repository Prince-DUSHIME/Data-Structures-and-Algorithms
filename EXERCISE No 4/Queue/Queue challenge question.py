from collections import deque
# Q stands for queue
# append (enqueue)
# pop (popleft/remove from front)
# Start empty queue
Q = deque()

# Voters arrive: enqueued in arrival order
Q.append("Voter1")   # queue: Voter1 (front)
Q.append("Voter2")   # queue: Voter1, Voter2
Q.append("Voter3")   # queue: Voter1, Voter2, Voter3

# Serve voters in order of arrival
served = Q.popleft()  # serves Voter1 (front)
served = Q.popleft()  # serves Voter2 next

# Remaining front is now Voter3
# Each voter keeps their place when they arrive; no one served before earlier arrivals which is exactly FIFO.