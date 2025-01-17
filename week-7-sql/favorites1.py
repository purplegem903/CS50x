import csv

with open("favorites.csv", "r") as file:
    reader = csv.DictReader(file)
    counts = {}
    for row in reader:
        favorite = row["language"]
        if favorite in counts:
            counts[favorite] += 1
        else:
            counts[favorite] = 1


def get_value(language):
    return counts[language]


# for favorite in counts:   # or in sorted(counts, reverse=True):
for favorite in sorted(counts, key=get_value, reverse=True):  # to sort by counts
    print(f"{favorite}: {counts[favorite]}")
