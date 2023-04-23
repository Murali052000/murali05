import csv
import re
import time
import psutil


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def read_csv(file_path):
    with open(file_path, 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        return {rows[0].lower(): rows[1].lower() for rows in reader}


def write_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data)


def replace_words(text, find_words, french_dict):
    unique_words_replaced = set()
    word_frequency = {}
    for word in find_words:
        if word in french_dict:
            replace_word = french_dict[word]
            pattern = r'\b{}\b'.format(re.escape(word))
            text, count = re.subn(pattern, replace_word, text, flags=re.IGNORECASE)
            if count > 0:
                unique_words_replaced.add(word)
                word_frequency[word] = count
    return text, unique_words_replaced, word_frequency


def main():
    # Start time
    start_time = time.time()

    # Read files
    input_file_path = 'C:/Users/mural/Downloads/TranslateWords Challenge/t8.shakespeare.txt'
    find_words_file_path = 'C:/Users/mural/Downloads/TranslateWords Challenge/find_words.txt'
    french_dict_file_path = 'C:/Users/mural/Downloads/TranslateWords Challenge/french_dictionary.csv'
    input_text = read_file(input_file_path)
    find_words = read_file(find_words_file_path).split()
    french_dict = read_csv(french_dict_file_path)

    # Replace words
    output_text, unique_words_replaced, word_frequency = replace_words(input_text, find_words, french_dict)

    # Write output file
    output_file_path = 'E:/New folder/output.txt'
    write_file(output_file_path, output_text)

    # Write frequency file
    frequency_file_path = 'E:/New folder/frequency.txt'
    with open(frequency_file_path, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['English word' 'French word' 'Frequency'])
        for word in unique_words_replaced:
            writer.writerow([word, french_dict[word], word_frequency[word]])

    # End time
    end_time = time.time()

    # Performance metrics
    time_taken = end_time - start_time
    memory_used = psutil.Process().memory_info().rss / 1024 ** 2  # in MB
    performance_metrics = f'Time to process: {time_taken:.0f} seconds\nMemory used: {memory_used:.2f} MB\n'

    # Write performance file
    performance_file_path = 'E:/New folder/performance.txt'
    write_file(performance_file_path, performance_metrics)


if __name__ == '__main__':
    main()
