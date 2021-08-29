#!/usr/bin/env python3
"""utils testing class"""
from unittest import TestCase
from unittest.mock import patch
from utils import access_nested_map, get_json
from parameterized import parameterized


class TestAccessNestedMap(TestCase):
    """main access_nested_map testing."""

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

class TestGetJson(TestCase):
    """ Class for Get Json Tests """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test that utils.get_json returns the expected result."""
        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()
