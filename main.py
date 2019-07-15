from metod_for_main import *


def main():
    print("""
███████████████████████████████████████████████████████████████████████
█____██____██_███__██████____██____██___██____███____██___██____██____█
█_██_██_██_██__█___██████_██_██_██_██_████_██__██_██_███_███_██_██_██_█
█____██____██_█ █__█___██____██____██___██_██__██____███_███_██_██____█
█_█████_██_██_███__██████_█████_█_███_████_██__██_██_███_███_██_██_█_██
█_█████_██_██_███__██████_█████_█_███___██____███_██_███_███____██_█_██
███████████████████████████████████████████████████████████████████████
""")
    if file_check("mafft-win") is False:
        answ = input("""The mafft sequence alignment program is not installed on your computer.
                     \nDo you want to install mafft (25,3 mb)? [y / n]: """)
        if answ == "y" or answ == "Y":
            download_mafft()
            unzip()
            print("Complete!\n")
        else:
            print("""The program can not continue to work without this module.
                  \nShut down ...""")
            exit()
    crispr_filename = input("Spacer: ")
    check_exit(crispr_filename)
    if file_check(crispr_filename) is False:
        print("\nThe file is not in the directory!\n")
        input("Press Enter...")
        exit()
    for i in range(10):
        seq = input("SEQ backteriophage filename %i: " % (i+1))
        value_fag[i] = seq
        check_exit(seq)
        if file_check(seq) is False:
            print("\nThe file is not in the directory!\n")
            input("Press Enter...")
            exit()
        if seq != "":
            fasta_spotter(seq)

    flag1 = 0
    flag2 = "(work_file)"

    for i in range(10):
        if value_fag[i] != "":
            write_in_file_for_align("test%i.txt" % flag1,
                                    seq_read(value_fag[i]),
                                    seq_read(crispr_filename))
            mafft("test%i.txt" % flag1, value_fag[i].replace(".fasta", "") +
                  flag2 + ".txt")
            flag1 += 1

    file_in_dir = search_flag(flag2)

    for i in file_in_dir:
        output = read_output(i)
        left_seq.append(output[0])
        right_seq.append(output[1])
    save_l_r(left_seq, "left.txt")
    save_l_r(right_seq, "right.txt")
    delete_file(flag2)
    delete_file("test")
    input("Enter...")

main()
