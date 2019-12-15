#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 12:48:01 2019

@author: dh
"""


import sys
import argparse


#%%

def add_arg_verbose(parser):
    parser.add_argument('-v', '--verbose',
                        nargs='?',
                        default=0,
                        const=1,
                        help='Verbose level')


#%%

class MyArgParser:

    def __init__(self, *args, **kwargs):
        self.add_args(*args, **kwargs)

    def add_args(self, *args, **kwargs):
        parser = argparse.ArgumentParser()


        subparsers = parser.add_subparsers(title="commands",
                                           dest="command")

        self.parser = parser
        self.subparsers = subparsers

        self.add_subparser_init()
        self.add_subparser_clone()

        self.add_subparser_show()
        self.add_subparser_status()
        self.add_subparser_list()

        self.add_subparser_exec()
        self.add_subparser_cancel()


    def add_subparser_init(self):
        p = self.subparsers.add_parser('init', help='init help')

        p.add_argument('destination', help='Init new job directory')

        p.add_argument('-n', '--dry-run', help='Dry run')
        add_arg_verbose(p)

    def add_subparser_clone(self):
        p = self.subparsers.add_parser('clone', help='clone help')

        p.add_argument('source', help='Directory to clone')
        p.add_argument('destination', help='Destination of cloned job directory')

        p.add_argument('-n', '--dry-run', help='Dry run')
        add_arg_verbose(p)

    def add_subparser_show(self):
        p = self.subparsers.add_parser('show', help='show help')

        p.add_argument('object', help='Object to show')

        add_arg_verbose(p)

    def add_subparser_status(self):
        p = self.subparsers.add_parser('status', help='status help')

        add_arg_verbose(p)

    def add_subparser_list(self):
        p = self.subparsers.add_parser('list', help='list help')

        p.add_argument('-e', '--executing', action='store_true', help='List executing')
        p.add_argument('-c', '--complete', action='store_true', help='List complete')
        p.add_argument('-i', '--incomplete', action='store_true', help='List incomplete')
        p.add_argument('-m', '--missing', action='store_true', help='List missing')

        add_arg_verbose(p)

    def add_subparser_exec(self):
        p = self.subparsers.add_parser('exec', help='exec help')

        p.add_argument('--prio', type=int, help='Use given priority level')

        p.add_argument('-n', '--dry-run', help='Dry run')
        add_arg_verbose(p)

    def add_subparser_cancel(self):
        p = self.subparsers.add_parser('cancel', help='cancel help')

        p.add_argument('-n', '--dry-run', help='Dry run')
        add_arg_verbose(p)



#        # create the parser for the "a" command
#        parser_a = subparsers.add_parser('init', help='init help')
#        parser_a.add_argument('bar', type=int, help='bar help')
#
#        # create the parser for the "b" command
#        parser_b = subparsers.add_parser('exec', help='exec help')
#        parser_b.add_argument('--baz', choices='XYZ', help='baz help')


#        self.add_subparser_init()
#        self.add_subparser_clone()
#        self.add_subparser_exec()
#        self.add_subparser_status()
#        self.add_
#
#        p = self.parser
#
#        p.add_argument("-n", "--dry-run", help="Do dry run")
#        p.add_argument("-i", "--incomplete", help="incomplete")

#        self.parser = p
#
#    def add_subparser_init(self):
#        p = self.parser

    def parse_args(self, *args, **kwargs):
        self.args = self.parser.parse_args()

        print(self.args)



#%%

class MyApp:

    def __init__(self, *args, **kwargs):
        self.configure(*args, **kwargs)
        self.run()

    def configure(self, *args, **kwargs):
        self.arg_parser = MyArgParser()

    def run(self, *args, **kwargs):
        pass


#%%

def main():
    self = MyArgParser()

    self.parse_args()


if __name__ == "__main__":
    main()

