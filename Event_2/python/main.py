from event_2 import *
from pathlib import Path

PATH_REPO = Path('/home/tomas/Personal projects/AOC')
PATH_DATA = PATH_REPO / 'Event_2' / 'Data' /'data.txt'

if __name__ == '__main__':

    init = EventTwo(PATH_DATA)
    depth,height = init.handle_input(slinding_window=True)
    print(sum(depth) * sum(height))