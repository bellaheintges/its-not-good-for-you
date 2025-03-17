# Table  2.  Creator information
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
    "Creator Followed": ["organicallyaddison", "dr.vegann", "veganchefmaya", "nobodyknowsmereally.vent", "bruh_justhot",
                          "helptoweightloss", "lowcarblove", "johnderting", "scaseyfitness", "blankitacisneros",
                          "stephgrassodietitian", "bart.wgsd", "petecataldo", "appleuser3995580", "dr.tommymartin",
                          "kiraswldiary_", "shakaylafelice", "dr.rachelpaul", "dr.kojosarfo", "mamaaronn",
                          "channy.fit", "l.ssvnrise", "ericrobertsfitness", "rachel.steward.fitness", "forgedbyfit",
                          "cnpfitness_", "findfoodfreedom", "nickrosenski", "slavicglan", "emma.currivan",
                          "patrickhongfit", "thewodfather", "heloomelloo", "iampeachye1", "skydoesfitness",
                          "ray2fitness", "i.f_fitness", "iamnotrealbleat", "thebuffunicorn", "dikarter",
                          "meeraefirkins", "ugcwithkaytelynn", "nutrition.corner_", "fine..fashion2", "jessicaplayfair",
                          "millyondollargirl", "hannahholthealth", "sororitynutritionist", "rumorzachariaa", "fitnfineewithpenelope"],
    "# of Followers": [80300, 43600, 71200, "N/A", 7019,
                     9491, 2000000, 4600000, 2800000, 64600,
                     2200000, 12100, 750, 88, 2500000,
                     1551, 164400, 688700, 2500000, 11100,
                     251300, 11400, 1500000, 259900, 8882,
                     "N/A", 672900, 234000, 779, 21000,
                     245000, 331, 492900, 1500000, 853900,
                     38400, 12100, 34500, 502600, 188,
                     330, 3518, 10400, 148500, 21500,
                     38100, 45500, 391600, 136000, 443300],
    "# of Likes": [3100000, 7500000, 49500, "N/A", 619100,
                 464200, 23000000, 110600000, 28400000, 2700000,
                 33900000, 124200, 14200, 59, 53800000,
                 91000, 3200000, 8400000, 73400000, 674500,
                 4400000, 377700, 39200000, 5900000, 19800,
                 "N/A", 7500000, 23700000, 37800, 523100,
                 4100000, 3561, 20800000, 70000000, 13900000,
                 1300000, 83000, 1500000, 28700000, 802,
                 1457, 81800, 161400, 9600000, 1000000,
                 1000000, 2000000, 8300000, 4700000, 2800000],
    "Creator Content": ["Nutrition & recipes", "Vegan health", "Healthy cooking", "Dieting & weight loss", "Fitness motivation",
                         "Weight loss tips", "Low-carb diet", "Nature & travel", "Fitness & health", "Personal training",
                         "Dietitian advice", "Workout tips", "Health coaching", "General fitness", "Doctor insights",
                         "Weight loss journey", "Plant-based lifestyle", "Nutrition science", "Mental health & well-being", "Detox & cleanse",
                         "Strength training", "Bodybuilding", "Fitness motivation", "Workout routines", "Body transformation",
                         "Food freedom", "Mindful eating", "Zero-calorie foods", "Thinspiration", "Weight management",
                         "Personal fitness", "CrossFit training", "Beauty & body trends", "Weight loss journey", "Muscle building",
                         "Fat burning", "Intermittent fasting", "Caloric deficit", "Strength & conditioning", "Extreme dieting",
                         "Meal prepping", "Body toning", "Healthy lifestyle", "Fashion & aesthetics", "Weight loss myths",
                         "Slimming techniques", "Restrictive dieting", "Caloric control", "Cutting phase", "Fitness & wellness"],
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
