import pytest
from unittest.mock import patch
from argparse import Namespace
from pyls.argument_parser import ArgumentParser


@pytest.fixture
def patched_parse_args():
    """
    Fixture to patch ArgumentParser.parse_args().

    :return: Mock object for parse_args()
    """
    with patch('pyls.argument_parser.argparse.ArgumentParser.parse_args') as mock_parse_args:
        yield mock_parse_args


@pytest.fixture
def parser():
    """
    Fixture to create an instance of ArgumentParser.

    :return: ArgumentParser instance
    """
    return ArgumentParser()


def test_default_arguments(parser, patched_parse_args):
    """
    Test default arguments.

    :param parser: ArgumentParser instance
    :param patched_parse_args: Mock object for parse_args()
    :return: None
    """
    patched_parse_args.return_value = Namespace(A=False, l=False, r=False, t=False, filter=None, path=None)
    args = parser.parse_args()
    assert args.path is None
    assert not args.A
    assert not args.l
    assert not args.r
    assert not args.t
    assert args.filter is None


def test_short_arguments(parser, patched_parse_args):
    """
    Test short arguments.

    :param parser: ArgumentParser instance
    :param patched_parse_args: Mock object for parse_args()
    :return: None
    """
    patched_parse_args.return_value = Namespace(A=True, l=True, r=True, t=True, filter=None, path='path')
    args = parser.parse_args()
    assert args.A
    assert args.l
    assert args.r
    assert args.t
    assert args.filter is None
    assert args.path == 'path'


def test_long_arguments(parser, patched_parse_args):
    """
    Test long arguments.

    :param parser: ArgumentParser instance
    :param patched_parse_args: Mock object for parse_args()
    :return: None
    """
    patched_parse_args.return_value = Namespace(A=False, l=False, r=False, t=False, filter='files', path='path')
    args = parser.parse_args()
    assert not args.A
    assert not args.l
    assert not args.r
    assert not args.t
    assert args.filter == 'files'
    assert args.path == 'path'
