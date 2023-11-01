# message = "BCAADDDCCACACAC"
message = "FFLPPFLPLNLPTPPPNFPF"
c_freq = []

for i in message :
    count = 0
    for j in message :
        if i == j :
            count += 1
        else :
            continue
    c_freq.append(count)

tmp = list(set(c_freq))
tmp.sort(reverse = True)

print("message after compressing")

for i in range(len(c_freq)) :
    for j in range(len(tmp)) :
        if c_freq[i] == tmp[j] :
            break
    for k in range(j) :
        print("0", end = "")
    print("1", end = "")
print()