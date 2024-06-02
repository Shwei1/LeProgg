from task1 import FileReader, Observer

class Showlines(Observer):
    def onReceive(self, line):
        print(line)


class WordFinder(Observer):
    def __init__(self, word):
        self.criterion = False
        self.word = word

    def onReceive(self, line):
        for word in line.split():
            if word == self.word:
                self.criterion = True
                break
            else:
                continue

    def __str__(self):
        return f"{self.word} in line: {self.criterion}"


class WordCounter(Observer):
    def __init__(self):
        self.counter = 0

    def onReceive(self, line):
        words = line.split()
        self.counter += len(words)

    def __str__(self):
        return f"WordCounter: count = {self.counter}"

class MaxFinder(Observer):
    def __init_(self):
        self.max_word = ""

    def onReceive(self, line):
        words = line.split()
        self.max_word = max(words, key=len)
        return self.max_word

    def __str__(self):
        return f"MaxFinder: largest word is {self.max_word} with length {len(self.max_word)}"











if __name__ == '__main__':
    # showLines = Showlines()
    fr = FileReader('input01.txt')
    # fr.subscriber(showLines)
    # fr.read()
    #
    findword = WordFinder("kiki")
    fr.subscriber(findword)
    fr.read()
    print(findword)
    counter = WordCounter()
    fr.subscriber(counter)
    fr.read()
    print(counter)
    maxf = MaxFinder()
    fr.subscriber(maxf)
    fr.read()
    print(maxf)
