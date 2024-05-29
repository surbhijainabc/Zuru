from pyls.utilities import human_readable_size


def test_human_readable_size():
    """
    Test the human_readable_size function.

    It tests the conversion of integer sizes to human-readable format. Added test for bytes,
    kilobytes, megabytes, gigabytes and edge case.

    :return: None
    """
    assert human_readable_size(512) == "512B"

    assert human_readable_size(2048) == "2.0K"
    assert human_readable_size(1500) == "1.5K"

    assert human_readable_size(1024 ** 2 * 2) == "2.0M"
    assert human_readable_size(1024 ** 2 * 1.5) == "1.5M"

    assert human_readable_size(1024 ** 3 * 2) == "2.0G"
    assert human_readable_size(1024 ** 3 * 1.5) == "1.5G"

    assert human_readable_size(0) == "0B"
