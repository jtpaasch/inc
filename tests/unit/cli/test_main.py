"""Unit tests for the ``cli.main`` module."""

from unittest import TestCase
from unittest.mock import patch, Mock

from inc.cli import main


class TestMain(TestCase):
    """Test suite for the ``cli.main`` module."""

    def test_args(self):
        """Ensure ``parse_args()`` gets the right args."""
        main_module = main.__name__
        p1 = patch("{}.argparse.FileType".format(main_module))
        with p1:
            args = main.parse_args([
                "--verbose"])
            self.assertTrue("verbose" in args)

    def test_cli(self):
        """Ensure ``cli()`` invokes the main program."""
        args = Mock(
            verbose="dummy-verbose-flag"
        )
        log = Mock()

        main_module = main.__name__
        p1 = patch("{}.main.run".format(main_module))
        p2 = patch("{}.parse_args".format(main_module))
        p3 = patch("{}.cli_log.get_log".format(main_module))

        with p1 as main_run, p2 as parse_args, p3 as get_log:
            parse_args.return_value = args
            get_log.return_value = log

            main.cli()
            main_run.assert_called_once_with(log)

    def test_cli_catches_errors(self):
        """Ensure ``cli()`` catches errors and exits cleanly."""
        main_module = main.__name__
        p1 = patch("{}.main.run".format(main_module))
        p2 = patch("{}.parse_args".format(main_module))
        with p1 as main_run, p2:
            main_run.side_effect = Exception
            with self.assertRaises(SystemExit):
                main.cli()
