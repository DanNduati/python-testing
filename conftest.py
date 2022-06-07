import pytest
import requests

# Autouse fixtures -> fixtures you do not have to request
# A fixture that all your tests will depend on.
# use of autouse fixtures cuts out a lot of redundant requests
@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def stunted_get():
        raise RuntimeError("Network access is not allowed during testing!!")
    monkeypatch.setattr(requests,"get",lambda *args, **kwargs:stunted_get())