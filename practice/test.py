# implement sliding window
from dataclasses import dataclass
@dataclass
class Attrs:
    s:str
    k:int
    n:int
    left:int
    right:int
   
def process():
    a = Attrs(s = "AABBBBAAA" , k = 2, n= len("AABBBBAAA"),left = 0, right = 0)
    
    def expand(a:Attrs)->bool:
        if a.right+1 <= a.n: 
            a.right+=1
            return True
        else:
            return False
            

    def contract(a:Attrs)->bool:
        if a.left<a.right:
            a.left+=1
            return True
        else:
            return False
            
    print(a.s[a.left:a.right+1])
    expand(a)
    print(a.s[a.left:a.right+1])
    contract(a)
    print(a.s[a.left:a.right+1])
    for i in range(100):
        expand(a)
    print(a.s[a.left:a.right+1])
process()