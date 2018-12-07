import csv


def create_csv():
	data_list = [
	        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
	        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
	        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
	    ]

	with open('export.csv', 'w', encoding='utf-8', newline='') as f:
	    writer = csv.DictWriter(f, data_list[0].keys(), delimiter=';')
	    writer.writeheader()
	    for user in data_list:
	        writer.writerow(user)

if __name__ == '__main__':
	create_csv()