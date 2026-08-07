import sys

html_file = 'wireline-tools-accessories.html'
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

target = '<div class="row g-4 mb-4"><div class="col-md-6 col-lg-3">'
insertion = '''<div class="row g-4 mb-4">
<div class="col-md-6 col-lg-3">
<div class="wireline-product-card">
<div class="wireline-product-img-wrapper" style="position: relative; height: 250px; overflow: hidden; background: #ffffff; display: flex; align-items: center; justify-content: center;">
<img alt="RELEASABLE COLLET BULL DOG SPEAR" class="wireline-product-img" src="reproductbrochureofscubeindustrieswirelineslickli5/RELEASABLE%20COLLET%20BULL%20DOG%20SPEAR.png" style="width: 100%; height: 100%; object-fit: contain; padding: 15px;"/>
</div>
<div class="wireline-product-card-body" style="padding: 20px; flex-grow: 1; display: flex; flex-direction: column;">
<h5 class="wireline-product-title" style="font-size: 1rem; font-weight: 600; color: #02204c; margin-bottom: 10px; text-transform: uppercase;">RELEASABLE COLLET BULL DOG SPEAR</h5>
<p class="wireline-product-desc" style="font-size: 0.85rem; color: #666; line-height: 1.5; flex-grow: 1;">Premium releasable collet bull dog spear engineered for high-performance well intervention operations.</p>
<a class="btn btn-sm btn-outline-primary d-block mb-2 text-start" href="reproductbrochureofscubeindustrieswirelineslickli5/RELEASABLE%20COLLET%20BULL%20DOG%20SPEAR.pdf" target="_blank" title="Download Releasable Collet Bull Dog Spear Technical Brochure"><i class="fas fa-file-pdf text-danger me-2"></i> Releasable Collet Bull Dog Spear</a>
</div>
</div>
</div>
<div class="col-md-6 col-lg-3">
<div class="wireline-product-card">
<div class="wireline-product-img-wrapper" style="position: relative; height: 250px; overflow: hidden; background: #ffffff; display: flex; align-items: center; justify-content: center;">
<img alt="MULTI ROLLER WHEEL FLUTED CENTRALIZER" class="wireline-product-img" src="reproductbrochureofscubeindustrieswirelineslickli5/MULTI%20ROLLER%20WHEEL%20FLUTED%20CENTRALIZER.png" style="width: 100%; height: 100%; object-fit: contain; padding: 15px;"/>
</div>
<div class="wireline-product-card-body" style="padding: 20px; flex-grow: 1; display: flex; flex-direction: column;">
<h5 class="wireline-product-title" style="font-size: 1rem; font-weight: 600; color: #02204c; margin-bottom: 10px; text-transform: uppercase;">MULTI ROLLER WHEEL FLUTED CENTRALIZER</h5>
<p class="wireline-product-desc" style="font-size: 0.85rem; color: #666; line-height: 1.5; flex-grow: 1;">Advanced multi-roller wheel fluted centralizer designed to center wireline tool strings and reduce friction.</p>
<a class="btn btn-sm btn-outline-primary d-block mb-2 text-start" href="reproductbrochureofscubeindustrieswirelineslickli5/MULTI%20ROLLER%20WHEEL%20FLUTED%20CENTRALISER.pdf" target="_blank" title="Download Multi Roller Wheel Fluted Centralizer Technical Brochure"><i class="fas fa-file-pdf text-danger me-2"></i> Multi Roller Wheel Fluted Centralizer</a>
</div>
</div>
</div>
<div class="col-md-6 col-lg-3">'''

if target in content:
    content = content.replace(target, insertion, 1)
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Successfully inserted new products.')
else:
    print('Target not found in the file.')
