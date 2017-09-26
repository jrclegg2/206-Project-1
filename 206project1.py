import os
import csv
import filecmp
from operator import itemgetter
# Jack Clegg - SI 206 - Fall '17' - Project 1
def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys will come from the first row in the data.

#Note: The column headings will not change from the
#test cases below, but the the data itself will
#change (contents and size) in the different test
#cases.
	open_file = open(file, 'r')
	read_file = csv.reader(open_file)
	list_of_people = [(First, Last, Email, Class, DOB) for (First, Last, Email, Class, DOB) in list(read_file)[1:]]
	list_of_dicts_of_people = []
	for person in list_of_people:
	    personal_dict = {}
	    personal_dict['First'] = person [0]
	    personal_dict['Last'] = person [1]
	    personal_dict['Email'] = person [2]
	    personal_dict['Class'] = person [3]
	    personal_dict['DOB'] = person [4]
	    list_of_dicts_of_people.append(personal_dict)
	return (list_of_dicts_of_people)

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName
  if col == 'First':
      sorted_list_of_people = sorted(data, key=itemgetter('First'))
      first_person = sorted_list_of_people [0]
      first_last = ''
      first_last += first_person['First']
      first_last += ' '
      first_last += first_person ['Last']
      return first_last
  if col == 'Last':
      sorted_list_of_people = sorted(data, key=itemgetter('Last'))
      first_person = sorted_list_of_people [0]
      first_last = ''
      first_last += first_person['First']
      first_last += ' '
      first_last += first_person ['Last']
      return first_last
  if col == 'Email':
      sorted_list_of_people = sorted(data, key=itemgetter('Email'))
      first_person = sorted_list_of_people [0]
      first_last = ''
      first_last += first_person['First']
      first_last += ' '
      first_last += first_person ['Last']
      return first_last
#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	dict_class_count = {}
	for person in data:
	    class_standing = person['Class']
	    dict_class_count[class_standing] = dict_class_count.get(class_standing, 0) + 1
	tuples_class_standing = list(zip(dict_class_count.keys(), dict_class_count.values()))
	sorted_tuples = sorted(tuples_class_standing, key = lambda x : x[1], reverse = True)
	return sorted_tuples
# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
  dict_day_count = {}
  for person in a:
      dob_split = person['DOB'].split('/')
      dict_day_count[dob_split[1]] = dict_day_count.get(dob_split[1], 0) + 1
  sorted_dict_day_count = sorted(dict_day_count.items(), key = itemgetter(1), reverse = True)
  return int(sorted_dict_day_count[0][0])
# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
  total_years = 0
  for person in a:
      year = 2017
      birthday = person['DOB']
      birth_year = int((birthday.split('/'))[2])
      age_years = year - birth_year
      total_years += age_years
  total_people = len(a)
  average_age = int(total_years / total_people)
  return average_age
#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None
	def personData(dict_person):
	     first_name = dict_person['First']
	     last_name = dict_person['Last']
	     email = dict_person['Email']
	     return (first_name, last_name, email)
	emptyfile = open(fileName, 'w', newline = '\n')
	if col == 'First':
	    sorted_list_of_people = sorted(a, key=itemgetter('First'))
	    for person in sorted_list_of_people:
	        personal_data = personData(person)
	        emptyfile.write('{},{},{}\n'.format(*personal_data))
	    emptyfile.close
	if col == 'Last':
	        sorted_list_of_people = sorted(a, key=itemgetter('Last'))
	        for person in sorted_list_of_people:
	            personal_data = personData(person)
	            emptyfile.write('{},{},{}\n'.format(*personal_data))
	        emptyfile.close
	if col == 'Email':
	        sorted_list_of_people = sorted(a, key=itemgetter('Email'))
	        for person in sorted_list_of_people:
	            personal_data = personData(person)
	            emptyfile.write('{},{},{}\n'.format(*personal_data))
	        emptyfile.close

################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)

	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()
