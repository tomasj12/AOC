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
     
    def handle_input_dict(self, data):
        d = {f'col_{i}':[] for i in range(self.length_row)}
        for j in range(self.length_row):
            for i in range(len(data)):
                d[f'col_{j}'].append(data[i][j])
            
            d[f'col_{j}'] = ''.join(d[f'col_{j}'])
        
        return d
      
    def handle_input(self, decrease: bool=False) -> t.Tuple[str,str]:

        if decrease:
            most_common = self.input.copy()
            least_common = self.input.copy()
            most_common_dict = self.input_dict.copy()
            least_common_dict = self.input_dict.copy()
            for j in range(self.length_row):
                ct_most = Counter(most_common_dict[f'col_{j}']).most_common(2)
                most_ = ct_most[0][0] if ct_most[0][1] != ct_most[1][1] else '1'
                most_common = [line for line in most_common if line[j:].startswith(most_)]
                most_common_dict = self.handle_input_dict(most_common)

                if len(most_common) == 1:
                    break
                
            for j in range(self.length_row):
                ct_least = Counter(least_common_dict[f'col_{j}']).most_common(2)
                least_ = ct_least[-1][0] if ct_least[0][1] != ct_least[1][1] else '0'
                least_common = [line for line in least_common if line[j:].startswith(least_)]
                least_common_dict = self.handle_input_dict(least_common)

                if len(least_common) == 1:
                    break

        else:
            most_common = [Counter(self.input_dict[f'col_{j}']).most_common(1)[0][0] for j in range(self.length_row)]
            least_common = [Counter(self.input_dict[f'col_{j}']).most_common(self.length_row + 1)[-1][0] for j in range(self.length_row)]

        return ''.join(most_common),''.join(least_common)
        
        
    
        
    

