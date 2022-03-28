import csv

new_data = []
mapper = []
result = []

with open('./csv/new_sql_out.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        new_data.append(row)

with open('./csv/mapper.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        mapper.append(row)

existing_ids = [d['userId'] for d in mapper]
new_ids = [d['user_id'] for d in new_data]
added_ids = list(filter(lambda id: id not in existing_ids, new_ids))
removed_ids = list(filter(lambda id: id not in new_ids, existing_ids))

for dict in mapper:
    if dict['userId'] in new_ids:
        item = {'internalId': dict['userId'],
                'externalId': dict['externalId'], 'createdAt': dict['createdAt']}
        result.append(item)

sorted_result = sorted(result, key=lambda d: d['createdAt'])

with open('./csv/result.csv', 'w', newline='') as csvfile:
    fieldnames = ['createdAt', 'externalId', 'internalId']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for dict in sorted_result:
        writer.writerow({'createdAt': dict['createdAt'],
                         'externalId': dict['externalId'], 'internalId': dict['internalId']})

for id in removed_ids:
    print(id)
