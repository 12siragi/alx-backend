#!/usr/bin/env python3
"""
This module contains a function that takes two integer arguments page and
page_size and returns a tuple of size two containing start and end index.
"""

from typing import Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for the given page and page_size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
