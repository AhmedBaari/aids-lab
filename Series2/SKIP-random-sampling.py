def custom_random_sample(data, N):
    seed = 1
    shuffled_data = data[:]
    for i in range(len(shuffled_data) - 1, 0, -1):
        seed = (seed * 1664525 + 1013904223) & 0xFFFFFFFF
        j = seed % (i+1)
        shuffled_data[i], shuffled_data[j] = shuffled_data[j], shuffled_data[i]
    return shuffled_data[:N]
print("Random Sample: ", custom_random_sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 4))