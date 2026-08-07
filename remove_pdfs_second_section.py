import re

html_file = 'wireline-tools-accessories.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the section "Our Wireline/Slickline Tools"
idx = content.find('Our Wireline/Slickline Tools')
if idx != -1:
    section_content = content[idx:]
    
    # Remove all PDF links that were added.
    # The pattern matches: <a ... fas fa-file-pdf ... </a>
    # We will look for <a class="btn btn-sm btn-outline-primary d-block mb-2 text-start" href=... fas fa-file-pdf text-danger me-2 ... </a>
    pattern = r'\n?\s*<a class="btn btn-sm btn-outline-primary d-block mb-2 text-start"[^>]*href="pdffoldertoadd/[^>]*>.*?fas fa-file-pdf.*?</a>\n?'
    
    cleaned_section = re.sub(pattern, '\n', section_content)
    
    # Replace the section in the original content
    new_content = content[:idx] + cleaned_section
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Removed PDFs from the specified section.")
else:
    print("Section not found.")
