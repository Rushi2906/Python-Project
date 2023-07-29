import pyshorteners as p

def shorten_url(long_url):
    try:
        s = p.Shortener()
        shorten_url = s.tinyurl.short(long_url)
        return shorten_url
    except Exception as e:
        print("Error: ",e)
        return None

def main():
    while True:
        long_url = input("Enter Long URL (type 'exit' to quite) : ")
        if long_url.lower()=="exit":
            break

        short_url = shorten_url(long_url)
        if short_url:
            print(f"Shortened URL: {short_url}")
            print("You can access the shortened URL to reach the original destination using 'ctrl+click' on shortened URL.")
            print()
        else:
            print("Failed to shorten the URL. Please try again.")
            print()

if __name__=="__main__":
    main()