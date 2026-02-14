import re

html_path = '/home/jas-d/Desktop/hack-web/testv1/index.html'
b64_path = '/home/jas-d/Desktop/hack-web/testv1/hackwave_logo_b64.txt'

with open(b64_path, 'r') as f:
    b64_data = f.read().strip()

with open(html_path, 'r') as f:
    content = f.read()

# 1. Inject Base64 Image
# Find the img tag we added earlier
# <img src="..." ... alt="HackWave" ...>
img_pattern = r'<img src="[^"]+" alt="HackWave"([^>]+)>'
# Replace src with data uri
def img_replacer(match):
    attrs = match.group(1)
    return f'<img src="data:image/png;base64,{b64_data}" alt="HackWave"{attrs}>'

new_content = re.sub(img_pattern, img_replacer, content)

# 2. Add Debug Style to SVGs
# Target 1512, 768, 427 width SVGs
# Add style="opacity: 0.1; border: 5px solid red;"
# Be careful if style attr already exists? (usually not in these SVGs based on snippets)
# Snippet: <svg ... xmlns="...">
# We can append style before xmlns or after width.

def svg_styler(match):
    tag = match.group(0) # The opening <svg ... >
    if 'style=' in tag:
        # Append to existing style? Too complex.
        # Just replace class?
        return tag.replace('<svg', '<svg style="opacity: 0.1; border: 5px solid red; background: rgba(0,0,0,0.5);"')
    else:
        return tag.replace('<svg', '<svg style="opacity: 0.1; border: 5px solid red; background: rgba(0,0,0,0.5);"')

svg_pattern = r'<svg[^>]*width="(?:1512|768|427)"[^>]*>'
new_content = re.sub(svg_pattern, svg_styler, new_content)

with open(html_path, 'w') as f:
    f.write(new_content)

print("Injected Base64 Image and Applied Debug Styles to SVGs.")
