import argparse

def main():
    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')
    parser.add_argument('filepath',type=int,required=True,
                        dest='filepath',
                        help="")
    parser.add_argument('-a',type=int,required=True,
                        dest='algorithm',
                        help="")
    parser.add_argument('-s',type=int,required=False,
                        default= 0,
                        dest='seed',
                        help="")
    args = parser.parse_args()
    print(args.algorithm)
    print(args.seed)

if __name__ == "__main__":
    main()