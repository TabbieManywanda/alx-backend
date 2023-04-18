#!/usr/bin/env python3

'''Class definition'''

import csv
import math
from typing import List, Tuple, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''method named `get_page`'''
        assert type(page_size) is int and type(page) is int
        assert page > 0
        assert page_size > 0
        self.dataset()
        index = index_range(page, page_size)
        if index[0] >= len(self.__dataset):
            return []
        else:
            return self.__dataset[index[0]:index[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        '''method named `get_hyper`'''
        dataset_items = len(self.dataset())
        data = self.get_page(page, page_size)
        total_pages = math.ceil(dataset_items / page_size)

        p = {
            'page': page,
            'page_size': page_size if page < total_pages else 0,
            'data': data,
            'next_page': page + 1 if page + 1 < total_pages else None,
            'prev_page': page - 1 if page - 1 > 0 else None,
            'total_pages': total_pages
            }
        return p


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''return a tuple of size two containing
    a start index and an end index
    corresponding to the range of indexes to return
    in a list for those particular pagination parameters'''

    startIndex = (page - 1) * page_size
    endIndex = startIndex + page_size

    return (startIndex, endIndex)
