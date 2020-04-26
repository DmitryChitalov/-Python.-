def ASCII(start, end, i):
    if i == 0:
        print()
        i=10
    print(f"{start}: {chr(start)}", end="   | ")
    if start == end:
        return
    ASCII(start+1,end, i-1)


if __name__ == "__main__":
    ASCII(32, 127, 10)