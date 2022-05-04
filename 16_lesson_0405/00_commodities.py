import json
import matplotlib.pyplot as plt

with open('series_GOLD.json') as jf:
    data = json.loads(jf.read())
    gold = data['data']['rates']  # достаю стоимости золота

quantity = []
dates = []
for date in gold:
    quantity.append(gold[date]['XAU'] * 0.0283495)
    dates.append(date)

plt.figure(figsize=(20, 7), dpi=80)


