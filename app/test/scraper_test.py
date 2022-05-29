import pytest, os, uuid, docker, json
from src.scraper import Scraper
from unittest.mock import patch, Mock
import os

def test_process_address_csv(mocker):
    csv_data = Scraper.process_address_csv("./app/test/file_testing_directory", remove_file=False)
    # assert sorted(files) == sorted(["thing.txt", "data.csv"])
    print(csv_data[0])
    assert csv_data[0] == {'address': '2604 Burlington Ave', 'city': 'Downers Grove', 'state': 'IL', 'zip': '60515', 'latitude': '41.7967207', 'longitude': '-88.0461085'}


