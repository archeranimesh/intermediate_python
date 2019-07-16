# String to List.
my_data = "this,is,a,comma,seperated,string"

# convert it to list.
my_comma_list = my_data.split(",")
print("my comma list: ", my_comma_list)

# convert it back to string
my_new_data = ",".join(my_comma_list)
print(my_new_data)

# Tuple unpacking to intialize variable
student = "XYZ,16,Maths"
name, age, subject = student.split(",")
print("-" * 10)
print(name, age, subject)

# list to set and vice versa
my_names = "XYZ, XXX, YYY, ZZZ, XYZ"
print(set(my_names.split(", ")))
print(",".join(set(my_names.split(", "))))
