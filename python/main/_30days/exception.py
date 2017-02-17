class Calculator:
    def power(self, n, f):
        if n < 0 or f < 0:
            raise Exception("n and p should be non-negative")
        else:
            return n ** f
