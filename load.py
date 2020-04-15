from apps.tac.models import inventory
from apps.tac.models import inventory_category
import csv



with open('inventory.csv') as f:
	reader = csv.reader(f)
	for row in reader:
		item = inventory()
		item.name = row[1]
		item.item_id = row[0]
		item.issue_allowed = row[3]
		category = inventory_category.objects.filter(name__contains=row[2])[0]
		item.item_type = category
		item.save()
		print("importing  :"+row[1])

