"""Test boards for Connect383

Place test boards in this module to help test your code.  Note that since connect383.GameState
stores board contents as a 0-based list of lists, these boards are reversed to they can be written
right side up here.

"""

boards = {}  # dictionary with label, test board key-value pairs

boards['choose_right'] = reversed([  
    [  0,  0 ],                       
    [ -1,  1 ],
    [ -1,  1 ] 
])

boards['choose_middle'] = reversed([  
    [ -1,  0,  0,  -1, -1 ],  
    [ -1,   1, -1,  1,  1 ],
    [  1,  -1,  1, -1,  1 ],
    [  1,   1, -1,  1, -1 ] 
])

boards['writeup_1'] = reversed([
    [  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0,  0,  0,  0,  0 ],
    [  0,  0,  0, -1,  0,  0,  0 ],
    [  0,  0,  0,  1,  0,  0,  0 ],
    [  0,  1,  0, -1,  0,  1,  0 ]
])

boards['writeup_2'] = reversed([  
    [ -1,  1, -1, -1 ],                       
    [  1, -1,  1, -1 ],
    [  1, -2, -1,  1 ],
    [  1, -2,  1, -1 ] 
])

boards['your_test'] = reversed([])  # put something here!



