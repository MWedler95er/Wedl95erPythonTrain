# pylint: skip-file

# DAY 11 - while loop that prints only odd numbers from 1 to 20

COUNTER = 0
while COUNTER < 20:
    if COUNTER % 2 == 1:
        print(COUNTER)
    COUNTER += 1
