import sys
def validate(source):
    try:
        value = int(source)
        print(value)
    except Exception as e:
        print('Bad String')

S = input().strip()
validate(S)
