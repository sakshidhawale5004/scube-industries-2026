import os
import urllib.parse

html_file = 'wireline-tools-accessories.html'
folder = 'Slickline & Wirelinescube'

if os.path.exists(folder):
    images = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.png', '.jpeg', '.gif', '.avif', '.webp'))]
    images.sort(key=lambda x: x.lower())
    
    html_content = ""
    for img in images:
        name = os.path.splitext(img)[0]
        # properly encode the path so that it works in HTML
        # HTML escaping for & and url escaping for spaces
        # But looking at existing ones like "Slickline &amp; Wireline Tools/Wireline Snipper.jpg", 
        # let's just do exactly that.
        folder_html = "Slickline &amp; Wirelinescube"
        img_escaped = img.replace(' ', '%20').replace('&', '%26')
        folder_escaped = folder.replace(' ', '%20').replace('&', '%26')
        src = f"{folder_escaped}/{img_escaped}"
        
        html_content += f'''<div class="col-md-6 col-lg-3">
<div class="wireline-product-card">
<div class="wireline-product-img-wrapper" style="position: relative; height: 250px; overflow: hidden; background: #ffffff; display: flex; align-items: center; justify-content: center;">
<img alt="{name}" class="wireline-product-img" src="{src}" style="width: 100%; height: 100%; object-fit: contain; padding: 15px;"/>
</div>
<div class="wireline-product-card-body" style="padding: 20px; flex-grow: 1; display: flex; flex-direction: column;">
<h5 class="wireline-product-title" style="font-size: 1rem; font-weight: 600; color: #02204c; margin-bottom: 10px; text-transform: uppercase;">{name}</h5>
</div>
</div>
</div>
'''

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    marker = '</div> <!-- close row g-4 -->'
    if marker in content:
        new_content = content.replace(marker, html_content + marker)
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Appended successfully")
    else:
        print("Marker not found")
else:
    print("Folder not found")
