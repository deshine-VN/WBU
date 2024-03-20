from process import Process
import truststore
import argparse
import urllib3

urllib3.disable_warnings()
truststore.inject_into_ssl()

def main():
    parser = argparse.ArgumentParser(description="Usage:")
    parser.add_argument('-u', '--url', help='target url (e.g https://example.com)', required=True)

    args = parser.parse_args()
    Process.run(args.url)
    exit()

if __name__ == "__main__": 
    main()