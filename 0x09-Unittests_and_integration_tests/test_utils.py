#!/usr/bin/env python3
"""utils testing class"""
from unittest import TestCase
from utils import access_nested_map, memoize
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(TestCase):
    """Main testing class."""

    @parameterized.expand([
        ({"a": {"b": {"c": 1}}}, ["a", "b", "c"], 1),
        ({"a": 1}, ['a'], 1),
        ({"a": {"b": 2}}, ['a'], {"b": 2}),
        ({"a": {"b": 2}}, ['a', 'b'], 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(access_nested_map(nested_map, path), expected)
