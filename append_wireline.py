import os

html_file = 'wireline-tools-accessories.html'
folder = 'WIRELINE-TOOLS-AND-ACCESSORIES'

if os.path.exists(folder):
    images = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.png', '.jpeg', '.gif', '.avif', '.webp'))]
    images.sort(key=lambda x: x.lower())
    
    html_content = ""
    for img in images:
        name = os.path.splitext(img)[0]
        img_src = f"{folder}/{img}".replace(' ', '%20')
        html_content += f'''            <div class="col-md-6 col-lg-3">
                <div class="wireline-product-card">
                    <div class="wireline-product-img-wrapper" style="position: relative; height: 250px; overflow: hidden; background: #f8f9fa; display: flex; align-items: center; justify-content: center;">
                        <img src="{img_src}" class="wireline-product-img" style="width: 100%; height: 100%; object-fit: contain; padding: 15px;" alt="{name}">
                    </div>
                    <div class="wireline-product-card-body" style="padding: 20px; flex-grow: 1; display: flex; flex-direction: column;">
                        <h5 class="wireline-product-title" style="font-size: 1rem; font-weight: 600; color: #02204c; margin-bottom: 10px; text-transform: uppercase;">{name}</h5>
                    </div>
                </div>
            </div>\n'''

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the end of the row. The row ends with `</div></div>\n    </div>\n</section>`
    # The last product card ends with `</div>\n            </div>`
    # then `</div></div>` which closes the row and container
    
    start_marker = '<div class="row g-4">'
    start_idx = content.find(start_marker)
    if start_idx != -1:
        end_idx = content.find('        </div></div>', start_idx)
        if end_idx != -1:
            new_content = content[:end_idx] + html_content + content[end_idx:]
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("Appended successfully")
        else:
            print("End marker not found")
    else:
        print("Start marker not found")
else:
    print("Folder not found")
