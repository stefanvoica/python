from dataclasses import dataclass
from queue import PriorityQueue

@dataclass
class Element:
    start: int
    final: int

    def __lt__(self, other):
        return self.final < other.final

fin = open("spectacole.in")
pq = PriorityQueue()
n = int(fin.readline())
s = fin.readline()
while s != "":
    s = s.split()
    pq.put(Element(int(s[0]),int(s[1])))
    s = fin.readline()
fin.close()

nr = 0 #nr de spectacole
sol = []  #solutia finala
ts = 0 #timp sfarsit
while not pq.empty():
    vf = pq.get()
    if vf.start >= ts:
        ts = vf.final
        nr += 1 
        sol.append((vf.start, vf.final))
print (nr)
print (sol)