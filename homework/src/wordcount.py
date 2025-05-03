import os

from ._internals.write_count_words import write_count_words

def main():
    input_files_list = os.listdir("data/input/")

    counter = {}
    for filename in input_files_list:
        with open("data/input/" + filename) as f:
            for l in f:
                for w in l.split():
                    w = w.lower().strip(",.!?")
                    counter[w] = counter.get(w, 0) + 1

    write_count_words(counter)


if __name__ == "__main__":
    main()
