

class AP:
    PROD='prod'
    STAGE='staging'
    QA='QA'

class Login:
    user_name="autogda00@gmail.com"
    password="access4auto"

class Auth():
    def __init__(self,ap,userlogin):
        self.Login=userlogin
        self.env=ap
        if self.env==AP.PROD:
            self.client_id="caf2e380f57e41526a0d8ff77f74b356b3eb9ff4e15cc0242be9b2ac71964d9f"
            self.client_secret="6fa55a297cdd8a8b98f8d6df4e0dab8d6758ca878faa09eb84e7463cb7e8a0f4"
            self.base_url="api.gopro.com"
            self.access_token="161ed60c50a82de0a4f7c8bddd9c6fc903312aa5a631df13ee180da80d4b613b"
            self.profile_id="fb21027d-cce9-4b52-aa0d-5c2d911a5968"
        elif self.env==AP.STAGE:
            self.client_id="b961e40c5163e2adbf68e392a948611eace48d2e7e85b3d733d4abec04329cbc"
            self.client_secret="7cb594146a104ad5598f59325bf85ed8e59f54c00da19cf98962277441e10650"
            self.base_url="api.staging.gopro.com"
            self.user_id="c00f6a19 - 8d26 - 415b - b00b - 1e12d1a8303f"
            self.service_id="2031"
            self.platform="mobile"
            self.media_id="ee5p42djN65p"
            self.access_token="f6cce3b09f0a55087a19712cf0bd7ffe14d1264b82587e4b4a0538ac16aab222"
            self.profile_id="09f4d0cf - 6730 - 4282 - b5b8 - 45fa0e35b0ad"
            self.user_name="bfriedman @ gopro.com"
            self.password="passwordst"
            self.device_token="undefined"
        elif self.env == AP.QA:
            self.client_id="8196170419ff39c4a27f3b6dae672dce2c3eb89b8a91b83e7a579cb6ce1f97e5"
            self.client_secret="df64221fdb8602037a3f62cb6009931b420a0cc4b32e5df0681a7332722cca5c"
            self.base_url="api.qa.gopro.com"
            self.user_id="c00f6a19 - 8d26 - 415b - b00b - 1e12d1a8303f"
            self.service_id="2031"
            self.platform="mobile"
            self.media_id="ee5p42djN65p"
            self.user_name="doddy @ gopro.com"
            self.password="password"
            self.media_id2="nyBOX34XDlP"
            self.access_token="0f978f95a719b09db699e097a1d08f62f01b34c0845c41238b2279aae81fee36"
            self.profile_id="92babdbd - 0144 - 4aad - a6db - bb55def54eb0"
            self.device_token="a98b3d25 - dd17 - 496d - 9e28 - 52156c5d4228"
            self.device_code="448833"


class WebAPIMethods():
    def __init__(self, auth):
        self.auth=auth

