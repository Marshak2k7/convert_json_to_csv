import json
import csv

with open('sales.json', encoding='utf-8') as f:
    x = json.load(f)

f = csv.writer(open("sales.csv", "w"))

f.writerow(["item", "country", "year", "sales"])

for item in x:
    for country in item['sales_by_country']:
        for year in item['sales_by_country'].get(country):
            f.writerow([item["item"],
                        country,
                        year,
                        item['sales_by_country'].get(country).get(year)]),
