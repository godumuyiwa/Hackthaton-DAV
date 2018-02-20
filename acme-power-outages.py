#converting ap_surge.csv to a dict object
import csv
reader = csv.reader(open('ap_surge.csv', 'r'))
ap_surge = {}
next(reader, None)
for row in reader:
    k, v = row
    ap_surge[k] = v


#converting data in dict from strings to integers
ap_surge_int ={}
for key in ap_surge.keys():
    int_key = int(key)
    int_values =float(ap_surge[key])
    ap_surge_int[int_key] =int_values
    #print(type(ap_surge_int[int_key]))
#print(ap_surge_int)

## checking for surges in data in the ap_surge dict

normal_power_threshold = 4.9
count = 0
for readings in ap_surge_int.values():
    if readings > normal_power_threshold:
        count = count + 1
        keyholder = ap_surge_int[readings]
        next_keyholder =keyholder + 1
        if ap_surge_int[next_keyholder] > normal_power_threshold:
            print "surge detected"
print "The total number of surge detected is", count





