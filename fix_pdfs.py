import os
import re

html_file = 'wireline-tools-accessories.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. JD PULLING TOOL
# Find: <h5 class="wireline-product-title" style="font-size: 1rem; font-weight: 600; color: #02204c; margin-bottom: 10px; text-transform: uppercase;">JD PULLING TOOL</h5>
# Replace with: same + \n<a class="btn btn-sm btn-outline-primary d-block mb-2 text-start" href="pdffoldertoadd/JD%20&%20JU%20SERIES%20PULLING%20TOOL.pdf" target="_blank" title="Download JD PULLING TOOL Technical Brochure"><i class="fas fa-file-pdf text-danger me-2"></i> JD PULLING TOOL</a>
jd_find = '<h5 class="wireline-product-title" style="font-size: 1rem; font-weight: 600; color: #02204c; margin-bottom: 10px; text-transform: uppercase;">JD PULLING TOOL</h5>'
jd_repl = jd_find + '\n<a class="btn btn-sm btn-outline-primary d-block mb-2 text-start" href="pdffoldertoadd/JD%20&%20JU%20SERIES%20PULLING%20TOOL.pdf" target="_blank" title="Download JD PULLING TOOL Technical Brochure"><i class="fas fa-file-pdf text-danger me-2"></i> JD PULLING TOOL</a>'
content = content.replace(jd_find, jd_repl)

# 2. PULLING TOOL S SERIES
pts_find = '<h5 class="wireline-product-title" style="font-size: 1rem; font-weight: 600; color: #02204c; margin-bottom: 10px; text-transform: uppercase;">PULLING TOOL S SERIES</h5>'
pts_repl = pts_find + '\n<a class="btn btn-sm btn-outline-primary d-block mb-2 text-start" href="pdffoldertoadd/PULLING%20TOOL%20S%20SERIES.pdf" target="_blank" title="Download PULLING TOOL S SERIES Technical Brochure"><i class="fas fa-file-pdf text-danger me-2"></i> PULLING TOOL S SERIES</a>'
content = content.replace(pts_find, pts_repl)

# 3. SELF RELEASING OVERSHOT - fix wrong PDF
sro_find = '<a class="btn btn-sm btn-outline-primary d-block mb-2 text-start" href="pdffoldertoadd/RELEASABLE%20OVERSHOT.pdf" target="_blank" title="Download SELF RELEASING OVERSHOT Technical Brochure"><i class="fas fa-file-pdf text-danger me-2"></i> SELF RELEASING OVERSHOT</a>'
sro_repl = '<a class="btn btn-sm btn-outline-primary d-block mb-2 text-start" href="pdffoldertoadd/SELF%20RELEASABLE%20OVERSHOT.pdf" target="_blank" title="Download SELF RELEASING OVERSHOT Technical Brochure"><i class="fas fa-file-pdf text-danger me-2"></i> SELF RELEASING OVERSHOT</a>'
content = content.replace(sro_find, sro_repl)

# 4. KNUCKLE SWIVEL JOINT (Line 521-525)
# Wait, this one has a description paragraph:
# <h5 class="wireline-product-title"...>KNUCKLE SWIVEL JOINT</h5>
# <p class="wireline-product-desc"...>Heavy-duty knuckle swivel joint...</p>
# </div>
ksj_find = '<p class="wireline-product-desc" style="font-size: 0.85rem; color: #666; line-height: 1.5; flex-grow: 1;">Heavy-duty knuckle swivel joint allowing 360-degree rotation and angular flexibility to prevent tool string torque and bind.</p>'
ksj_repl = ksj_find + '\n<a class="btn btn-sm btn-outline-primary d-block mb-2 text-start" href="pdffoldertoadd/KNUCKLE%20SWIVEL%20JOINT.pdf" target="_blank" title="Download KNUCKLE SWIVEL JOINT Technical Brochure"><i class="fas fa-file-pdf text-danger me-2"></i> KNUCKLE SWIVEL JOINT</a>'
content = content.replace(ksj_find, ksj_repl)

# 5. TUBING PERFORATOR PUNCH (Line 790-794)
# <p class="wireline-product-desc"...>Mechanical tubing perforator punch engineered to punch communication holes in tubing walls for circulation or drainage.</p>
tpp_find = '<p class="wireline-product-desc" style="font-size: 0.85rem; color: #666; line-height: 1.5; flex-grow: 1;">Mechanical tubing perforator punch engineered to punch communication holes in tubing walls for circulation or drainage.</p>'
tpp_repl = tpp_find + '\n<a class="btn btn-sm btn-outline-primary d-block mb-2 text-start" href="pdffoldertoadd/TUBING%20PERFORATOR%20PUNCH.pdf" target="_blank" title="Download TUBING PERFORATOR PUNCH Technical Brochure"><i class="fas fa-file-pdf text-danger me-2"></i> TUBING PERFORATOR PUNCH</a>'
content = content.replace(tpp_find, tpp_repl)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("PDFs linked successfully!")
