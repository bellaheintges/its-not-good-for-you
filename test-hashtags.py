# Table  1.  Hashtags searched on each account corresponding to the creators followed
# TikTok Test

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
    "Hashtag Searched": ["#keto", "#vegan", "#abs", "#lowcalorie", "#sugarfree",
                          "#skinny", "#lowcarb", "#water", "#eggwhites", "#trainer",
                          "#nutrition", "#macros", "#portioncontrol", "#healthy", "#BMI",
                          "#wl", "#plant-based", "#protein", "#binge", "#detox",
                          "#exercise", "#workout", "#caloriecounting", "#BMR", "#body",
                          "#mindfuleating", "#yoyodiet", "#zerocalorie", "#thin", "#scale",
                          "#thigh", "#highcardio", "#hourglassfigure", "#loseweight", "#bodyfat",
                          "#fatburn", "#fasting", "#lean", "#shredded", "#caloriedeficit",
                          "#mealprep", "#fitbod", "#fastmetabolism", "#thinarms", "#under100cal",
                          "#skinnylegend", "#restricting", "#lowfat", "#cuttingcals", "#fatloss"],
    "Creator Followed": ["organicallyaddison", "dr.vegann", "veganchefmaya", "nobodyknowsmereally.vent", "bruh_justhot",
                          "helptoweightloss", "lowcarblove", "johnderting", "scaseyfitness", "blankitacisneros",
                          "stephgrassodietitian", "bart.wgsd", "petecataldo", "appleuser3995580", "dr.tommymartin",
                          "kiraswldiary_", "shakaylafelice", "dr.rachelpaul", "dr.kojosarfo", "mamaaronn",
                          "channy.fit", "l.ssvnrise", "ericrobertsfitness", "rachel.steward.fitness", "forgedbyfit",
                          "cnpfitness_", "findfoodfreedom", "nickrosenski", "slavicglan", "emma.currivan",
                          "patrickhongfit", "thewodfather", "heloomelloo", "iampeachye1", "skydoesfitness",
                          "ray2fitness", "i.f_fitness", "iamnotrealbleat", "thebuffunicorn", "dikarter",
                          "meeraefirkins", "ugcwithkaytelynn", "nutrition.corner_", "fine..fashion2", "jessicaplayfair",
                          "millyondollargirl", "hannahholthealth", "sororitynutritionist", "rumorzachariaa", "fitnfineewithpenelope"]
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
