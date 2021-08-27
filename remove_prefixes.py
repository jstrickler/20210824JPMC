import shutil

DATA_FILE = 'mydata.txt'
TEMP_FILE = DATA_FILE + ".tmp"

with open('prefixes.txt') as prefixes_in:
    prefixes = [line.rstrip() for line in prefixes_in]
print("prefixes:", prefixes)

data = []
with open(DATA_FILE) as mydata_in:
    with open(TEMP_FILE, 'w') as temp_out:
        for raw_line in mydata_in:
            line = raw_line.rstrip()
            for prefix in prefixes:
                if line.startswith(prefix):
                    line = line.replace(prefix, '')
                    temp_out.write(line + '\n')
                    number_value = int(line)
                    data.append(number_value)
                    break

print(data)
shutil.move(DATA_FILE, DATA_FILE + ".bak")
shutil.move(TEMP_FILE, DATA_FILE)

