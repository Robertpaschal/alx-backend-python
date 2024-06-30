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
    get_json,
    memoize
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
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    Tests for the memoize decorator.
    """
    def test_memoize(self) -> None:
        """
        Tests the memoize decorator.
        """
        class TestClass:
            def a_method(self) -> int:
                """
                A method that returns a fixed value.
                """
                return 42

            @memoize
            def a_property(self) -> int:
                """
                A memoized property that calls a_method.
                """
                return self.a_method()

        with patch.object(TestClass,
                          'a_method', return_value=42) as mock_method:
            test_instance = TestClass()

            result1 = test_instance.a_property
            result2 = test_instance.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
