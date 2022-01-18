massiv = []
local_number=300
while len(massiv)<20:
    local_number=local_number+1
    if local_number%13==0 or local_number%17==0:
        massiv.append(local_number)
print(massiv)
        