from array import array
a = array('H', [4000, 10, 700, 22222])
sum(a)
26932 #output
a[1:3]
array('H', [10, 700]) #output


from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())
Handling task1 #output