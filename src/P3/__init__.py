import P2


def main():
    print("P3 main:")
    print("P3 call to => get s3 resources from P2", P2.get_s3_resources())
    print("P3 call to => get_weather from P2:", P2.get_weather(32.0853,34.7818))

if __name__ == "__main__":
    main()