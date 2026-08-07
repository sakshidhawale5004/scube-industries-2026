import os

html_file = 'wireline-tools-accessories.html'
img_folder = 'foldertoadd'
pdf_folder = 'pdffoldertoadd'

images = [f for f in os.listdir(img_folder) if f.lower().endswith(('.jpg', '.png', '.jpeg', '.gif', '.avif', '.webp'))]
pdfs = [f for f in os.listdir(pdf_folder) if f.lower().endswith('.pdf')]

images.sort(key=lambda x: x.lower())

def find_pdf(img_name):
    base_name = os.path.splitext(img_name)[0]
    base_lower = base_name.lower().replace(' ', '').replace('&', '').replace('series', '').replace('too', 'tool').replace('releasing', 'releasable')
    
    for pdf in pdfs:
        pdf_base = os.path.splitext(pdf)[0].lower().replace(' ', '').replace('&', '').replace('series', '')
        if base_lower in pdf_base or pdf_base in base_lower:
            return pdf
    return None

html_content = ""
for img in images:
    name = os.path.splitext(img)[0]
    img_src = f"{img_folder}/{img}".replace(' ', '%20')
    pdf_match = find_pdf(img)
    
    html_content += f'''<div class="col-md-6 col-lg-3">
<div class="wireline-product-card">
<div class="wireline-product-img-wrapper" style="position: relative; height: 250px; overflow: hidden; background: #ffffff; display: flex; align-items: center; justify-content: center;">
<img alt="{name}" class="wireline-product-img" src="{img_src}" style="width: 100%; height: 100%; object-fit: contain; padding: 15px;"/>
</div>
<div class="wireline-product-card-body" style="padding: 20px; flex-grow: 1; display: flex; flex-direction: column;">
<h5 class="wireline-product-title" style="font-size: 1rem; font-weight: 600; color: #02204c; margin-bottom: 10px; text-transform: uppercase;">{name}</h5>'''
    
    if pdf_match:
        pdf_src = f"{pdf_folder}/{pdf_match}".replace(' ', '%20')
        html_content += f'''
<a class="btn btn-sm btn-outline-primary d-block mb-2 text-start" href="{pdf_src}" target="_blank" title="Download {name} Technical Brochure"><i class="fas fa-file-pdf text-danger me-2"></i> {name}</a>'''
    
    html_content += '''
</div>
</div>
</div>
'''

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

target_marker = '</div> <!-- close row g-4 -->'
if target_marker in content:
    new_content = content.replace(target_marker, html_content + target_marker)
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully added new items to HTML.")
else:
    print("Could not find the target marker in HTML.")
