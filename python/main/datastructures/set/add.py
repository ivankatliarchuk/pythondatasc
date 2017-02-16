"""
TASK
Apply knowledge of the add() operation.
Count the total number of distinct country stamps in her collection.
Pick the stamps one by one from a stack on N country stamps.
INPUT
The first line contains an integer N, the total number of country stamps.
The next N lines contains the name of the country where the stamp is from.
CONSTANTS
0 < N < 1000
OUTPUT
Output the total number of distinct country stamps on a single line.
SAMPLE INPUT
7
UK
China
USA
France
New Zealand
UK
France
SAMPLE OUTPUT
5
EXPLANATION
-----
"""
N = int(input().strip())
countries = set()

for num in range(0, N):
    country = (input().strip())
    countries.add(country)

print(len(countries))
