from process import Process
import truststore
import argparse
import urllib3

urllib3.disable_warnings()
truststore.inject_into_ssl()

def main():
    print(r"""
 __        __          _                _      _   _      _     
 \ \      / /_ _ _   _| |__   __ _  ___| | __ | | | |_ __| |___ 
  \ \ /\ / / _` | | | | '_ \ / _` |/ __| |/ / | | | | '__| / __|
   \ V  V / (_| | |_| | |_) | (_| | (__|   <  | |_| | |  | \__ \
    \_/\_/ \__,_|\__, |_.__/ \__,_|\___|_|\_\  \___/|_|  |_|___/
                 |___/                                          

                 Author: deshine (https://hackerone.com/deshine)
""")
    
    parser = argparse.ArgumentParser(description="Usage:")
    parser.add_argument('-u', '--url', help='target url (e.g https://example.com)', required=True)

    args = parser.parse_args()
    Process.run(args.url)
    exit()

if __name__ == "__main__": 
    main()