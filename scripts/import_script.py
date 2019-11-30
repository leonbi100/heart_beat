from beat_site.models import Country
import csv
import itertools

with open('data/countries.csv') as r, open('data/gdp.csv') as f, open('data/co2.csv') as d:
    country_reader = csv.reader(r)
    reader = csv.reader(f)
    coreader = csv.reader(d)

    iterrow = iter(reader)
    next(iterrow)
    citerrow = iter(country_reader)
    next(citerrow)
    coiter = iter(coreader)
    next(coiter)

    for country_row, co2_row in itertools.zip_longest(citerrow, coiter):
        for i in range(2, len(country_row)):
            if country_row[i] != "":
                try:
                    co2 = float(co2_row[i])
                    # gdp = float(row[i])
                    year = 1960 + i - 2
                    country = country_row[0]
                    curr_rate = float(country_row[58])
                    rate = float(country_row[i])
                    created = Country.objects.get_or_create(
                        name=country,
                        gdp=Country.objects.get(rate=rate).gdp,
                        year=year,
                        curr_rate=curr_rate,
                        rate=rate,
                        co2=co2
                        )
                except:
                    pass

# with open('data/countries.csv') as f:
#         reader = csv.reader(f)
#         iterrow = iter(reader)
#         next(iterrow)
#         for row in iterrow:
#             for i in range(2, len(row)):
#                 if row[i] != "":
#                     rate = float(row[i])
#                     year = 1960 + i - 2
#                     country = row[0]
#                     # curr_rate = row[58]
#                     created = Country.objects.update_or_create(
#                         name=country,
#                         rate=rate,
#                         year=year
#                         # curr_rate=curr_rate
#                         )