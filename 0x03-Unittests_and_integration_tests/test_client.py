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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: Mock) -> None:
        """Test that GithubOrgClient.public_repos
        returns the correct list of repos."""
        expected_repos_url = "https://api.github.com/orgs/google/repos"
        repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "apache-2.0"}}
        ]
        mock_get_json.return_value = repos_payload

        with patch.object(GithubOrgClient,
                          '_public_repos_url',
                          new_callable=Mock, return_value=expected_repos_url):
            client = GithubOrgClient("google")
            result = client.public_repos()

            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(result, expected_repos)

            mock_get_json.assert_called_once_with(expected_repos_url)
            client._public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self,
                         repo: Dict,
                         license_key: str, expected: bool) -> None:
        """Test that GithubOrgClient.has_license returns the correct value.

        Parameters
        ----------
        repo: Dict
            The repository dictionary.
        license_key: str
            The license key to check.
        expected: bool
            The expected result.
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main___":
    unittest.main()
