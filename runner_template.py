import random as r, string as s
r.seed(S)
p=L
q=[r.choice(s.printable)for _ in range(max(p)+1)]
exec(''.join([q[x]for x in p]))