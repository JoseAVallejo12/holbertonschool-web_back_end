#!/usr/bin/env python3
"""Simple pagination"""


import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


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
        """get specific index an a list

        Args:
            page (int, optional): [description]. Defaults to 1.
            page_size (int, optional): [description]. Defaults to 10.

        Returns:
            List[List]: list of values
        """
        assert(type(page) == int == type(page_size))
        assert(page > 0 < page_size)
        self.dataset()
        start_index, end_index = index_range(page, page_size)
        return self.__dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> object:
        """[summary]

        Args:
            page (int, optional): [description]. Defaults to 1.
            page_size (int, optional): [description]. Defaults to 10.

        Returns:
            object: [description]
        """
        data_list = self.get_page(page, page_size)
        if len(data_list) == 0:
            next_index = None
        else:
            next_index = page + 1
        return {
            'page_size': len(data_list),
            'page': page,
            'data': data_list,
            'next_page': next_index,
            'prev_page': page - 1,
            'total_pages':  int(round(len(self.__dataset) / page_size))
        }