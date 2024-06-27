#!/usr/bin/env python3
"""
Test module
"""
import unittest
from unittest.mock import (
    patch,
    Mock
)
from utils import (
    access_nested_map,
    get_json
)
from typing import Any, Dict, Tuple
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests for access_nested_map function.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Dict[str, Any],
                               path: Tuple[str, ...],
                               expected: Any) -> None:
        """
        Test that access_nested_map returns the expected result.

        Parameters
        ----------
        nested_map: Dict[str, Any]
            A nested dictionary to access.
        path: Tuple[str, ...]
            A sequence of keys representing the path to the value.
        expected: Any
            The expected value to be returned from the nested map.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'")
    ])
    def test_access_nested_map_exception(self,
                                         nested_map: Dict[str, Any],
                                         path: Tuple[str, ...],
                                         expected: str) -> None:
        """
        Test that access_nested_map raises KeyError with the expected message.

        Parameters
        ----------
        nested_map: Dict[str, Any]
            A nested dictionary to access.
        path: Tuple[str, ...]
            A sequence of keys representing the path to the value.
        expected_exception_message: str
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected)


class TestGetJson(unittest.TestCase):
    """
    Test class for get_json method
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url: str, test_payload: Dict) -> None:
        """
        Test that get_json returns the expected result.

        Parameters
        ----------
        test_url: str
            The URL to request.
        test_payload: Dict
            The expected JSON payload.
        """
        config = {'return_value.json.return_value': test_payload}
        patcher = patch('requests.get', **config)
        mock = patcher.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patcher.stop()


if __name__ == "__main__":
    unittest.main()
