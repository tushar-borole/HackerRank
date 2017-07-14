def target_number(arr, targetnumber):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] != arr[j] and i != j:
                if arr[i] + arr[j] == targetnumber:
                    return True



    return False



print target_number([1,2,3,4,5], 15)  #return true
print target_number([1,1],2)     #should truen False as numbe is duplicate