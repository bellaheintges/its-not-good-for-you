# Table  1.  Hashtags searched on each account corresponding to the creators followed
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
    "Hashtag Searched": ["#friends", "#love", "#mushrooms", "#ocean", "#water",
                          "#robot", "#spectrum", "#lung", "#ball", "#star",
                          "#monopoly", "#animals", "#laser", "#vision", "#circle",
                          "#respect", "#grow", "#queen", "#drill", "#grill",
                          "#mosaic", "#happy", "#frog", "#scrapbook", "#snowman",
                          "#flicker", "#orbit", "#velvet", "#lipstick", "#paint",
                          "#money", "#respect", "#cherry", "#pickle", "#soccer",
                          "#real", "#necklace", "#pig", "#lipstick", "#jupiter",
                          "#gingerbread", "#hat", "#ball", "#witch", "#penguin",
                          "#money", "#apple", "#computer", "#geography", "#ring"],
    "Creator Followed": ["ernieqfish", "darxycracra", "vivispamm_0", "physicians_formula", "serenebloomm",
                          "trendy_viewz", "saranne_wrap", "instituteofhumananatomy", "charitymermaidpirate", "elysianescape",
                          "amarynax_", "thefeatheryflock", "guinutil", "sicr3t.acc0unt", "andrewivx2.0",
                          "silviogabriel77", "wavyy.bvby", "user381929201", "stxmx", "grillz.queen",
                          "theartrevival", "isla.moonadevntures", "pampermoony", "taylortysenn", "wrizzposts69",
                          ".im_n0t_a_pers0n", "littlepoisontree", "modernbymb", "briohni", "messybynature2025",
                          "linkyanime", "are.you.okay.15", "azziyaaa_", "cookiterica", "sporf",
                          "e.l_083848", "theholynecklace", "_gabeybabey", "mydlvz1", "astrospaceq",
                          "themainstreetduo", "rancherhatstore", "soccer_5711", "empathvibez", "whitecatt03",
                          "tealoes2up", "apple.mood", "wzzqo", "jordan_the_stallion8", "getrealwithalix"]
}

df = pd.DataFrame(data)

fig, ax = plt.subplots(figsize=(10, 5))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='left', loc='center', colWidths=[0.05, 0.2, 0.3])

for key, cell in table.get_celld().items():
    if key[0] == 0 or (key[1] == 0 and df.iloc[key[0]-1, 0] != ""):
        cell.set_text_props(weight='bold')
    if key[1] == 0:
        cell.set_text_props(weight='bold', ha='center')
    if key[0] > 0 and ((key[0]-1) // 5) % 2 == 1:
        cell.set_facecolor("lightgray")

plt.show()
