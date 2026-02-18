
$filePath = "c:\Users\JasD\OneDrive\Desktop\website\hackwavev1\colosseum.com\breakout\resources.html"
$timelineHtml = @"
          <div class="relative max-w-4xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
            <div class="absolute top-0 bottom-0 left-1/2 w-1 bg-breakout-black transform -translate-x-1/2 hidden md:block"></div>
            
            <!-- Timeline Item 1 -->
            <div class="relative z-10 mb-12 md:mb-24 group">
              <div class="flex flex-col md:flex-row items-center justify-between w-full">
                <div class="order-1 w-full md:w-5/12 md:text-right mb-4 md:mb-0">
                  <h3 class="font-anime-ace-3bb text-xl text-breakout-black group-hover:text-breakout-blue transition-colors duration-300">Registration Opens</h3>
                  <p class="font-geist text-breakout-black mt-2">Sign-ups officially open for Hackwave 2.0. Secure your spot early.</p>
                  <span class="inline-block mt-2 px-3 py-1 bg-breakout-black text-white font-anime-ace-3bb text-xs border-2 border-breakout-black rounded">Jan 15, 2026</span>
                </div>
                <div class="z-20 flex items-center order-1 bg-white border-4 border-breakout-black w-10 h-10 rounded-full justify-center absolute left-1/2 transform -translate-x-1/2 hidden md:flex">
                  <div class="w-4 h-4 bg-breakout-black rounded-full"></div>
                </div>
                <div class="order-1 w-full md:w-5/12 px-6 py-4"></div>
              </div>
            </div>

            <!-- Timeline Item 2 -->
            <div class="relative z-10 mb-12 md:mb-24 group">
              <div class="flex flex-col md:flex-row items-center justify-between w-full">
                <div class="order-1 w-full md:w-5/12 px-6 py-4 md:order-last"></div>
                <div class="z-20 flex items-center order-1 bg-white border-4 border-breakout-black w-10 h-10 rounded-full justify-center absolute left-1/2 transform -translate-x-1/2 hidden md:flex">
                  <div class="w-4 h-4 bg-breakout-black rounded-full"></div>
                </div>
                <div class="order-1 w-full md:w-5/12 mb-4 md:mb-0">
                  <h3 class="font-anime-ace-3bb text-xl text-breakout-black group-hover:text-breakout-green transition-colors duration-300">Hackathon Begins</h3>
                  <p class="font-geist text-breakout-black mt-2">The building phase kicks off. Start coding your projects!</p>
                  <span class="inline-block mt-2 px-3 py-1 bg-breakout-black text-white font-anime-ace-3bb text-xs border-2 border-breakout-black rounded">Feb 1, 2026</span>
                </div>
              </div>
            </div>

            <!-- Timeline Item 3 -->
            <div class="relative z-10 mb-12 md:mb-24 group">
              <div class="flex flex-col md:flex-row items-center justify-between w-full">
                <div class="order-1 w-full md:w-5/12 md:text-right mb-4 md:mb-0">
                  <h3 class="font-anime-ace-3bb text-xl text-breakout-black group-hover:text-breakout-purple transition-colors duration-300">Submission Deadline</h3>
                  <p class="font-geist text-breakout-black mt-2">Final deadline to submit your projects for review.</p>
                  <span class="inline-block mt-2 px-3 py-1 bg-breakout-black text-white font-anime-ace-3bb text-xs border-2 border-breakout-black rounded">Mar 15, 2026</span>
                </div>
                <div class="z-20 flex items-center order-1 bg-white border-4 border-breakout-black w-10 h-10 rounded-full justify-center absolute left-1/2 transform -translate-x-1/2 hidden md:flex">
                  <div class="w-4 h-4 bg-breakout-black rounded-full"></div>
                </div>
                <div class="order-1 w-full md:w-5/12 px-6 py-4"></div>
              </div>
            </div>

            <!-- Timeline Item 4 -->
            <div class="relative z-10 group">
              <div class="flex flex-col md:flex-row items-center justify-between w-full">
                <div class="order-1 w-full md:w-5/12 px-6 py-4 md:order-last"></div>
                <div class="z-20 flex items-center order-1 bg-white border-4 border-breakout-black w-10 h-10 rounded-full justify-center absolute left-1/2 transform -translate-x-1/2 hidden md:flex">
                  <div class="w-4 h-4 bg-breakout-black rounded-full"></div>
                </div>
                <div class="order-1 w-full md:w-5/12 mb-4 md:mb-0">
                  <h3 class="font-anime-ace-3bb text-xl text-breakout-black group-hover:text-breakout-orange transition-colors duration-300">Winners Announced</h3>
                  <p class="font-geist text-breakout-black mt-2">Winning teams and prizes are revealed globally.</p>
                  <span class="inline-block mt-2 px-3 py-1 bg-breakout-black text-white font-anime-ace-3bb text-xs border-2 border-breakout-black rounded">Apr 1, 2026</span>
                </div>
              </div>
            </div>
          </div>
"@

$lines = Get-Content -Path $filePath
# We need to replace lines 610 to 986 (1-based from Python script logic).
# PowerShell arrays are 0-based.
# line 610 is index 609.
# line 986 is index 985.
# We want to keep 0..608 (first 609 lines).
# Insert new content.
# Keep 986..end (from index 986).

$head = $lines[0..608]
$tail = $lines[986..($lines.Count - 1)]

# Create temp file to avoid encoding issues with direct manipulation if possible, but Set-Content is fine usually.
$newContent = $head + $timelineHtml + $tail
$newContent | Set-Content -Path $filePath -Encoding UTF8
Write-Host "Replaced timeline content in $filePath"
