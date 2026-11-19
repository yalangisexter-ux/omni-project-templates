"""
Vector Logo & Brand Identity Asset Generator
-------------------------------------------
Generates production-grade, mathematically balanced vector SVG brand assets
and style guides with zero external dependencies.
"""

import json
from pathlib import Path

OUT_DIR = Path(__file__).resolve().parent / "assets"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def generate_horizontal_logo(brand_name: str, tag: str, primary_color: str = "#6366F1", secondary_color: str = "#06B6D4") -> str:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 200" width="800" height="200">
  <defs>
    <linearGradient id="nexusGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{primary_color}" />
      <stop offset="100%" stop-color="{secondary_color}" />
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="8" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Background container for dark mode preview -->
  <rect width="100%" height="100%" rx="16" fill="#0B0F19"/>

  <!-- Geometric Abstract Tech Emblem -->
  <g transform="translate(60, 40)">
    <!-- Outer Hex Shield -->
    <polygon points="60,10 110,38 110,95 60,123 10,95 10,38" fill="none" stroke="url(#nexusGrad)" stroke-width="6" stroke-linejoin="round" />
    
    <!-- Dynamic Quantum Energy Core -->
    <circle cx="60" cy="66" r="22" fill="url(#nexusGrad)" opacity="0.9" filter="url(#glow)"/>
    <circle cx="60" cy="66" r="10" fill="#FFFFFF"/>
    
    <!-- Orbiting Energy Arcs -->
    <path d="M 35 45 Q 60 25 85 45" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" opacity="0.8"/>
    <path d="M 35 88 Q 60 108 85 88" fill="none" stroke="#FFFFFF" stroke-width="3" stroke-linecap="round" opacity="0.8"/>
    
    <!-- Accent Nodes -->
    <circle cx="110" cy="38" r="4" fill="{secondary_color}" />
    <circle cx="10" cy="95" r="4" fill="{primary_color}" />
  </g>

  <!-- Brand Typography -->
  <text x="210" y="105" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif" font-size="58" font-weight="800" letter-spacing="-1" fill="#FFFFFF">
    {brand_name}<tspan fill="{secondary_color}">.</tspan>
  </text>
  
  <text x="212" y="145" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif" font-size="16" font-weight="600" letter-spacing="4" fill="#94A3B8">
    {tag.upper().replace('&', '&amp;')}
  </text>
</svg>"""
    return svg


def generate_app_icon(primary_color: str = "#6366F1", secondary_color: str = "#06B6D4") -> str:
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
  <defs>
    <linearGradient id="iconBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1E1B4B" />
      <stop offset="100%" stop-color="#0F172A" />
    </linearGradient>
    <linearGradient id="emblemGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{primary_color}" />
      <stop offset="100%" stop-color="{secondary_color}" />
    </linearGradient>
    <filter id="iconGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="16" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>

  <!-- Squircle App Icon Base -->
  <rect width="512" height="512" rx="115" fill="url(#iconBg)" />
  <rect width="504" height="504" x="4" y="4" rx="111" fill="none" stroke="#334155" stroke-width="2" opacity="0.4"/>

  <!-- Icon Geometric Emblem -->
  <g transform="translate(136, 136)">
    <!-- Outer Hex -->
    <polygon points="120,20 220,77 220,190 120,247 20,190 20,77" fill="none" stroke="url(#emblemGrad)" stroke-width="14" stroke-linejoin="round" />
    
    <!-- Central Core -->
    <circle cx="120" cy="133" r="48" fill="url(#emblemGrad)" filter="url(#iconGlow)"/>
    <circle cx="120" cy="133" r="22" fill="#FFFFFF"/>
    
    <!-- Dynamic Orbiting Energy -->
    <path d="M 70 90 Q 120 50 170 90" fill="none" stroke="#FFFFFF" stroke-width="7" stroke-linecap="round" opacity="0.9"/>
    <path d="M 70 176 Q 120 216 170 176" fill="none" stroke="#FFFFFF" stroke-width="7" stroke-linecap="round" opacity="0.9"/>
  </g>
</svg>"""
    return svg


def generate_monochrome_logo(brand_name: str, dark_mode: bool = True) -> str:
    fg = "#FFFFFF" if dark_mode else "#0F172A"
    bg = "#0B0F19" if dark_mode else "#F8FAFC"
    
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 160" width="600" height="160">
  <rect width="100%" height="100%" rx="12" fill="{bg}"/>
  <g transform="translate(50, 30)">
    <polygon points="50,10 90,33 90,80 50,103 10,80 10,33" fill="none" stroke="{fg}" stroke-width="5" stroke-linejoin="round" />
    <circle cx="50" cy="56" r="18" fill="{fg}"/>
  </g>
  <text x="170" y="88" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="48" font-weight="800" letter-spacing="-1" fill="{fg}">
    {brand_name}
  </text>
</svg>"""
    return svg


def build_complete_brand_suite(brand_name: str = "NEXUSAURA", tagline: str = "Autonomous Intelligence & Next-Gen Cloud"):
    print(f"[+] Generating Complete Brand Identity Suite for: {brand_name}")
    
    # 1. Primary Full Logo
    h_logo = generate_horizontal_logo(brand_name, tagline)
    (OUT_DIR / "logo_primary_dark.svg").write_text(h_logo, encoding="utf-8")
    
    # 2. Square App Icon / Favicon
    app_icon = generate_app_icon()
    (OUT_DIR / "app_icon_512.svg").write_text(app_icon, encoding="utf-8")
    (OUT_DIR / "favicon.svg").write_text(app_icon, encoding="utf-8")
    
    # 3. Monochrome Variants
    mono_dark = generate_monochrome_logo(brand_name, dark_mode=True)
    mono_light = generate_monochrome_logo(brand_name, dark_mode=False)
    (OUT_DIR / "logo_monochrome_dark.svg").write_text(mono_dark, encoding="utf-8")
    (OUT_DIR / "logo_monochrome_light.svg").write_text(mono_light, encoding="utf-8")
    
    # 4. Brand Guidelines Document
    guidelines = f"""# Brand Style Guidelines & Design System
## Project: {brand_name}
**Tagline**: {tagline}  
**Lead Designer**: Aryan Kumar (`aryankumar9412`) â€” 8 Years Engineering & Design Experience  
**Package Tier**: Enterprise Brand Identity Suite

---

## 1. Color Palette System

| Role | Color Name | Hex Code | RGB | Usage |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Accent** | Electric Indigo | `#6366F1` | `rgb(99, 102, 241)` | Main emblems, primary CTAs, active states |
| **Secondary Accent** | Cyber Cyan | `#06B6D4` | `rgb(6, 182, 212)` | Glow gradients, highlights, badges |
| **Deep Background** | Void Obsidian | `#0B0F19` | `rgb(11, 15, 25)` | Primary canvas, dark mode surfaces |
| **Elevated Surface** | Slate Shadow | `#1E293B` | `rgb(30, 41, 59)` | Cards, dialogs, borders |
| **High Contrast Text** | Pure Pearl | `#FFFFFF` | `rgb(255, 255, 255)` | Primary typography, high visibility nodes |
| **Muted Text** | Cool Slate | `#94A3B8` | `rgb(148, 163, 184)` | Secondary text, captions, metadata |

---

## 2. Typography Rules
* **Primary Display Font**: Inter / SF Pro Display / System Sans-Serif
* **Headline Weights**: `Font-Weight: 800` (Extrabold) with `-1px` letter spacing
* **Subheadings / Taglines**: `Font-Weight: 600` (Semibold) with `+4px` tracking (all caps)
* **Body Copy**: `Font-Weight: 400` / `500` with `1.6` line-height

---

## 3. Clear Space & Minimum Sizes
* **Clear Space Rule**: Maintain an exclusion margin equal to the height of the inner core circle (`22px` relative) around all edges.
* **Minimum Digital Size**:
  * Horizontal Lockup: Minimum `160px` wide.
  * App Icon: Minimum `32x32px` for browser favicons.
* **Vector Scalability**: All vector SVG files are infinitely scalable with 0 raster artifacting.

---

## 4. Deliverables Manifest
1. `logo_primary_dark.svg`: Full horizontal lockup on dark background.
2. `app_icon_512.svg`: Standard 512x512 app store & mobile squircle icon.
3. `favicon.svg`: Ultra-crisp vector browser favicon.
4. `logo_monochrome_dark.svg`: Pure white monochrome lockup for single-color dark prints.
5. `logo_monochrome_light.svg`: Slate monochrome lockup for white document letterheads.
"""
    (OUT_DIR / "BRAND_STYLE_GUIDELINES.md").write_text(guidelines, encoding="utf-8")
    print(f"[✓] Brand identity suite created at: {OUT_DIR}")


if __name__ == "__main__":
    build_complete_brand_suite()
