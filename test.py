import random as r, string as s
r.seed(123)
p=[250, 303, 37, 78, 104, 117, 9, 1, 97, 84, 97, 9, 87, 76, 80, 206, 100, 206, 82, 58, 42, 206, 39, 42, 206, 157, 174, 76, 250, 303, 37, 78, 104, 117, 236, 178, 119, 117, 80, 87, 87, 76]
q=[r.choice(s.printable)for _ in range(max(p)+1)]
exec(''.join([q[x]for x in p]))