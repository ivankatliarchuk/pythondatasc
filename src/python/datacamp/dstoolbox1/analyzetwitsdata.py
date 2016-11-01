import pandas as pd

# http://s3.amazonaws.com/assets.datacamp.com/production/course_1532/datasets/tweets.csv
df = pd.read_csv('tweets.csv')

langs_count = {}

col = df['lang']

# iterate over lang colum in df
for entry in col:
    # if the language is in langs_count, add +1
    if entry in langs_count.keys():
        langs_count[entry] += 1
    # else add the language to langs_count, set the value to 1
    else:
        langs_count[entry] = 1

print(langs_count)


def count_entries(df, col_name):
    '''
    Return a dictionary with counts of occurences as value
    for each key
    :param df: data frame
    :param col_name: column name
    :return:
    '''
    langs_count = {}
    # extract colum form DataFrame: col
    col = df[col_name]
    for entry in col:
        if entry in langs_count.keys():
            langs_count[entry] += 1
        else:
            langs_count[entry] = 1
    return langs_count


result = count_entries(df, 'lang')
print(result)
