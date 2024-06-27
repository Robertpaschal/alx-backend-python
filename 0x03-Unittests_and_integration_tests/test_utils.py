#!/usr/bin/env python3
"""
Test module
"""
import unittest
from utils import access_nested_map
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


if __name__ == "__main__":
    unittest.main()
