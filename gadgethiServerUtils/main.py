import os
import sys
import argparse
import pkg_resources

def command_line_interface(args=None, arglist=None):
    """
    Main catsoop command line entry point
    args, arglist are used for unit testing
    """
    help_text = """
Example commands:
    configure      : generate gserver configuration file using an interactive wizard
"""
    cmd_help = """A variety of commands are available, each with different arguments:
configure      : generate gserver configuration file using an interactive wizard
"""

    parser = argparse.ArgumentParser(
        description=help_text, formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("command", help=cmd_help)
    parser.add_argument("args", nargs="*", help="arguments for the given command")

    if not args:
        args = parser.parse_args(arglist)

    if args.command == "configure":
        from .scripts import configure

        configure.main()

    else:
        print("Unknown command %s" % args.command)
        sys.exit(-1)