FILEPATH = "tdos.txt"

def get_tdos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        tdos_local = file_local.readlines()
    return tdos_local

def write_tdos(tdos_arg, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(tdos_arg)

if __name__ == "__main__":
    pass