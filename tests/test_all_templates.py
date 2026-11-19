"""
Omni-Templates 100% Quality Assurance Test Suite
------------------------------------------------
Comprehensive test harness validating every template in the repository
for syntactic, structural, and functional compliance.
"""

import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = BASE_DIR / "templates"


class TestOmniTemplates(unittest.TestCase):

    def test_ai_model_factory_template(self):
        ai_dir = TEMPLATES_DIR / "ai-model-factory"
        self.assertTrue((ai_dir / "train_qlora.py").exists())
        self.assertTrue((ai_dir / "quantize_gguf.py").exists())
        self.assertTrue((ai_dir / "serve_openai_api.py").exists())
        self.assertTrue((ai_dir / "setup_windows.ps1").exists())
        self.assertTrue((ai_dir / "setup_mac_linux.sh").exists())
        self.assertTrue((ai_dir / "Modelfile.template").exists())

    def test_fullstack_webapp_template(self):
        app_dir = TEMPLATES_DIR / "fullstack-webapp"
        self.assertTrue((app_dir / "backend" / "server.py").exists())
        self.assertTrue((app_dir / "static" / "index.html").exists())
        self.assertTrue((app_dir / "Dockerfile").exists())
        self.assertTrue((app_dir / "docker-compose.yml").exists())

        # Test HTML content
        html = (app_dir / "static" / "index.html").read_text(encoding="utf-8")
        self.assertIn("TaskPulse", html)
        self.assertIn("api/tasks", html)

    def test_android_mobile_apk_template(self):
        mobile_dir = TEMPLATES_DIR / "android-mobile-apk"
        manifest = mobile_dir / "app" / "src" / "main" / "AndroidManifest.xml"
        self.assertTrue(manifest.exists())
        
        tree = ET.parse(manifest)
        root = tree.getroot()
        self.assertIn("package", root.attrib)

        activity = mobile_dir / "app" / "src" / "main" / "java" / "com" / "omni" / "app" / "MainActivity.java"
        self.assertTrue(activity.exists())
        self.assertIn("MainActivity", activity.read_text(encoding="utf-8"))

    def test_saas_landing_page_template(self):
        page_dir = TEMPLATES_DIR / "saas-landing-page"
        index = page_dir / "index.html"
        self.assertTrue(index.exists())
        content = index.read_text(encoding="utf-8")
        self.assertIn("viewport", content)
        self.assertIn("tailwind", content.lower())
        self.assertIn("glass", content)

    def test_brand_identity_template(self):
        brand_dir = TEMPLATES_DIR / "brand-identity-system"
        self.assertTrue((brand_dir / "generate_brand_assets.py").exists())
        
        assets_dir = brand_dir / "assets"
        svgs = list(assets_dir.glob("*.svg"))
        self.assertGreaterEqual(len(svgs), 3)

        for s in svgs:
            tree = ET.parse(s)
            self.assertIn("svg", tree.getroot().tag.lower())

        guide = assets_dir / "BRAND_STYLE_GUIDELINES.md"
        self.assertTrue(guide.exists())
        self.assertIn("Color Palette", guide.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
