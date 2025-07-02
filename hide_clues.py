import os
import sys
import random

START_CLUE = 1
LAST_CLUE = 12
CLUE_SPACE = 100000
# should be consecutive digits of the form 1234...
FIRST_CLUE = 12345

def zero_pad(clue):
    l = len(str(clue))
    m = len(str(CLUE_SPACE)) - 1
    if l < m:
        return "0"*(m-l) + str(clue)
    else:
        return str(clue)

def gen_clue_list(first, last, space):
    with open(".seed","r") as seedfile:
        seed = int(seedfile.readline())
    R = random.Random()
    R.seed(seed)
    clue_indexes = []
    for i in range(first, last+1):
        clue_indexes.append(R.randint(1, space))
    clue_indexes[0] = FIRST_CLUE
    return clue_indexes

if __name__ == "__main__":

    secret_number = 42

    result = ""
    try:
        result = os.stat("clues")
    except:
        pass

    if (result):
        sys.exit("Clues folder already exists.")

    os.mkdir("clues")
    seed = random.Random().randrange(1000000,9999999)
    with open(".seed", "w") as seedfile:
        print(seed, file=seedfile)

    clue_indexes = gen_clue_list(START_CLUE, LAST_CLUE,
                                 CLUE_SPACE)

    template_names = os.listdir(".clue-templates")
    template_names.sort()
    template_data = []

    for t in template_names:
        data = open(".clue-templates/" + t, "r").read()
        template_data.append(data)

    print("Hiding clues...")
    for i in range(0, CLUE_SPACE):
        dir_name = "clues/" + \
            "0"*(len(str(CLUE_SPACE))-1 - len(str(i))) + str(i)
        os.mkdir(dir_name)
        file_name = open(dir_name + "/clue", "w")
        if (i not in clue_indexes):
            file_name.write("Nothing to see here.\n")
        else:

            template_index = clue_indexes.index(i)

            if (template_index < len(template_data)):
                file_name.write(template_data[template_index])
            else:
                file_name.write("Clue: \n")
    print("Done hiding clues.")
    print("You can find your first clue at clues/12345/clue")
