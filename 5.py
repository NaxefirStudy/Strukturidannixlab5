import os
import time
from collections import Counter
import re

def load_text(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"[!] Ошибка при чтении файла: {e}")
        return ""

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = text.split()
    return words

def build_word_freq(words):
    word_counts = Counter(words)
    return word_counts

def build_index(words, word_counts):
    index = {}
    for i, word in enumerate(words):
        if word not in index:
            index[word] = []
        index[word].append(i)
    return index

def find_matching_words(query, index, word_counts, all_words):
    candidates = [word for word in word_counts if query in word]
    sorted_candidates = sorted(candidates, key=lambda x: word_counts[x], reverse=True)
    return sorted_candidates[:20]

def main():
    print("Работу выполнил - Попов Олег Михайлович 09.03.01ПОВа-o24")
    file_name = 'voina-i-mir.txt'
    text = load_text(file_name)
    if not text:
        print("[!] Не удалось загрузить текст.")
        return

    start_time = time.time()
    words = preprocess_text(text)
    word_counts = build_word_freq(words)
    index = build_index(words, word_counts)
    end_time = time.time()

    print(f"\n[INFO] Обработка текста заняла {end_time - start_time:.2f} секунд")

    while True:
        query = input("\nВведите слово (не короче 3 символов): ").strip().lower()
        if len(query) < 3:
            print("[!] Слово должно быть длиной не менее 3 символов.")
            continue

        start_query = time.time()
        results = find_matching_words(query, index, word_counts, words)
        end_query = time.time()

        print(f"\n[INFO] Время обработки запроса: {end_query - start_query:.4f} секунд")
        if results:
            print("\nРезультаты:")
            for word in results:
                print(word)
        else:
            print("\n[!] Ничего не найдено.")

if __name__ == "__main__":
    main()
