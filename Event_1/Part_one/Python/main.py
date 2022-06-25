from event_1 import *
from pathlib import Path

PATH_REPO = Path('/home/tomas/Personal projects/AOC')
PATH_DATA = PATH_REPO / 'Event_1' / 'Data' /'data.txt'

if __name__ == '__main__':

    init = EventOne(PATH_DATA)
    data_output = init.handle_input(slinding_window=True)
    print(sum(data_output))