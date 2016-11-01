from array import array
class XorTester:
    def solve(self):

        firstLine = input("")
        secondLine = input("")

        rows = firstLine.split(" ")[0]
        columns = firstLine.split(" ")[1]
        numbers = secondLine.split(" ")

        current = array('L')
        for num in numbers:
            current.append(int(num))

        # //e = c ^ d
        var = int(columns)
        rowNum = int(rows)
        while var > 0:
            temp = array('L')
            count = 0
            for idx, val in enumerate(current):
                var -= 1
                if (idx < rowNum -1):
                    temp.append(current[idx] ^ current[idx + 1])
                if (idx == rowNum - 1):
                    temp.append(current[idx] ^ current[0])
                count += 1
            if (count == 0):
                current = temp
                break
            current = temp
        output = ""
        for idx, num in enumerate(current):
            if (idx < rowNum - 1):
                output += str(num) + " "
            else:
                output += str(num)
        print(str(output))



XorTester().solve()
