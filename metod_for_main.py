"""global variables"""
length_crispr = 0
value_fag = ["", "", "", "", "", "", "", "", "", ""]
nucleotides = ["a", "t", "c", "g"]
right_seq = []
left_seq = []
file_in_dir = []
"""function"""


def write_in_file_for_align(filename, seq1, seq2):
    file = open(filename, "w+")
    file.write(">1\n")
    file.write(seq1)
    file.write(">2\n")
    file.write(seq2)
    file.close()
# write_in_file_for_align("testdata.txt","ATAGCTAGCATG","ACATGCATGACTGC")


def download_mafft():
        from urllib.request import urlretrieve
        name = "mafft-7.429-win64-signed.zip"
        url = "https://mafft.cbrc.jp/alignment/software/%s" % name
        destination = url.rsplit('/', 1)[1]
        urlretrieve(url, destination)


def unzip():
        import zipfile
        fantasy_zip = zipfile.ZipFile('mafft-7.429-win64-signed.zip')
        fantasy_zip.extractall()
        fantasy_zip.close()


def mafft(filename_input, filename_output):
    import os
    os.system('mafft-win\mafft.bat --auto --reorder --out ' +
              filename_output + ' ' + filename_input)


def file_check(address):
        import os
        if address == "" or address == " ":
                return True
        return os.path.exists(address)


def check_exit(inp_str):
        inp_str = inp_str.lower()
        if inp_str == "exit":
                exit()


def search_flag(flag):
        import os
        file_list = os.listdir()
        ret_list = []
        for i in file_list:
                if flag in i:
                        ret_list.append(i)
        return ret_list


def seq_read(seq_filename):
    file = open(seq_filename, "r")
    seq = file.read()
    file.close()
    return seq


def fasta_spotter(filename):
        file = open(filename, "r")
        first_line = file.readline()
        nucleo = file.read()
        file.close()
        nucleo = nucleo.replace(first_line, "")
        file = open(filename, "w+")
        file.write(nucleo)
        file.close()
# функция нахождения выровненной КРИСП строки среди "-"


def search_pos(string, start):
        i = start
        position = []
        while i in range(len(string)):
                if string[i] in ["a", "c", "g", "t"]:
                        position.append(i)
                        while string[i] != "-":
                                i += 1
                        if(string[i] == "-"):
                                position.append(i-1)
                i += 1
        return position


def save_l_r(array, sobaka):
        file = open(sobaka, "w+")
        for i in array:
                for j in i:
                        for k in j:
                                file.write(k + "\n")
        file.close()


def space_write(i_need_str, i, length_seq):
        ret_str = ""
        while True:
                ret_str += i_need_str[i]
                i += 1
                if i == length_seq:
                        break
        return ret_str


def delete_file(flag):
        import os
        file_in_dir = os.listdir()
        target = []
        for i in file_in_dir:
                if flag in i:
                        target.append(i)
        for i in target:
                os.remove(i)


def read_output(filename):
        import re
        file = open(filename, "r")
        parcer = file.read()
        parcer = parcer.replace("\n", "")
        parcer = parcer.replace(" ", "")
        length_seq = len(parcer)
        right = []
        left = []
        l_r_sequence = []
        pos = []
        start = 0
        space = ""
        l_r_const = 25
        expr = "[a-z]+"
        name = filename.replace(".txt", "")
        for i in range(len(parcer)):
                if parcer[i] == "2":
                        space = space_write(parcer, i, length_seq)
                        pos = search_pos(space, start)
        space2 = re.findall(expr, space)
        for i in range(len(pos)):
                if i % 2 == 0:
                        pos[i] += 1
                if i % 2 == 1:
                        pos[i] += 1

        flag = 1
        for i in pos:
                if flag % 2 == 0:
                        right.append([parcer[i:(i+l_r_const)], name])
                if flag % 2 == 1:
                        left.append([parcer[(i-l_r_const):i], name])
                flag += 1
        l_r_sequence.append(left)
        l_r_sequence.append(right)
#        print("LEFT: ",left)
#        print("RIGHT: ",right)
        file.close()
        return l_r_sequence
