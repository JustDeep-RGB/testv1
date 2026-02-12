$targetDir = $PSScriptRoot

# Branding Elements
$brandingLight = '<span class="text-breakout-black font-anime-ace-3bb text-2xl md:text-4xl lg:text-5xl italic font-bold uppercase leading-none transition-all duration-300 hover:scale-105 tracking-wider">HACKWAVE 2.0</span>'
$brandingDark = '<span class="text-white font-anime-ace-3bb text-2xl md:text-4xl lg:text-5xl italic font-bold uppercase leading-none transition-all duration-300 hover:scale-105 tracking-wider">HACKWAVE 2.0</span>'

# Regex Patterns
# 1. Light Header Logo (Inline SVG inside specific anchor)
# Matches <a href="...breakout.html" class="flex items-center self-stretch"><svg...></svg></a>
$lightLogoPattern = '(<a href="[^"]*breakout\.html" class="flex items-center self-stretch">\s*)(<svg[\s\S]*?</svg>|\s*<span[\s\S]*?</span>\s*)(\s*</a>)'

# 1b. Light Footer Logo (Inline SVG inside specific anchor - no self-stretch)
# Matches <a href="...breakout.html" class="flex items-center"><svg...></svg></a>
$lightFooterLogoPattern = '(<a href="[^"]*breakout\.html" class="flex items-center">\s*)(<svg[\s\S]*?</svg>|\s*<span[\s\S]*?</span>\s*)(\s*</a>)'

# 2. Dark Header Logo (Image tag)
# Matches <a href="...index.html"...><img...colosseum-logo-white.svg...></a>
$darkLogoPattern = '(<a href="[^"]*index\.html"[^>]*>\s*)(<img[^>]*colosseum-logo-white\.svg[^>]*>|\s*HACKWAVE\s*2\.0\s*)(\s*</a>)'

$files = Get-ChildItem -Path $targetDir -Recurse -Filter *.html

foreach ($file in $files) {
    try {
        $content = Get-Content -Path $file.FullName -Raw -Encoding UTF8
        $originalContent = $content

        # 1. Update Title
        if ($content -notmatch "HACKWAVE 2.0") {
            $content = $content -replace '<title>.*?</title>', '<title>HACKWAVE 2.0</title>'
        }

        # 2. Update Meta Description
        $content = $content.Replace('content="Solana Breakout Online Hackathon"', 'content="HACKWAVE 2.0"')
        $content = $content.Replace('content="Colosseum is a platform combining hackathons, accelerators, and a venture fund focused on supercharging the Solana ecosystem."', 'content="HACKWAVE 2.0"')
        $content = $content.Replace('content="Welcome to Colosseum"', 'content="HACKWAVE 2.0"')

        # 3. Replace Light Logo (Header)
        $content = [regex]::Replace($content, $lightLogoPattern, {
                param($match)
                return $match.Groups[1].Value + $brandingLight + $match.Groups[3].Value
            })

        # 3b. Replace Light Logo (Footer)
        $content = [regex]::Replace($content, $lightFooterLogoPattern, {
                param($match)
                return $match.Groups[1].Value + $brandingLight + $match.Groups[3].Value
            })

        # 3c. Apply Translucent Header to Resources Page (and similar)
        # Matches the specific nav-container in resources.html and adds the style if missing
        # Updated to also remove centering classes for full-width look
        $resourcesNavPattern = '(<div id="nav-container" class="fixed)(?: left-1/2)?( top-0 z-50 flex w-full)(?: max-w-\[1512px\])?(?: -translate-x-1/2)?(?: px-0)?( xl:)(?:top-3 )?(px-4 2xl:px-0")(?![^>]*style=)(>)'
        $translucentStyle = ' style="background-color: rgba(255, 255, 255, 0.8); backdrop-filter: blur(8px); -webkit-backdrop-filter: blur(8px);"'
        
        $content = [regex]::Replace($content, $resourcesNavPattern, {
                param($match)
                # Reconstruct the tag without the captured optional groups (centering/width classes)
                return $match.Groups[1].Value + $match.Groups[2].Value + $match.Groups[3].Value + $match.Groups[4].Value + $translucentStyle + $match.Groups[5].Value
            })

        # 4. Replace Dark Logo
        $content = [regex]::Replace($content, $darkLogoPattern, {
                param($match)
                return $match.Groups[1].Value + $brandingDark + $match.Groups[3].Value
            })

        # 5. General Cleanup
        $content = $content.Replace("Colosseum Breakout Hackathon", "HACKWAVE 2.0")

        if ($content -ne $originalContent) {
            Set-Content -Path $file.FullName -Value $content -Encoding UTF8
            Write-Host "Updated: $($file.Name)"
        }
        else {
            Write-Host "No changes matched: $($file.Name)"
        }
    }
    catch {
        Write-Host "Error updating $($file.Name): $_"
    }
}
Write-Host "Update complete."
