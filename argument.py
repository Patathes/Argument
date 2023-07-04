import sys

class Argument:

    def __init__(self, name=sys.argv[0], description=sys.argv[0]):
        self.name = name
        self.description = description
        self.args = {}

    def add(self, label: str, long: str="", range: tuple=(), type: type=str, target=lambda _: _, required: bool=True, default=None, message: str=""):
        if range != ():
            type = str
        self.args[label] = (range, type, target, required, default, message)

    def help(self):
        arg_list = list()
        print(self.name)
        print("-" * 5)
        print(self.description)
        print()
        for k, v in self.args.items():
            print(f"[{k}]: {v[-1]}")
            arg_list.append(k)
        print("\n\n")
        for k in arg_list:
            print(f"[{k}]  ", end="")
        print()

    def parse(self):
        values = {}
        for k, v in self.args.items():
            if v[-3]:
                values[k.replace("-", "")] = v[-2]

        if "-h" in sys.argv or "--help" in sys.argv:
            self.help()
            return

        for k, v in self.args.items():
            for index in range(1, len(sys.argv)):
                if sys.argv[index] == k:
                    if index + 1 >= len(sys.argv) and v[-3]:
                        print(f"Required item {k} not given")
                        print()
                        self.help()
                        return
                    elif index + 1 >= len(sys.argv):
                        pass
                    elif len(v[0]):
                        if str(sys.argv[index + 1]) not in v[0]:
                            print(f"Given argument {k} must be in {v[0]}")
                            print()
                            self.help()
                            return
                        else:
                            values[k.replace("-", "")] = v[1](sys.argv[index + 1])
                    elif (v[1] != str) and type(v[1](sys.argv[index + 1])) != v[1]:
                        print(f"Type of item {k} not matching with required type {v[1]}")
                        print()
                        self.help()
                        return
                    elif v[2] != False:
                        values[k.replace("-", "")] = v[2](v[1](sys.argv[index + 1]))
                    else:
                        values[k.replace("-", "")] = v[1](sys.argv[index + 1])

        return values
