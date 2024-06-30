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

    def test_public_repos_url(self) -> None:
        """
        Test that GithubOrgClient._public_repos_url returns the correct URL.
        """
        expected_repos_url = "https://api.github.com/orgs/google/repos"
        payload = {"repos_url": expected_repos_url}

        with patch.object(GithubOrgClient,
                          'org', new_callable=Mock, return_value=payload):
            client = GithubOrgClient("google")
            result = client._public_repos_url
            self.assertEqual(result, expected_repos_url)


if __name__ == "__main___":
    unittest.main()
