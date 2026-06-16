import argparse

parent_parser = argparse.ArgumentParser(prog="test", 
                                 description="testing argparse", 
                                 epilog="text after description", 
                                 add_help=False
                                 )
parent_parser.add_argument("--help", help="test")
parent_parser.add_argument("--test", help="output")

main_parser = argparse.ArgumentParser(parents=[parent_parser])
main_parser.add_argument("-f", help="output_2")