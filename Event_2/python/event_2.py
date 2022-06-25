import typing as t
import abc
from pathlib import Path
import collections.abc as tc
import itertools as it

### Types
Depth = t.TypeVar('Depth', bound=int)
Height = t.TypeVar('Height', bound=int)

# TODO: Create class for input handler, where
# method handle_input will be abstract method 
class InputHandler(abc.ABC):
    
    def __init__(self,path: Path) -> None:
        
        self.path = path

        with open(self.path, 'r') as file:
            self.input = file.readlines()
            self.input = [line.rstrip('\n').split(' ') for line in self.input]
    
    @abc.abstractmethod
    def handle_input(self):
        pass
    

class EventTwo(InputHandler):

     def __init__(self, path: Path) -> None:
         super().__init__(path)
         self.mapping = {'forward': 1, 'down': 1,'up':-1}
     
     def handle_input(self, aim_: bool=False) -> t.Tuple[t.Sequence[Depth],t.Sequence[Height]]:
        
        height = [int(d[1]) if d[0] == 'forward' else 0 for d in self.input]

        if aim_:
            aim = [self.mapping[d[0]] * int(d[1])  if d[0] != 'forward' else 0 for d in self.input]
            aim = list(it.accumulate(aim))
            depth = [h * a for h,a in zip(height,aim)]
        else:
            depth = [self.mapping[d[0]] * int(d[1])  if d[0] != 'forward' else 0 for d in self.input]

        return depth, height
    
        
    

