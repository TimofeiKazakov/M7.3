class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                file = file.read().lower()
                for j in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    file = file.replace(j, '')
                words = file.split()
                all_words[i] = words
        return all_words

    def find(self, word):
        find = {}
        for self.file_num in self.file_names:
            for key, value in self.get_all_words().items():
                word = word.upper()
                if word in [x.upper() for x in value]:
                    find[key] = (value.index(word.lower()) + 1)
            return find

    def count(self, word):
        count = {}
        for i, word_ in self.get_all_words().items():
            count[i] = word_.count(word.lower())
        return count

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))