#loads .panda files
def read_from_file(file, output_dict):
    lines = file.readlines()
    for line in lines:
        data = line.split("|")
        name_of_constant = data[0]
        constant = data[1]
        output_dict[name_of_constant] = constant
