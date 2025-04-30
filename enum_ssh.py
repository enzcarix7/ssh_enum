from paramiko import SSHClient, AuthenticationException, SSHException, AutoAddPolicy
from time import sleep

def ssh_enumerate(ip: str, username_list: str, port: int = 22) -> list[str]:
    ssh_client: SSHClient = SSHClient()
    ssh_client.set_missing_host_key_policy(AutoAddPolicy())
    result: list[str] = []
    with open(username_list, encoding='utf-8', errors='ignore') as usernames:
        for username in usernames:
            #sleep(4)
            username: str = username.strip()
            try:
                ssh_client.connect(ip, port=port, username=username, timeout=10)
                if username:
                    print(f"[+] Valid username: {username}")
                    result.append(username)
            except AuthenticationException as e:
                print(f"[-] Invalid username: {username} - {str(e)}")
                continue
            except SSHException as e:
                print(f"[-] SSH error for {username}: {str(e)}")
                continue
            except EOFError:
                print(f"[-] EOFError: Possible non-SSH server or network issue for {username}")
                continue
            except Exception as e:
                print(f"[-] Error: {str(e)}")
                continue
    ssh_client.close()
    for valid_username in result:
        print(f"[+] Valid username: {valid_username}")
    return result

user_path: str = r'wlist/path' #replace w wlist
ssh_enumerate('x.x.x.x', user_path) #replace w ulist
