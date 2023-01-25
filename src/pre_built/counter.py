def count_ocurrences(path: str, word: str) -> int:
    file = open(path, "r")
    read_data = file.read()
    word_count = read_data.lower().count(word.lower())
    return word_count


if __name__ == "__main__":
    print(count_ocurrences("data/jobs.csv", "JAVASCRIPT"))
