import json
from unittest import TestCase

from api.base_api.version_api import VersionApi
from api.settings import STATUS_CODE



class TestVersionApi(TestCase):

    def test_version(self):
        rep = VersionApi().get()
        self.assertEqual(rep.status_code, STATUS_CODE)
        rep_content = json.loads(rep.content)
        self.assertEqual(len(rep_content), 5)
        self.assertEqual(rep_content['message'], 'updatestest')
