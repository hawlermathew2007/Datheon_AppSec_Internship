import xml.etree.ElementTree as ET
from urllib.parse import urlparse, urlunparse
from pathlib import Path

SITEMAP_FILE = Path("../recon/docs/sitemap.xml")
LINKS_FILE = Path("../recon/docs/datheon_links.txt")
API_FILE = Path("../recon/docs/datheon_potential_api.txt")

# API versions to generate
API_PREFIXES = [
    "/api",
    "/api/v1",
    "/api/v2",
    "/api/v3",
    "/api/v4",
    "/api/v5",
]


def extract_urls(sitemap_file):
    tree = ET.parse(sitemap_file)
    root = tree.getroot()

    urls = []

    for loc in root.iter():
        if loc.tag.endswith("loc") and loc.text:
            urls.append(loc.text.strip())

    return urls


def generate_api_urls(url):
    parsed = urlparse(url)

    api_urls = []

    for prefix in API_PREFIXES:
        # Insert API prefix before the original URL path
        new_path = prefix + parsed.path

        api_url = urlunparse((
            parsed.scheme,
            parsed.netloc,
            new_path,
            parsed.params,
            parsed.query,
            parsed.fragment
        ))

        api_urls.append(api_url)

    return api_urls


def main():
    urls = extract_urls(SITEMAP_FILE)

    potential_api_urls = []

    for url in urls:
        potential_api_urls.extend(generate_api_urls(url))

    # Remove duplicates while preserving order
    potential_api_urls = list(dict.fromkeys(potential_api_urls))

    # Write original URLs
    with open(LINKS_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(urls))

    # Write potential API URLs
    with open(API_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(potential_api_urls))

    print(f"[+] Extracted {len(urls)} URLs")
    print(f"[+] Generated {len(potential_api_urls)} potential API URLs")
    print(f"[+] Saved to {LINKS_FILE}")
    print(f"[+] Saved to {API_FILE}")


if __name__ == "__main__":
    main()
