# https://vcrpy.readthedocs.io/en/latest/usage.html
import unittest
import uuid
from unittest.mock import patch

import vcr
from freezegun import freeze_time

from data_extractor.extractor import Extractor


class TestExtractor(unittest.TestCase):
    def test_extract(self):
        with vcr.use_cassette("tests/fixtures/vcr_cassettes/test_extract.yaml"): # https://vcrpy.readthedocs.io/en/latest/usage.html#usage
            extractor = Extractor("https://www.example.com")
            data = extractor.get_data()

            self.assertTrue("Example Domain" in data)

###########################################################

# my_vcr = vcr.VCR(
#     cassette_library_dir="tests/fixtures/vcr_cassettes",
#     match_on=["uri", "method"], # https://vcrpy.readthedocs.io/en/latest/configuration.html#request-matching
#     # this is the default list of matchers
# )

# class TestExtractor(unittest.TestCase):
#     def test_extract(self):
#         # once, new_episodes, none, all
#         with my_vcr.use_cassette("test_extract.yaml", record_mode="once"): # https://vcrpy.readthedocs.io/en/latest/usage.html#record-modes
#             extractor = Extractor("https://www.example.com")
#             page = extractor.get_data()

#             self.assertTrue("Example Domain" in page)

###########################################################

# class TestExtractor(unittest.TestCase):
#     def test_extract(self):
#         with vcr.use_cassette("tests/fixtures/vcr_cassettes/test_multiple_extract.yaml", record_mode="once"):
#             extractor = Extractor("https://example.com")
#             pages = extractor.get_data_with_loop()

#             self.assertTrue(all(["Example Domain" in page for page in pages]))

###########################################################

# @patch("data_extractor.extractor.uuid4", return_value=uuid.UUID("4f620be9-a6e7-4e65-9846-f08805823617")) # Always stub before recording
# @freeze_time("2023-08-17T09:44:24Z") # Stub after recording by looking for the timestamp in the cassette
# class TestExtractor(unittest.TestCase):
#     def test_extract(self, uuid_mock):
#         with vcr.use_cassette("tests/fixtures/vcr_cassettes/test_unstable_extract.yaml", record_mode="once"):
#             extractor = Extractor("https://example.com")
#             page = extractor.get_data_with_changing_query()

#             self.assertTrue("Example Domain" in page)
