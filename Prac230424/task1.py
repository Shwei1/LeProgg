from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    @abstractmethod
    def onReceive(self, line):
        raise NotImplementedError


class FileReader:
    def __init__(self, file_name):
        self.file_name = file_name
        self.observers = [] # spysok sposterihachiv

    def subscriber(self, observer):
        self.observers.append(observer)

    def read(self):
        with open(self.file_name) as f:
            for line in f:
                for observer in self.observers:
                    observer.onReceive(line.rstrip())






if __name__ == '__main__':
    fr = FileReader('input01.txt')
    fr.read()

