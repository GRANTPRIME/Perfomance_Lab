import argparse

def circular_array_path(n, m):
    i = 1
    result = []
    while True:
        result.append(str(i))
        i = 1 + (i + m - 2) % n
        if i == 1:
            break
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("m", type=int)

    args = parser.parse_args()
    path = circular_array_path(args.n, args.m)
    result = "".join(path)
    print(result)

if __name__ == "__main__":
    main()
