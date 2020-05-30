total = 0

with open('pricesDone.csv') as games:
    for line in games:
        gameid, name, price = line.split(',')
        if (price.rstrip() != "Price"):
            total += float(price.rstrip())

print(round(total,2))