import os
import re

# Configuration
target_dir = os.path.dirname(os.path.abspath(__file__))

# Branding Element (Light Mode / Standard - Black Text)
# Used on light backgrounds like breakout.html and breakout/resources.html
branding_light = """<span class="text-breakout-black font-anime-ace-3bb text-2xl md:text-4xl lg:text-5xl italic font-bold uppercase leading-none transition-all duration-300 hover:scale-105 tracking-wider">HACKWAVE
                  2.0</span>"""

# Branding Element (Dark Mode - White Text)
# Used on dark backgrounds like accelerator.html and hackathon.html
branding_dark = """<span class="text-white font-anime-ace-3bb text-2xl md:text-4xl lg:text-5xl italic font-bold uppercase leading-none transition-all duration-300 hover:scale-105 tracking-wider">HACKWAVE
                  2.0</span>"""

# Regex Patterns
title_pattern = r'<title>.*?</title>'

# 1. Light Header Logo (Inline SVG inside specific anchor)
# Found in breakout.html, breakout/resources.html
# We match the anchor and replace the SVG inside it.
light_logo_pattern = r'(<a href="[^"]*breakout\.html" class="flex items-center self-stretch">\s*)(<svg[\s\S]*?</svg>|\s*<span[\s\S]*?</span>\s*)(\s*</a>)'

# 2. Dark Header Logo (Image tag)
# Found in accelerator.html, hackathon.html, etc.
# Match anchor pointing to index.html with the colosseum-logo-white.svg inside.
dark_logo_pattern = r'(<a href="[^"]*index\.html"[^>]*>\s*)(<img[^>]*colosseum-logo-white\.svg[^>]*>|\s*HACKWAVE\s*2\.0\s*)(\s*</a>)'

def update_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # 1. Update Title
        if "HACKWAVE 2.0" not in content:
             content = re.sub(title_pattern, '<title>HACKWAVE 2.0</title>', content)

        # 2. Update Meta Description
        # Replace specific old strings if found
        content = content.replace('content="Solana Breakout Online Hackathon"', 'content="HACKWAVE 2.0"')
        content = content.replace('content="Colosseum is a platform combining hackathons, accelerators, and a venture fund focused on supercharging the Solana ecosystem."', 'content="HACKWAVE 2.0"')
        content = content.replace('content="Welcome to Colosseum"', 'content="HACKWAVE 2.0"')

        # 3. Replace Light Logo (SVG)
        # Using a function to inject content ensures we don't mess up groups
        content = re.sub(light_logo_pattern, lambda m: f'{m.group(1)}{branding_light}{m.group(3)}', content)

        # 4. Replace Dark Logo (Img)
        content = re.sub(dark_logo_pattern, lambda m: f'{m.group(1)}{branding_dark}{m.group(3)}', content)
        
        # 5. General Cleanup (Careful with this)
        content = content.replace("Colosseum Breakout Hackathon", "HACKWAVE 2.0")

        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {file_path}")
        else:
            print(f"No changes matched: {file_path}")

    except Exception as e:
        print(f"Error updating {file_path}: {e}")

def main():
    print("Starting global branding update...")
    for root, dirs, files in os.walk(target_dir):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                update_file(file_path)
    print("Update complete.")

if __name__ == "__main__":
    main()
