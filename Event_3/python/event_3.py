import typing as t
import abc
from pathlib import Path
import collections.abc as tc
import itertools as it
from collections import Counter

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
            self.input = [line.rstrip('\n') for line in self.input]
    
    @abc.abstractmethod
    def handle_input(self):
        pass
    

class EventThree(InputHandler):

    def __init__(self, path: Path) -> None:
        super().__init__(path)
        self.length_row = len(self.input[0])
        self.input_dict = {f'col_{i}':[] for i in range(self.length_row)}
        
        for j in range(self.length_row):
            for i in range(len(self.input)):
                self.input_dict[f'col_{j}'].append(self.input[i][j])
            
            self.input_dict[f'col_{j}'] = ''.join(self.input_dict[f'col_{j}'])
     
    def handle_input(self) -> t.Tuple[t.List[int],t.List[int]]:

        most_common = [Counter(self.input_dict[f'col_{j}']).most_common(1)[0][0] for j in range(self.length_row)]
        least_common = [Counter(self.input_dict[f'col_{j}']).most_common(self.length_row + 1)[-1][0] for j in range(self.length_row)]

        return ''.join(most_common),''.join(least_common)
        
        
    
        
    

