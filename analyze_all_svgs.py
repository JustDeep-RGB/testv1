import re
import collections

file_path = '/home/jas-d/Desktop/hack-web/testv1/index.html'

with open(file_path, 'r') as f:
    content = f.read()

def get_path_centroid_x(d_str):
    nums = [float(x) for x in re.findall(r'-?\d*\.?\d+', d_str)]
    if not nums: return -1
    xs = nums[0::2]
    if not xs: return -1
    return sum(xs) / len(xs)

def analyze_svg(match):
    svg_tag = match.group(1)
    inner_content = match.group(2)
    
    # Try to find width, else Unknown
    width_match = re.search(r'width="(\d+)"', svg_tag)
    width = float(width_match.group(1)) if width_match else "Unknown"
    
    print(f"\n--- SVG Width: {width} (Tag: {svg_tag[:100]}...) ---")
    
    paths = re.findall(r'<path[^>]*d="([^"]+)"[^>]*fill="([^"]+)"', inner_content)
    print(f"  Total Paths: {len(paths)}")
    
    # Check for specific logo colors
    logo_colors = ['#56BC6C', '#DABAF5', '#FFD233', '#FF7E46', '#87CDF7']
    found_logo_colors = []
    for d, fill in paths:
        if fill in logo_colors:
            found_logo_colors.append(fill)
            
    if found_logo_colors:
        counts = collections.Counter(found_logo_colors)
        print(f"  POTENTIAL LOGO FOUND! Colors: {dict(counts)}")

# Match ALL svgs
pattern = r'(<svg[^>]*>)(.*?)(</svg>)'
re.sub(pattern, analyze_svg, content, flags=re.DOTALL)
