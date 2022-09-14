import re

# valid ip address scanning using regular expression

# [1-256].[0-256].[0-256].[0-256]

def check_ip_address(ip: str) -> bool:
    #matched = re.search("(\d+)\.(\d+)\.(\d+)\.(\d+)", ip)
    matched = re.search("^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$", ip)
    if matched:
        print(matched)
        print(f"valid ip address: ", {matched.group()} )
    '''   
    firstOct = matched.group(1)
    secondOct = matched.group(2)
    thirdOct = matched.group(3)
    fourthOct = matched.group(4)
    print(f"firstOct: {firstOct}, secondOct: {secondOct}, thirdOct:{thirdOct}, fourthOct: {fourthOct}")
    '''




if __name__ == "__main__":
    check_ip_address("172.20.196.10")


