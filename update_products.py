import os
import re

html_file = 'wireline-tools-accessories.html'
pdf_folder = 'reproductbrochureofscubeindustrieswirelineslickli5'

pdf_mapping = {
    "ALLIGATOR GRAB": "ALLIGATOR GRAB.pdf",
    "Alligator Grabs": "ALLIGATOR GRAB.pdf",
    "BLIND BOX": "BLIND BOX.pdf",
    "Blind Box": "BLIND BOX.pdf",
    "BULL DOG SPEAR": "BULL DOG SPEAR.pdf",
    "Bull Dog Spears": "BULL DOG SPEAR.pdf",
    "FLUTED CENTRALISER": "FLUTED CENTRALISER.pdf",
    "Fluted Centralizers": "FLUTED CENTRALISER.pdf",
    "IMPRESSION BLOCK": "IMPRESSION BLOCK.pdf",
    "Impression Blocks": "IMPRESSION BLOCK.pdf",
    "MAGNETIC FISHING TOOL": "MAGNETIC FISHING TOOL.pdf",
    "Magnetic Fishing Tools": "MAGNETIC FISHING TOOL.pdf",
    "Multi-Roller Wheel Fluted Centraliser": "MULTI ROLLER WHEEL FLUTED CENTRALISER.pdf",
    "Releasable Collect Bull Dog Spears": "RELEASABLE COLLET BULL DOG SPEAR.pdf",
    "Releasable Collet Bull Dog Spears": "RELEASABLE COLLET BULL DOG SPEAR.pdf",
    "SKATE SYSTEM": "SKATE SYSTEM.pdf",
    "Skate System": "SKATE SYSTEM.pdf",
    "WIRELINE FISHING MAGNET": "WIRELINE FISHING MAGNET.pdf",
    "Wireline Fishing Magnets": "WIRELINE FISHING MAGNET.pdf"
}

image_mapping = {
    "Multi-Roller Wheel Fluted Centraliser": "MULTI ROLLER WHEEL FLUTED CENTRALIZER.png",
    "Releasable Collect Bull Dog Spears": "RELEASABLE COLLET BULL DOG SPEAR.png",
    "Releasable Collet Bull Dog Spears": "RELEASABLE COLLET BULL DOG SPEAR.png"
}

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# First replace "Releasable Collect Bull Dog Spears" with "Releasable Collet Bull Dog Spears"
content = content.replace("Releasable Collect Bull Dog Spears", "Releasable Collet Bull Dog Spears")

cards = content.split('<div class="wireline-product-card-body"')
new_content = cards[0]

for card in cards[1:]:
    # Find the title
    title_match = re.search(r'<h5[^>]*>([^<]+)</h5>', card)
    if title_match:
        title = title_match.group(1).strip()
        
        # Add PDF
        if title in pdf_mapping:
            pdf_file = pdf_mapping[title]
            pdf_path = f"{pdf_folder}/{pdf_file}".replace(' ', '%20').replace('&', '%26')
            
            # Check if it already has a link to THIS pdf or any pdf.
            if f'href="{pdf_path}"' not in card:
                link_html = f'\n<a class="btn btn-sm btn-outline-primary d-block mb-2 text-start" href="{pdf_path}" target="_blank" title="Download {title.title()} Technical Brochure"><i class="fas fa-file-pdf text-danger me-2"></i> {title.title()}</a>\n'
                
                h5_end = card.find('</h5>')
                if h5_end != -1:
                    first_div_close = card.find('</div>', h5_end)
                    if first_div_close != -1:
                        card = card[:first_div_close] + link_html + card[first_div_close:]
                        print(f"Added PDF for {title}")

    new_content += '<div class="wireline-product-card-body"' + card

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

# Now for the images, they are often located in the `<div class="wireline-product-card">` which is BEFORE `<div class="wireline-product-card-body"`.
# So we need to do a different approach to replace the image. We can just regex replace the img src for these specific products.

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# For Multi-Roller Wheel Fluted Centraliser
# Previous: <img alt="Multi-Roller Wheel Fluted Centraliser" class="wireline-product-img" src="wireline/Multi-Roller%20Wheel%20Fluted%20Centraliser.jpg"
# We'll just replace the whole tag or find it.
img_pattern_mr = re.compile(r'<img[^>]*alt="Multi-Roller Wheel Fluted Centraliser"[^>]*>')
def repl_mr(m):
    return f'<img alt="Multi-Roller Wheel Fluted Centraliser" class="wireline-product-img" src="{pdf_folder}/MULTI%20ROLLER%20WHEEL%20FLUTED%20CENTRALIZER.png" style="width: 100%; height: 100%; object-fit: contain; padding: 15px;" />'
content = img_pattern_mr.sub(repl_mr, content)

# For Releasable Collet Bull Dog Spears
img_pattern_rc = re.compile(r'<img[^>]*alt="Releasable Collet Bull Dog Spears"[^>]*>')
def repl_rc(m):
    return f'<img alt="Releasable Collet Bull Dog Spears" class="wireline-product-img" src="{pdf_folder}/RELEASABLE%20COLLET%20BULL%20DOG%20SPEAR.png" style="width: 100%; height: 100%; object-fit: contain; padding: 15px;" />'
content = img_pattern_rc.sub(repl_rc, content)

# Note: The alt attribute for Releasable Collet Bull Dog Spears might still be "Releasable Collect Bull Dog Spears" in the img tag because our string replace replaced it!
# Wait, `content.replace("Releasable Collect Bull Dog Spears", "Releasable Collet Bull Dog Spears")` was done on the HTML, so the alt attribute IS NOW "Releasable Collet Bull Dog Spears". So the regex works!

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Images updated successfully")
