import pytest
from src.mapper import map_fhir_address

# @pytest.fixture()
# def resource():
#     print("setup")
#     yield "resource"
#     print("teardown")


class TestFhirAddressMapper:
    def test_map_fhir_address_test(self):
        fhir = {"something": "else"}
        address = "addressssss"
        assert map_fhir_address(fhir, address) == {"something": "address"}
