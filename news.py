import os

choice = int(input("tech news or normal news?: "))

if choice == 1:
    os.system("python3 tech-news.py")
elif choice == 2:
    os.system("python3 nytimes.py")

else:
    print("invalid input!")

