#loads .panda files
def read_from_file(file, output_dict):
    lines = file.readlines()
    for line in lines:
        data = line.split("|")
        name_of_constant = data[0]
        constant = data[1]
        if isInt(constant):
            output_dict[name_of_constant] = int(constant)
        else:
            output_dict[name_of_constant] = constant

def isInt(string):
    try:
        int(string)
        return True
    except:
        return False