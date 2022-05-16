import csv

merged = []

for num in range(1, 5):
    print(f'Loading results({str(num)}).csv...')
    with open(f'./csv/results ({str(num)}).csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            merged.append(row)

sorted_result = sorted(merged, key=lambda d: d['createdAt'])

with open('./csv/merged.csv', 'w', newline='') as file:
    fieldnames = ['createdAt', 'externalId', 'userId']
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for dict in sorted_result:
        writer.writerow({'createdAt': dict['createdAt'],
                         'externalId': dict['externalId'], 'userId': dict['userId']})

print('Created merged.csv')
