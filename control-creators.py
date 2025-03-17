# Table  2.  Creator information
# TikTok Control

import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Day": ["1", "", "", "", "",
            "2", "", "", "", "",
            "3", "", "", "", "",
            "4", "", "", "", "",
            "5", "", "", "", "",
            "6", "", "", "", "",
            "7", "", "", "", "",
            "8", "", "", "", "",
            "9", "", "", "", "",
            "10", "", "", "", ""],
    "Creator Followed": ["ernieqfish", "darxycracra", "vivispamm_0", "physicians_formula", "serenebloomm",
                          "trendy_viewz", "saranne_wrap", "instituteofhumananatomy", "charitymermaidpirate", "elysianescape",
                          "amarynax_", "thefeatheryflock", "guinutil", "_sicr3t.acc0unt_", "andrewivx2.0",
                          "silviogabriel77", "wavyy.bvby", "user381929201", "stxmx", "grillz.queen",
                          "theartrevival", "isla.moonadevntures", "pampermoony", "taylortysenn", "wrizzposts69",
                          ".im_n0t_a_pers0n", "littlepoisontree", "modernbymb", "briohni", "messybynature2025",
                          "linkyanime", "are.you.okay.15", "azziyaaa_", "cookiterica", "sporf",
                          "e.l_083848", "theholynecklace", "_gabeybabey", "mydlvz1", "astrospaceq",
                          "themainstreetduo", "rancherhatstore", "soccer_5711", "empathvibez", "whitecatt03",
                          "tealoes2up", "apple.mood", "wzzqo", "jordan_the_stallion8", "getrealwithalix"],
    "# of Followers": [2025, 285, "N/A", 45900, 41800,
                     719500, 305000, 10700000, 86000, 115000,
                     3833, 332, 1800000, 66, 4300000,
                     1900000, 671700, 19900, 17700, 496500,
                     144700, 1800000, 732400, 284, 66800,
                     795, 228, 220100, 68000, 1637,
                     8699, 498600, 98600, 3200000, 851400,
                     27600, 52500, 851200, 24600, 4000000,
                     114100, 103800, 14800, 9550, 90800,
                     117400, 44600, 7118, 13900000, 3838],
    "# of Likes": [22200, 60600, 345000, 157100, 7600000,
                 47000000, 15000000, 113800000, 2200000, 6400000,
                 1300000, 8773, 49400000, 9563, 120700000,
                 94400000, 13200000, 8400000, 912300, 23000000,
                 18700000, 34400000, 19300000, 2487, 3000000,
                 37300, 55800, 3600000, 9600000, 39600,
                 43600, 39600000, 5400000, 146800000, 28700000,
                 4600000, 2000000, 56400000, 3500000, 197900000,
                 26700000, 1300000, 924200, 21000, 15800000,
                 3700000, 1600000, 1100000, 630500000, 320600],
    "Creator Content": ["Travel-related, fishing, hiking", "Various", "Various", "Makeup products, brand page", "Sunsets, beaches",
                         "Popular content/news", "Various", "Information about the body", "DIY crafts and tutorials", "Edits of stars, space, sky",
                         "Various", "Pet bird videos", "Scary edits", "Love edits/manifestation", "How to...",
                         "Various edits", "Various", "Aesthetic edits", "Drill dancing videos", "Grillz/jewelry making",
                         "Arts over time", "Passion for nature", "Famous frog account", "Scrapbooking", "Meme account",
                         "Gaming edits", "Various edits", "Fashion brand", "Makeup reviews", "Acrylic painting",
                         "Random edits", "Random edits", "Random ideas", "Cooking recipes", "Viral home-sports vids",
                         "Edits/memes", "Christian jewelry brand", "Pet pig account", "Mom lifestyle account", "Space edits",
                         "Couple on Disney adventures", "Hat store in TX", "Homemade soccer vids", "Eclectic witch", "Animal videos/facts",
                         "Money edits", "Apple tech. products promo", "Meme/random edit posts", "Advice/speaking to camera", "Fashion, health, wellness"],
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(25, 15))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='left', loc='left', colWidths=[0.05, 0.1, 0.1, 0.1, 0.15])

for key, cell in table.get_celld().items():
    if key[0] == 0:
        cell.set_text_props(weight='bold')
    if key[1] == 0:
        cell.set_text_props(weight='bold', ha='center')
    if key[0] > 0 and ((key[0]-1) // 5) % 2 == 1:
        cell.set_facecolor("lightgray")
plt.show()
