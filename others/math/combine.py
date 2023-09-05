#For Plying Path of Exile and its Jewels
import itertools
mods_choices = ["Increased Attack Speed with Bows",
                "Increased Maximum Life",
                "Increased Burning Damage",
                "Increased Fire Damage over Time Multiplier/Damage over Time Multiplier",
                "Increased Damage over Time Multiplier",
                "Increased Attack Speed",
                "Increased Damage over Time"]

Jewels = {}

for i in range(2, 4):
    for combination in itertools.combinations(mods_choices, i):
        Jewels[combination] = None

print(Jewels)