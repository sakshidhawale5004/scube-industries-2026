import os
import re

html_file = 'wireline-tools-accessories.html'
pdf_folder = 'pdffoldertoadd'

pdf_mapping = {
    "HYDROSTATIC BAILER": "HYDROSTATIC BAILER.pdf",
    "JD PULLING TOOL": "JD & JU SERIES PULLING TOOL.pdf",
    "KNUCKLE SWIVEL JOINT": "KNUCKLE SWIVEL JOINT.pdf",
    "PULLING TOO R SERIES": "PULLING TOOL R SERIES.pdf",
    "PULLING TOOL R SERIES": "PULLING TOOL R SERIES.pdf",
    "PULLING TOOL S SERIES": "PULLING TOOL S SERIES.pdf",
    "RELEASABLE OVERSHOT": "RELEASABLE OVERSHOT.pdf",
    "SAND PUMP BAILER": "SAND PUMP BAILER.pdf",
    "SELF RELEASING OVERSHOT": "SELF RELEASABLE OVERSHOT.pdf",
    "SIDE WALL CUTTER": "SIDE WALL CUTTER.pdf",
    "TUBING PERFORATOR PUNCH": "TUBING PERFORATOR PUNCH.pdf",
    "WIRELINE OVERSHOT": "WIRELINE OVERSHOT.pdf",
    "WIRELINE SPEAR": "WIRELINE SPEAR.pdf"
}

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# We will search for each title and insert the PDF link if it's not already there.
# Pattern to match the card body:
# <h5 class="wireline-product-title"...>TITLE</h5>
# <p ...>...</p>
# </div>

for title, pdf_file in pdf_mapping.items():
    # Find the title in the HTML
    # We want to insert the link just before the closing </div> of the card-body.
    # We'll use a regex that matches from <h5...>TITLE</h5> to the next </div>
    
    # Let's find all occurrences of this title
    pattern = r'(<h5[^>]*>\s*' + re.escape(title) + r'\s*</h5>\s*<p[^>]*>.*?</p>)(?=\s*</div>)'
    
    # We'll write a replacement function
    def replacer(match):
        block = match.group(1)
        # Check if there's already an <a> tag in this block (meaning we already added a link or it had one)
        # But wait, the <a> tag would be appended after the <p> block, so it would be inside the match if it existed?
        # Actually, if there is already a link, it might be after the <p>.
        
        # Let's just append the link
        pdf_path = f"{pdf_folder}/{pdf_file}".replace(' ', '%20').replace('&', '%26')
        link_html = f'\n<a class="btn btn-sm btn-outline-primary d-block mb-2 text-start" href="{pdf_path}" target="_blank" title="Download {title.title()} Technical Brochure"><i class="fas fa-file-pdf text-danger me-2"></i> {title.title()}</a>'
        return block + link_html

    # But wait, there are cases where the description might not be exactly <p>...</p> or there might be other things.
    # Let's do a more robust approach. We can split the content into product cards and check each.
    pass

# Better approach: split by card body
cards = content.split('<div class="wireline-product-card-body"')
new_content = cards[0]

for card in cards[1:]:
    # Find the title
    title_match = re.search(r'<h5[^>]*>([^<]+)</h5>', card)
    if title_match:
        title = title_match.group(1).strip()
        if title in pdf_mapping:
            # Check if it already has a link to this PDF or similar
            if 'fas fa-file-pdf' not in card or pdf_mapping[title] not in card:
                # Find the closing </div> of this card body
                # The card string goes up to the next '<div class="wireline-product-card-body"'
                # So we just find the last </div> before the end of this string?
                # Actually, card contains everything until the next card-body.
                # So it has </div> </div> </div> etc.
                # The first </div> that closes the wireline-product-card-body is a bit tricky to find with split.
                # Let's just find the first </div> that appears after the <p> tag?
                
                pdf_file = pdf_mapping[title]
                pdf_path = f"{pdf_folder}/{pdf_file}".replace(' ', '%20').replace('&', '%26')
                link_html = f'\n<a class="btn btn-sm btn-outline-primary d-block mb-2 text-start" href="{pdf_path}" target="_blank" title="Download {title.title()} Technical Brochure"><i class="fas fa-file-pdf text-danger me-2"></i> {title.title()}</a>\n'
                
                # We'll insert it right before the first `</div>` that appears after the `<h5` tag.
                # But wait, there might be other divs inside. No, wireline-product-card-body usually doesn't have nested divs.
                # Let's find the first </div> after </h5>
                h5_end = card.find('</h5>')
                if h5_end != -1:
                    first_div_close = card.find('</div>', h5_end)
                    if first_div_close != -1:
                        card = card[:first_div_close] + link_html + card[first_div_close:]
                        print(f"Added PDF for {title}")
    
    new_content += '<div class="wireline-product-card-body"' + card

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done")
