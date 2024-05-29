def human_readable_size(size: int) -> str:
    """
    Convert size in bytes to a human-readable string representation.

    size: Size in bytes.
    """
    if size < 1024:
        return f"{size}B"
    elif size < 1024 ** 2:
        return f"{size / 1024:.1f}K"
    elif size < 1024 ** 3:
        return f"{size / 1024 ** 2:.1f}M"
    else:
        return f"{size / 1024 ** 3:.1f}G"
