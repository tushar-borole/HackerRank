input_number=map(int,raw_input().strip().split(" "))
total_no_subject=input_number[1]
list_data=[]
for data in range(total_no_subject):
    list_data.append(map(float,raw_input().strip().split(" ")))

zipped_data=map(list,zip(*list_data))
for data in zipped_data:
    average_count=sum(data)/total_no_subject
    print average_count

