"""
    Umweltbundesamt Air Data API

    Air data API of Umweltbundesamt  # noqa: E501

    The version of the OpenAPI document: 2.0.1
    Contact: immission@uba.de
    Generated by: https://openapi-generator.tech
"""


import unittest

from deutschland.luftqualitaet.api.metadata_api import MetadataApi  # noqa: E501

from deutschland import luftqualitaet


class TestMetadataApi(unittest.TestCase):
    """MetadataApi unit test stubs"""

    def setUp(self):
        self.api = MetadataApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_components_json_get(self):
        """Test case for components_json_get

        Get all components  # noqa: E501
        """
        pass

    def test_meta_json_get(self):
        """Test case for meta_json_get

        Get combined metadata for use  # noqa: E501
        """
        pass

    def test_networks_json_get(self):
        """Test case for networks_json_get

        Get all networks  # noqa: E501
        """
        pass

    def test_scopes_json_get(self):
        """Test case for scopes_json_get

        Get all scopes  # noqa: E501
        """
        pass

    def test_stationsettings_json_get(self):
        """Test case for stationsettings_json_get

        Get all station settings  # noqa: E501
        """
        pass

    def test_stationtypes_json_get(self):
        """Test case for stationtypes_json_get

        Get all station types  # noqa: E501
        """
        pass

    def test_thresholds_json_get(self):
        """Test case for thresholds_json_get

        Get all thresholds  # noqa: E501
        """
        pass

    def test_transgressiontypes_json_get(self):
        """Test case for transgressiontypes_json_get

        Get all exceedances types  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
