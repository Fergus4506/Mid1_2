class Perm:
    def __init__(self, start_permutation, end_permutation):
        self.start_permutation = start_permutation
        self.end_permutation = end_permutation
        self.current_permutation = start_permutation[:]
        self.n = len(start_permutation)
        self.finished = False
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.finished:
            raise StopIteration
        
        result = self.current_permutation[:]
        
        if self.current_permutation <= self.end_permutation:
            if self.current_permutation == self.end_permutation:
                self.finished = True
            else:
                k = -1
                for i in range(self.n - 1):
                    if self.current_permutation[i] < self.current_permutation[i + 1]:
                        k = i
                if k == -1:
                    self.finished = True
                    raise StopIteration
                l = -1
                for i in range(k + 1, self.n):
                    if self.current_permutation[k] < self.current_permutation[i]:
                        l = i
                self.current_permutation[k], self.current_permutation[l] = self.current_permutation[l], self.current_permutation[k]
                self.current_permutation[k + 1:] = reversed(self.current_permutation[k + 1:])
            return result
        else:
            raise StopIteration
if __name__ == "__main__":
    start_perm = list(map(int, input().split()))
    end_perm = list(map(int, input().split()))
    
    my_perm = Perm(start_perm, end_perm)
    
    for p in my_perm:
        print(p)