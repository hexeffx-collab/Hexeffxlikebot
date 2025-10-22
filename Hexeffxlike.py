import requests
import time
import os
import json
import webbrowser

# API BASE
API_URL = "http://69.62.118.156:19126/like?uid={uid}&server_name={region}&key=freeapi"

# Track daily limit
like_request_done = False

def call_api(region, uid):
    url = API_URL.format(uid=uid, region=region)
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200 or not response.text.strip():
            return "API_ERROR"
        return response.json()
    except (requests.exceptions.RequestException, json.JSONDecodeError):
        return "API_ERROR"

def process_like(region, uid):
    global like_request_done

    if like_request_done:
        print("\n⚠️ You have already used your daily request limit! Try again later.")
        return

    print("\n⏳ Processing your request...\n")
    time.sleep(1)
    print("🔄 Fetching data from server... 10%")
    time.sleep(1)
    print("🔄 Validating UID & Region... 30%")
    time.sleep(1)
    print("🔄 Sending like request... 60%")
    time.sleep(1)
    print("🔄 Almost Done... 90%")
    time.sleep(1)

    response = call_api(region, uid)

    if response == "API_ERROR":
        print("\n🚨 API ERROR! ⚒️ Please wait for 8 hours, our server may be down.\n")
        return

    # ✅ Handle success
    if response.get("status") == 1:
        like_request_done = True
        print("\n✅ Like Added Successfully!")
        print(f"🔹 UID: {response.get('UID', 'N/A')}")
        print(f"🔸 Player Nickname: {response.get('PlayerNickname', 'N/A')}")
        print(f"🔸 Likes Before: {response.get('LikesbeforeCommand', 'N/A')}")
        print(f"🔸 Likes After: {response.get('LikesafterCommand', 'N/A')}")
        print(f"🔸 Likes By Bot: {response.get('LikesGivenByAPI', 'N/A')}")
        print("\n🗿 SHARE US FOR MORE: https://youtube.com/@teamxcutehack\n")

    # ✅ Handle already max likes but still send confirmation
    else:
        print(f"\n💔 UID {uid} has already received max likes for today.")
        print("✅ Like Done Command Sent To Server.")
        print("🔄 Try again tomorrow for more likes!\n")

def main():
    os.system('clear')
    banner = r"""
 __    __                               
|  \  |  \                              
| $$  | $$  ______   __    __   ______  
| $$__| $$ /      \ |  \  /  \ /      \ 
| $$    $$|  $$$$$$\ \$$\/  $$|  $$$$$$\
| $$$$$$$$| $$    $$  >$$  $$ | $$    $$
| $$  | $$| $$$$$$$$ /  $$$$\ | $$$$$$$$
| $$  | $$ \$$     \|  $$ \$$\ \$$     \
 \$$   \$$  \$$$$$$$ \$$   \$$  \$$$$$$$
                                        
                                        
"""
    print("\033[1;36m" + banner + "\033[0m")  # Cyan color banner
    print("╭────────────────────────────────────────────╮")
    print("│      Free Like Tool  -  @hexe.ffx          │")
    print("╰────────────────────────────────────────────╯")
    print("📱 Follow us on Instagram: @hexe.ffx")
    print("")

    choice = input("start (y/n): ").strip().lower()
    if choice == "y":
        time.sleep(2)

    print()
    region = input("🌍 Enter region (e.g. ind): ").strip().lower()
    uid = input("🆔 Enter UID (numbers only): ").strip()

    if not region.isalpha() or not uid.isdigit():
        print("\n⚠️ Invalid input! Region must be text, UID must be numeric.")
        print("📌 Example: ind 8385763215\n")
        return

    process_like(region, uid)

if __name__ == "__main__":
    main()