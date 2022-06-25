import typing as t
import abc
from pathlib import Path
import collections.abc as tc


### Types
B = t.TypeVar('B', bound=bool)

# TODO: Create class for input handler, where
# method handle_input will be abstract method 
class InputHandler(abc.ABC):
    
    def __init__(self,path: Path) -> None:
        
        self.path = path

        with open(self.path, 'r') as file:
            self.input = file.readlines()
            self.input = [int(x.rstrip('\n')) for x in self.input]
    
    @abc.abstractmethod
    def handle_input(self):
        pass
    


class EventOne(InputHandler):
     
     def handle_input(self, slinding_window: bool=False) -> t.Sequence[B]:
         
        if slinding_window:
            self.input = [
                sum(self.input[i - 3:i]) for i in range(3,len(self.input) + 1)
            ]

        res = [
                self.input[i] > self.input[i-1] for i in range(1,len(self.input))
            ]

        return res

    
        
    

