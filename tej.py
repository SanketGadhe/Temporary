def main():
    bt = []
    wt = 0
    twt = 0
    ttat = 0

    p = int(input("Enter the number of processes: "))
    
    print("Enter the burst time for each process:")
    for i in range(p):
        bt.append(int(input()))

    # Sorting burst times in ascending order
    bt.sort()

    print("Burst time \t Waiting time \t Turn-around time")

    for i in range(p):
        tat = bt[i] + wt
        twt += wt
        ttat += tat
        print(f" {bt[i]} \t\t {wt} \t\t {tat}")
        wt += bt[i]

    print("\n Average waiting time:", twt / p)
    print("\n Average turn-around time:", ttat / p)

if __name__ == "__main__":
    main()
