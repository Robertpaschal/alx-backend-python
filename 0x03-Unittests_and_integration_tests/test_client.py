#!/usr/bin/env python3
"""
Test client module
"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import patch, Mock
from typing import Dict


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests the GithubOrgClient class
    """
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json', return_value={"login": "google"})
    def test_org(self,
                 org_name: str,
                 expected: Dict,
                 mock_get_json: Mock) -> None:
        """
        Test that GithubOrgClient.org returns the correct value.

        Parameters
        ----------
        org_name: str
            The name of the organization.
        expected: Dict
            The expected JSON response.
        mock_get_json: Mock
            Mock object for get_json.
        """
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected)


if __name__ == "__main___":
    unittest.main()
