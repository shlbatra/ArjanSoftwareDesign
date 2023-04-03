from dataclasses import dataclass, field

    
@dataclass
class A:
    _length: int = 0
    
def list_init():
    if l is None:
        return []
    else:
        return l
    
@dataclass
class B:
    x: int
    y: str = "hello"
    l: list[int] = field(default_factory=list_init(l))
    
@dataclass
class C:
    a: int = 3
    b: int = field(init=False) 
    
    def __post_init__(self):
        self.b = self.a + 3
        
if __name__ == '__main__':
    a = A()
    print(a)
    b = B(1)
    print(b)
    c = C()
    print(c)