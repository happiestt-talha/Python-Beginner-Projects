import argparse as ag
par = ag.ArgumentParser()

par.add_argument(
    "--name",
    type=str,
    help="Enter your name",
    required=True

)
args = par.parse_args()
print(args.name)
# now you can use this program to get a person's name from the command line
