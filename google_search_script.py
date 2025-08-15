from googlesearch import search

print("Welcome to Google Search Tool!")

query = input("Enter your search query:")

for i in search(query, start = 0, stop = 10):
    print(i)