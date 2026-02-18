
import os

file_path = r'c:\Users\JasD\OneDrive\Desktop\website\hackwavev1\colosseum.com\breakout\resources.html'

timeline_html = """          <div class="relative max-w-4xl mx-auto py-12 px-4 sm:px-6 lg:px-8">
            <div class="absolute top-0 bottom-0 left-1/2 w-1 bg-breakout-black transform -translate-x-1/2 hidden md:block"></div>
            
            <!-- Timeline Item 1 -->
            <div class="relative z-10 mb-12 md:mb-24 group">
              <div class="flex flex-col md:flex-row items-center justify-between w-full">
                <div class="order-1 w-full md:w-5/12 md:text-right mb-4 md:mb-0">
                  <h3 class="font-anime-ace-3bb font-bold text-xl text-breakout-black group-hover:text-breakout-blue transition-colors duration-300">Registration Opens</h3>
                  <p class="font-anime-ace-3bb font-normal text-breakout-black mt-2 text-sm">Sign-ups officially open for Hackwave 2.0. Secure your spot early.</p>
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
                  <h3 class="font-anime-ace-3bb font-bold text-xl text-breakout-black group-hover:text-breakout-green transition-colors duration-300">Hackathon Begins</h3>
                  <p class="font-anime-ace-3bb font-normal text-breakout-black mt-2 text-sm">The building phase kicks off. Start coding your projects!</p>
                  <span class="inline-block mt-2 px-3 py-1 bg-breakout-black text-white font-anime-ace-3bb text-xs border-2 border-breakout-black rounded">Feb 1, 2026</span>
                </div>
              </div>
            </div>

            <!-- Timeline Item 3 -->
            <div class="relative z-10 mb-12 md:mb-24 group">
              <div class="flex flex-col md:flex-row items-center justify-between w-full">
                <div class="order-1 w-full md:w-5/12 md:text-right mb-4 md:mb-0">
                  <h3 class="font-anime-ace-3bb font-bold text-xl text-breakout-black group-hover:text-breakout-purple transition-colors duration-300">Submission Deadline</h3>
                  <p class="font-anime-ace-3bb font-normal text-breakout-black mt-2 text-sm">Final deadline to submit your projects for review.</p>
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
                  <h3 class="font-anime-ace-3bb font-bold text-xl text-breakout-black group-hover:text-breakout-orange transition-colors duration-300">Winners Announced</h3>
                  <p class="font-anime-ace-3bb font-normal text-breakout-black mt-2 text-sm">Winning teams and prizes are revealed globally.</p>
                  <span class="inline-block mt-2 px-3 py-1 bg-breakout-black text-white font-anime-ace-3bb text-xs border-2 border-breakout-black rounded">Apr 1, 2026</span>
                </div>
              </div>
            </div>
          </div>
"""

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Keep lines 0 to 609 (inclusive, so 0-610 slice in python? No, line 610 is where we start deleting)
# Line 610 is index 609.
# We want to keep lines[:609] (lines 1 to 609)
# Insert timeline
# Keep lines from 986 onwards?
# Line 986 in file is `</section>`. We delete up to 986.
# So we keep from 986 (index 986, which is line 987).
# Let's verify line count.
# 610 is line index 609.
# 986 is line index 985.
# We want to remove 609 to 985 inclusive.
# So lines[:609] + new + lines[986:]

new_content = "".join(lines[:609]) + timeline_html + "".join(lines[986:])

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Successfully replaced content with timeline.")
