import csv
path= r'/Users/ethan/Desktop/CodingDojo/Week3/10.03.2016/us-500.csv'
with open (path,'rU') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print "firt_name : ", row['first_name']
        print "last_name : ", row['last_name']
        print "company_name : ", row['company_name']
        print "address : ", row['address']
        print "city : ", row['city']
        print "county : ", row['county']
        print "state : ", row['state']
        print "zip : ", row['zip']
        print "phone1 : ", row['phone1']
        print "phone2 : ", row['phone2']
        print "email : ", row['email']
        print "web : ", row['web']
        print "-----------------"
