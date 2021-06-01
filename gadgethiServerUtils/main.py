import sys
import re
import argparse

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
    parser.add_argument("args", nargs=1, help="arguments for the given command")

    if not args:
        args = parser.parse_args(arglist)

    if args.command == "configure":
        from _configs import generate_configs

        # make sure the arguments meet the regex
        yaml_regex = "^.+\.yaml$"

        if not bool(re.search(yaml_regex, args.args[0])):
            print("Args %s is not a yaml file" % args.args[0])
            sys.exit(-1)

        generate_configs(args.args[0])

    else:
        print("Unknown command %s" % args.command)
        sys.exit(-1)

if __name__ == '__main__':
    command_line_interface()