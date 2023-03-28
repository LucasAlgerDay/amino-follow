import aminofix as amino, concurrent.futures
from colorama import Fore
from pyfiglet import figlet_format

print(
    f"""{Fore.CYAN}
Follow script made by Lucas Day"""
)

print(figlet_format("Follow 2.0", font="stop"))


client = amino.Client()
email = input("Email: ")
password = input("Password: ")
client.login(email=email, password=password)



def followonlineusers():
    clients = client.sub_clients(size=100)
    for x, name in enumerate(clients.name, 1):
        print(f"{x}.{name}")
    communityid = clients.comId[int(input("Select the community: "))-1]
    sub_client = amino.SubClient(comId=communityid, profile=client.profile)
    with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
        for i in range(0, 20000, 100):
            onlineusers = sub_client.get_online_users(start=i, size=5000).profile.userId
            if onlineusers:
                for userId in onlineusers:
                    print(f"{userId} followed/")
                    _ = [executor.submit(sub_client.follow, [userId])]
            else:
                break




def followall():
    clients = client.sub_clients(size=100)
    for x, name in enumerate(clients.name, 1):
        print(f"{x}.{name}")
    communityid = clients.comId[int(input("Select the community: "))-1]
    sub_client = amino.SubClient(comId=communityid, profile=client.profile)
    with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
        for i in range(0, 200000, 100):
            all = sub_client.get_all_users(start=i, size=50000).profile.userId
            if all:
                for userId in all:
                    print(f"{userId} followed/")
                    _ = [executor.submit(sub_client.follow, [userId])]
            else:
                print("All members followed")
                break


def followglobalall():
    with concurrent.futures.ThreadPoolExecutor(max_workers=10000) as executor:
        for i in range(0, 20000, 100):
            all = client.get_all_users(start=i, size=5000).profile.userId
            if all:
                for userId in all:
                    print(f"{userId} followed/")
                    _ = [executor.submit(client.follow, [userId])]
            else:
                print("All members followed")
                break


print("1.Follow Online Users:")
print("2.Follow All in the community:")
print("3.Follow global (all lenguages):")
inviteselect = input("Type Number: ")
if inviteselect == "1":
	followonlineusers()


elif inviteselect == "2":
	followall()

elif inviteselect == "3":
	followglobalall()
