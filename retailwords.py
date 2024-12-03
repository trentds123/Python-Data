from mrjob.job import MRJob

class WordCount(MRJob):

    def mapper(self,key, line):
        words = line.split("\t")
        if words[2] == "Description" or words[2] == "":
            pass
        else:
            nList = words[2].split(" ")
            for w in nList:
                if w == "":
                    pass
                else:
                    yield(w,1)

    def reducer(self,key,values):
        yield (key, sum(values))

if __name__ == '__main__':
    WordCount.run()
