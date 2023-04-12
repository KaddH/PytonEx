file_path = "C:\class_colon.txt"
data_dict = {}

with open(file_path, "r") as f:
    for line in f:
        id, *data = line.strip().split(":")
        data_dict[id] = tuple(data)

for k in data_dict :
    print(k, data_dict[k])

smax = 0; midx =0
for k in data_dict :
    if int(data_dict[k][1]) > smax:
        smax = int(data_dict[k][1])
        midx = k
print('최대 수강인원은 = ', midx, ':', data_dict[midx])

snumList = []
for k in data_dict :
    idata = int(data_dict[k][1])
    snumList.append(idata)

print('리스트 함수이용 : 최대 수강인원은 = ', max(snumList))