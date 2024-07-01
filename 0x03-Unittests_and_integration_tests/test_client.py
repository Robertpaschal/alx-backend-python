#!/usr/bin/env python3
"""
Test client module
"""
import unittest
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
from typing import Dict
from fixtures import TEST_PAYLOAD
import requests


class TestGithubOrgClient(unittest.TestCase):
    """
    Tests the GithubOrgClient class
    """
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json')
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
        mock_get_json.return_value = expected
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
                          'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = payload
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
                          new_callable=PropertyMock) as mock_repos_url:
            mock_repos_url.return_value = expected_repos_url
            client = GithubOrgClient("google")
            result = client.public_repos()

            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(result, expected_repos)

            mock_get_json.assert_called_once_with(expected_repos_url)

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


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test for GithubOrgClient.public_repos
    """
    @classmethod
    def setUpClass(cls) -> None:
        """ Set up the class"""
        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        """Tear down the class"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method
        Integration test: public repos"""
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """ Integration test for public repos with License """
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.assertEqual(test_class.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()


if __name__ == "__main__":
    unittest.main()
