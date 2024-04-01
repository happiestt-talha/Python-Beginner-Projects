import argparse as ag
p = ag.ArgumentParser()
p.add_argument("URL", help="Url ha jo kaand kro gy us ka")
p.add_argument("output", help="Apka Kiya hua kaand")

arg = p.parse_args()
print(arg.URL)
print(arg.output)
