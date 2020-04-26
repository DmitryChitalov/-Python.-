def ASCII(start, end):
    i = 0
    while start <= end:
        if i == 10:
            i=0
            print()
        print(f"{start}: {chr(start)}", end="   | ")
        start+=1
        i+=1


if __name__ == "__main__":
    ASCII(32, 127)
