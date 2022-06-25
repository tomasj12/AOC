import typing as t
import abc


# TODO: Create class for input handler, where
# method handle_input will be abstract method 
class InputHandler(abc.ABC):
    
    def __init__(self,path: str) -> None:
        
        self.path = path

        with open(self.path, 'r') as file:
            self.input = file.readlines()
    
    @abc.abstractmethod
    def handle_input(self):
        pass


class EventOne(InputHandler):
     
     def handle_input(self):
         pass

test = EventOne('/home/tomas/Personal projects/Advent of Code/Event 1/data.txt')
print(test.input)        
    
    
        
    

