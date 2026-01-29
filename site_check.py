#!/usr/bin/env python3
import requests
import time
import socket

def check_site(url):
    print(f"\n🔍 Checking: {url}\n")

    # DNS Check
    try:
        host = url.replace("https://", "").replace("http://", "").split("/")[0]
        ip = socket.gethostbyname(host)
        print(f"✅ DNS OK → {host} resolves to {ip}")
    except Exception as e:
        print(f"❌ DNS Problem → {e}")
        return

    # HTTP Check
    try:
        start = time.time()
        r = requests.get(url, timeout=10)
        end = time.time()

        latency = round((end - start) * 1000, 2)

        print(f"🌐 Status Code : {r.status_code}")
        print(f"⏱️ Response Time: {latency} ms")

        if r.status_code == 200:
            print("✅ Website is UP and working fine")
        else:
            print("⚠️ Website reachable but returned error")

    except requests.exceptions.Timeout:
        print("❌ Timeout – Server slow or not responding")
    except requests.exceptions.ConnectionError:
        print("❌ Connection Error – Server down or blocked")
    except Exception as e:
        print(f"❌ Unknown Error → {e}")

def main():
    print("🌐 Welcome to Website Health Checker")
    print("🔹 Enter multiple URLs separated by space to check all at once\n")
    sites = input("Enter website URL(s): ").split()
    for site in sites:
        check_site(site)
        print("-"*50)
        time.sleep(1)

if __name__ == "__main__":
    main()
