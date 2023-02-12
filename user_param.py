import argparse

# user input
parser = argparse.ArgumentParser(prog="T20", description="Manage your screen time.")
parser.add_argument('-m', '--min', type=int, default=20, help='set number of minutes to work. default: 20.')
parser.add_argument('-s', '--sec', type=int, default=20, help='set number of seconds to rest. default: 20.')
parser.add_argument('-l', '--loop', type=int, default=-1, help="""how many times repeat the timer.
(-1 for nonstop) default: -1.""")
parser.add_argument('-S', '--suspend', default=False, action='store_true', help="""suspend the screen after the work 
time is over. (disable rest and loop)""")
parser.add_argument('-q', '--quiet', default=True, action='store_false', help='disable alarm in the last minutes')

args = parser.parse_args()
# end of user input
