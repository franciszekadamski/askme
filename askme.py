#!/usr/bin/python3

import sys

import askmelib
from askmelib import *


__doc__ = """Parser for Askme app;
Press "r" to repeat question;
Press "s" to skip question;
Press "q" to quit;
"""


def main(filename="data/docker"):
    """Ask questions
    Source file should be passed without extension and there should be .json file with given name
    Parameters:
        filename : str
    Output:
        None
    """
    ask_to_pickle(filename + ".ask")
    content = read(filename + ".pkl", ftype="pickle")
    random.shuffle(content)
    fails = 0
    threshold = 0.9
    score = 1

    for n, cell in enumerate(content):
        score = len(content) - fails
        similarity = 0
        while similarity < threshold:
            os.system("clear")
            response = multiline_input("==========================================\nQuestion {}/{} | Score {}/{} | Score [%] {}\n==========================================\n{}\n\n".format(n + 1, len(content), score, len(content), round(100*score/len(content), 2), cell["question"]))
            similarity = jellyfish.jaro_similarity(response, cell["answer"])
            print("\n{}%".format(int(similarity * 100)))
            print("\n\n{}\n".format(cell["answer"]))
            decision = input()

            if similarity < threshold:
                fails += 1

            if decision == "s":
                similarity = 1
            elif decision == "r":
                similarity = 0
            elif decision == "q":
                similarity = 1
                sys.exit(1)

    print(round(100*score/len(content), 2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help=__doc__)
    args = parser.parse_args()

    main(args.file)
