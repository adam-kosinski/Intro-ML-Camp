from random import randint

def main():
    names = ['Amogh', 'Calder', 'Michiko', 'William', 'Rohan', 'Adam', 'Aryaman', 'Sirish', 'Luke']
    groups = []
    while len(names) >= 2:
        newGroup = []
        newGroup.append(names.pop(randint(0, len(names)-1)))
        newGroup.append(names.pop(randint(0, len(names)-1)))
        if len(names) == 1:
            newGroup.append(names.pop(randint(0, len(names)-1)))
        groups.append(newGroup)

    print('')
    for group in groups:
        print(', '.join(group))
    print('')


if __name__ == "__main__":
    main()