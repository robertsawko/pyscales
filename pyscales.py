from pandas import read_csv, Timestamp, Timedelta
from numpy.random import choice

scales_data = read_csv('current.csv', parse_dates=[1], index_col=0)

# This will work in the same way as flashcard program

# construct the set of unlearnt
to_learn = []
now = Timestamp('now')
for s in scales_data.iterrows():
    if (s[1][0] + Timedelta('{0:n} days'.format(s[1][1])) < now):
        to_learn.append(s[0])


def session(scales_to_learn, number_of_questions):
    for s in choice(scales_to_learn, number_of_questions):
        print(s)
