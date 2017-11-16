"""CLI for the package."""

import argparse
import sys

from . import log as cli_log
from ..lib import app


def parse_args(args):
    """Parse command line arguments."""
    desc = "A reverse tableaux prover."
    parser = argparse.ArgumentParser(description=desc)

    verb_help = "show verbose output?"
    parser.add_argument("--verbose", help=verb_help, action="store_true")

    return parser.parse_args(args)


def cli():
    """Execute/run the CLI."""
    args = parse_args(sys.argv[1:])
    log = cli_log.get_log(args.verbose)
    log("Starting the program...")
    try:
        app.run(log)
    except:  # noqa: E722
        exc_type, exc_val, exc_tb = sys.exc_info()
        msg = "Error - {}: {}".format(exc_type.__name__, exc_val)
        sys.exit(msg)
