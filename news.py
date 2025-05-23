import os

choice = int(input("tech news or normal news?: "))

if choice == 1:
    os.system("python3 /home/saurya-jha/dev/web-scraping/news-headlines/tech-news.py")
elif choice == 2:
    os.system("python3 /home/saurya-jha/dev/web-scraping/news-headlines/nytimes.py")

else:
    print("invalid input!")

