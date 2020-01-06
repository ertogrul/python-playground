




#---------------- sys.argv
'''

import sys

print('hello')
print(sys.argv)
'''

# -----------------------------	 \t  \n
'''
para_str = """this is a long string that is made up of
several lines and non-printable characters such as
TAB ( \t ) and they will show up that way when displayed.
NEWLINEs within the string, whether explicitly given like
this within the brackets [ \n ], or just a NEWLINE within
the variable assignment will also show up.
"""
print (para_str)

'''


'''
valid_algos = ['vpg', 'trpo', 'ppo', 'ddpg', 'td3', 'sac']
valid_utils = ['plot', 'test_policy']

str_valid_cmds = '\t'+ '\n\t'.join(valid_algos+valid_utils)
print(str_valid_cmds)
'''


# ---------------PRZYJKŁAD UŻYCIA JOIN
'''
s = "-";
seq = ("a", "b", "c");
print (s.join(seq))

'''

#------------------- eval
'''
s = "10+4+57"
ev = eval(s)
print (ev)
'''

#--------------------

#pusc komende: python -m spinup.run ppo --hid "[32,32]" --env LunarLander-v2 --exp_name installtest --gamma 0.999
'''
import sys
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])

for i in range(len(sys.argv)):
	print(sys.argv[i])
'''
#----------------------

cmd = 'ppo'
algo = eval('spinup.'+cmd)
print(algo)






