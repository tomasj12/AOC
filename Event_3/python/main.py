from event_3 import *
from pathlib import Path

PATH_REPO = Path('/home/tomas/Personal projects/AOC')
PATH_DATA = PATH_REPO / 'Event_3' / 'Data' /'data.txt'

if __name__ == '__main__':

    init = EventThree(PATH_DATA)
    most_common,least_common = init.handle_input()
    print(int(most_common,base=2) * int(least_common, base=2))