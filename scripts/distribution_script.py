import json

with open('data.json') as json_file:
    result = {}
    data = json.load(json_file)
    #each year
    for line in data:
        year_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        year = line['Country Name']
        values = line.values()
        #each country
        itervalues = iter(values)
        next(itervalues)
        for entry in itervalues:
            try:
                entry = int(entry)
                if entry <= 10:
                    year_data[0] += 1
                elif entry > 10 and entry <= 20 :
                    year_data[1] += 1
                elif entry > 20 and entry <= 30 :
                    year_data[2] += 1
                elif entry > 30 and entry <= 40 :
                    year_data[3] += 1
                elif entry > 40 and entry <= 50 :
                    year_data[4] += 1
                elif entry > 50 and entry <= 60 :
                    year_data[5] += 1
                elif entry > 60 and entry <= 70 :
                    year_data[6] += 1
                elif entry > 70 and entry <= 80 :
                    year_data[7] += 1
                elif entry > 80 and entry <= 90 :
                    year_data[8] += 1
                elif entry > 90 and entry <= 100 :
                    year_data[9] += 1
                elif entry > 100 and entry <= 110 :
                    year_data[10] += 1
                elif entry > 110 and entry <= 120 :
                    year_data[11] += 1
                elif entry > 120 and entry <= 130 :
                    year_data[12] += 1
                elif entry > 130 and entry <= 140 :
                    year_data[13] += 1
                elif entry > 140 and entry <= 150 :
                    year_data[14] += 1
                elif entry > 150 and entry <= 160 :
                    year_data[15] += 1
                elif entry > 160 and entry <= 170 :
                    year_data[16] += 1
                elif entry > 170 and entry <= 180 :
                    year_data[17] += 1
                elif entry > 180 and entry <= 190 :
                    year_data[18] += 1
                elif entry > 190 and entry <= 200 :
                    year_data[19] += 1      
                elif entry > 200:
                    year_data[20] += 1
            except:
                pass
        result[year] = year_data

    with open('freq_data.json', 'w') as fp:
        json.dump(result, fp)





