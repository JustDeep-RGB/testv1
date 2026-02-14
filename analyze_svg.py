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
    
    width_match = re.search(r'width="(\d+)"', svg_tag)
    if not width_match: return
    width = float(width_match.group(1))
    
    print(f"\n--- SVG Width: {width} ---")
    
    # regex for paths
    # Capture d and fill
    paths = re.findall(r'<path[^>]*d="([^"]+)"[^>]*fill="([^"]+)"', inner_content)
    
    clusters = collections.defaultdict(list)
    
    for d, fill in paths:
        cx = get_path_centroid_x(d)
        if cx == -1: continue
        
        # Bin by 10% buckets
        bucket = int((cx / width) * 10) * 10
        clusters[bucket].append(fill)
        
    for bucket in sorted(clusters.keys()):
        fills = clusters[bucket]
        counts = collections.Counter(fills)
        print(f"  X-Range {bucket}%-{bucket+10}%: {len(fills)} paths. Colors: {dict(counts)}")

pattern = r'(<svg[^>]*width="(?:1512|768|427)"[^>]*>)(.*?)(</svg>)'
re.sub(pattern, analyze_svg, content, flags=re.DOTALL)
