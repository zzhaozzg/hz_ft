import json
from unittest import TestCase

from api.base_api.image_captcha_api import ImageCaptchaApi
from settings import STATUS_CODE, IMG_CAPTCHA_URL


class TestCaptchaImageApi(TestCase):

    def test_captcha_image(self):
        rep = ImageCaptchaApi().get()
        self.assertEqual(rep.status_code, STATUS_CODE)
        rep_url = json.loads(rep.content)['url']
        rep_captcha_hash = json.loads(rep.content)['captcha_hash']
        self.assertIn(IMG_CAPTCHA_URL, rep_url)
        self.assertEqual(len(rep_captcha_hash), 40)
