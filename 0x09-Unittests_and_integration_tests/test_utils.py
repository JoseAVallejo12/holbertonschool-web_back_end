#!/usr/bin/env python3
"""utils testing class"""
from unittest import TestCase
from utils import access_nested_map, memoize
from parameterized import parameterized


class TestAccessNestedMap(TestCase):
    """Main testing class."""

    @parameterized.expand([
        ({"a": 1}, ['a'], 1),
        ({"a": {"b": 2}}, ['a'], {"b": 2}),
        ({"a": {"b": 2}}, ['a', 'b'], 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """method access_nested_map test."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ['a']),
        ({"a": 1}, ['a', 'b'])
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test raise error method access_nested_map."""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, path)
