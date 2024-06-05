class MusicNotes():
    def __init__(self):
        self._notes = [55,61.74,65.41,73.42,82.41,87.31,98]
        self._index = -1
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._index>len(self._notes)*5-1:
            raise StopIteration()
        self._index +=1
        return self._notes[int(self._index/5)]*pow(2,self._index%5)

        

nodes_iter = iter(MusicNotes())
for freq in nodes_iter:
    print(freq)