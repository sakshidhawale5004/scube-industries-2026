import os

html_file = 'wireline-tools-accessories.html'
folder = 'foldertoadd'
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

images = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.png', '.jpeg', '.gif', '.avif', '.webp', '.PNG', '.png'))]
images.sort(key=lambda x: x.lower())

html_content = "\n"
for img in images:
    name = os.path.splitext(img)[0]
    img_src = f"{folder}/{img}".replace(' ', '%20')
    
    # Check if there is a mapped PDF
    pdf_html = ""
    if name in pdf_mapping:
        pdf_file = pdf_mapping[name]
        pdf_path = f"{pdf_folder}/{pdf_file}".replace(' ', '%20').replace('&', '%26')
        pdf_html = f'\n<a class="btn btn-sm btn-outline-primary d-block mb-2 text-start" href="{pdf_path}" target="_blank" title="Download {name.title()} Technical Brochure"><i class="fas fa-file-pdf text-danger me-2"></i> {name.title()}</a>'

    html_content += f'''<div class="col-md-6 col-lg-3">
<div class="wireline-product-card">
<div class="wireline-product-img-wrapper" style="position: relative; height: 250px; overflow: hidden; background: #ffffff; display: flex; align-items: center; justify-content: center;">
<img src="{img_src}" class="wireline-product-img" style="width: 100%; height: 100%; object-fit: contain; padding: 15px;" alt="{name}">
</div>
<div class="wireline-product-card-body" style="padding: 20px; flex-grow: 1; display: flex; flex-direction: column;">
<h5 class="wireline-product-title" style="font-size: 1rem; font-weight: 600; color: #02204c; margin-bottom: 10px; text-transform: uppercase;">{name}</h5>
<p class="wireline-product-desc" style="font-size: 0.85rem; color: #666; line-height: 1.5; flex-grow: 1;">Premium {name.lower()} engineered for high-performance well intervention operations.</p>{pdf_html}
</div>
</div>
</div>\n'''

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<div class="row g-4 mb-4">'
start_idx = content.find(start_marker)

end_section = content.find('</section>', start_idx)
end_idx = content.rfind('</div></div>', start_idx, end_section)

if start_idx != -1 and end_idx != -1:
    new_content = content[:end_idx] + '</div>' + html_content + '</div>' + content[end_idx+12:]
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Done")
else:
    print("Error finding markers")
