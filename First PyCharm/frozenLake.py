def main():
    lake = [
        ['S','F','F','F'],
        ['F','H','F','F'],
        ['F','F','H','H'],
        ['F','F','F','E']
    ]

    for row in lake:
        print(' '.join(row))

if __name__ == "__main__":
    main()