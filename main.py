def file_check(address):
        import os
        if address == "" or address == " ":
                return True
        return os.path.exists(address)


def copy_in_str(string1, string2):
    ret_str = ""
    i = 0
    while i != len(string1):
        if string1[i] != string2[i]:
            ret_str += "-"
        if string1[i] == string2[i]:
            ret_str += string1[i]
        i += 1
    return ret_str


def check_exit(inp_str):
        inp_str = inp_str.lower()
        if inp_str == "exit":
                exit()


def find_protospacers(spacer, fag_seq):
    if spacer not in fag_seq:
        return False
    else:
        return fag_seq.find(spacer)


def read_file_with_spacers(spacers_filename):
    with open(spacers_filename, "r") as f:
        spacers = f.read()
    spacers = spacers.replace(" ", "")
    spacers = spacers.split("\n")
    return spacers


def read_file_with_fag(fag_filename):
    with open(fag_filename, "r") as f:
        warn = f.readline()
        text = f.read()
    text = text.replace("\n", "")
    text = text.replace(" ", "")
    return text


def print_pam_predictor():
    print("""
███████████████████████████████████████████████████████████████████████
█____██____██_███__██████____██____██___██____███____██___██____██____█
█_██_██_██_██__█___██████_██_██_██_██_████_██__██_██_███_███_██_██_██_█
█____██____██_█_█__█___██____██____██___██_██__██____███_███_██_██____█
█_█████_██_██_███__██████_█████_█_███_████_██__██_██_███_███_██_██_█_██
█_█████_██_██_███__██████_█████_█_███___██____███_██_███_███____██_█_██
███████████████████████████████████████████████████████████████████████
""")


def main():
    right = []
    left = []
    fag_filename = []
    print_pam_predictor()

    spacer_filename = input("Enter file name with spacers : ")
    # УБРАТЬ В СЛУЧАЕ ОШИБКИ СВЯЗЯННОЙ С КОДИРОВКОЙ
    check_exit(spacer_filename)
    if file_check(spacer_filename) is False:
        print("""\n!!!This file is not in the directory.!!!\n
                Please place the file being processed in a directory.\n""")
        exit()

    while True:
        input_filename = input("Enter filename seq backteriophage or exit: ")
        check_exit(input_filename)
        if file_check(input_filename) is False:
            print("""\n!!!This file is not in the directory.!!!\n
                    Please place the file being processed in a directory.\n""")
            exit()
        if input_filename == "":
            break
        fag_filename.append(input_filename)

    spacers = read_file_with_spacers(spacer_filename)
    print("SPACERS: ", spacers)
    for j in fag_filename:
        for i in spacers:
            text = read_file_with_fag(j)
            if find_protospacers(i, text) is not False:
                pos = find_protospacers(i, text)
                right.append(text[pos + len(i):pos + len(i) + 10])
                left.append(text[pos - 10:pos])
    try:
        save_l = left[0]
        save_r = right[0]
        for i in range(len(right)):
            save_r = copy_in_str(right[i], save_r)
        for i in range(len(left)):
            save_l = copy_in_str(left[i], save_l)
    except:
        print("Few spacers or bacteriophages...")
        exit()
    print("LEFT : ", left)
    print("RIGHT : ", right)
    print("Possible PAM in right : ", save_r)
    print("Possible PAM in left  : ", save_l)
    input("Enter...")
main()
