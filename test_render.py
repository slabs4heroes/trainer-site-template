import json
import tempfile
import unittest
from pathlib import Path

from render import HERE, validate_pack, main


class SiteGeneratorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pack = json.loads((HERE / "content_packs/gator-alley-k9.json").read_text())
        cls.images = json.loads((HERE / "content_packs/gator-alley-images.json").read_text())

    def test_preview_passes_and_publish_needs_a_real_webhook(self):
        self.assertEqual(validate_pack(self.pack, self.images), [])
        errors = validate_pack(self.pack, self.images, publish=True)
        self.assertTrue(any("preview-only" in e for e in errors))
        self.assertTrue(any("lead_webhook_url" in e for e in errors))

    def test_missing_image_fails_closed(self):
        pack = json.loads(json.dumps(self.pack))
        pack["programs"]["hero"]["image_url"] = "IMG:not approved"
        self.assertTrue(any("asset manifest" in e for e in validate_pack(pack, self.images)))

    def test_publish_passes_once_a_real_webhook_is_set(self):
        pack = json.loads(json.dumps(self.pack))
        pack["business"]["lead_webhook_url"] = "https://services.leadconnectorhq.com/hooks/test/webhook-trigger/abc123"
        # still has "gen-test"/"viktor.page" preview strings elsewhere in this pack -> still blocked
        errors = validate_pack(pack, self.images, publish=True)
        self.assertTrue(any("preview-only" in e for e in errors))
        self.assertFalse(any("lead_webhook_url" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
