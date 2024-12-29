import requests
import time

def get_reason_code(reason_text):
    reason_map = {
        "hate speech": 9007,
        "inappropriate content": 9007,
        "spam": 1001,
        "harassment": 1002,
        "violence": 1003
    }
    return reason_map.get(reason_text.lower(), 9007)

def send_tiktok_report(payload, reports_count):
    url = "https://www.tiktok.com/aweme/v2/aweme/feedback/"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": payload.get("browser_version", "Mozilla/5.0")
    }

    print("🌟 Powered by Viper Droid 🌟")
    print("====================================\n")

    for i in range(1, reports_count + 1):
        try:
            print(f"🚀 Sending report {i} of {reports_count}...")
            response = requests.post(url, json=payload, headers=headers)

            if response.status_code == 200:
                response_data = response.json()
                if response_data.get("data", {}).get("need_captcha"):
                    print(f"⚠️ CAPTCHA required for report {i}. Stopping process.")
                    break
                elif response_data.get("status_code") == 0:
                    print(f"✅ Report {i} sent successfully! 🎉")
                else:
                    print(f"❌ Error in report {i}. Status message: {response_data.get('status_message')}")
            else:
                print(f"❌ Failed to send report {i}. HTTP Status code: {response.status_code}")
                print(f"Response: {response.text}")

        except Exception as e:
            print(f"⚠️ Error on report {i}: {e}")

        print("⏳ Waiting for 1 second before the next report...\n")
        time.sleep(1)

    print("🎯 All reports completed! 🚩\n")

def get_dynamic_payload(target_user_id, target_user_name):
    payload = {
        "WebIdLastTime": "1734385972",
        "aid": "1988",
        "app_language": "en",
        "app_name": "tiktok_web",
        "browser_language": "en-US",
        "browser_name": "Mozilla",
        "browser_online": "true",
        "browser_platform": "Win32",
        "browser_version": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
        "channel": "tiktok_web",
        "cookie_enabled": "true",
        "current_region": "IQ",
        "data_collection_enabled": "true",
        "device_id": "7449130936150017544",
        "device_platform": "web_pc",
        "focus_state": "true",
        "from_page": "user",
        "history_len": 6,
        "is_fullscreen": "false",
        "is_page_visible": "true",
        "lang": "en",
        "nickname": target_user_name,  
        "object_id": target_user_id,
        "odinId": "7196250726359811078",
        "os": "windows",
        "owner_id": target_user_id,
        "priority_region": "IQ",
        "reason": 9007,  
        "referer": f"https://www.tiktok.com/@{target_user_name}",
        "region": "IQ",
        "report_type": "user",
        "reporter_id": "7196250726359811078",
        "root_referer": "https://www.google.com/",
        "screen_height": 1080,
        "screen_width": 1920,
        "secUid": "MS4wLjABAAAAf-YKZA_VXJ9Qsh-NsePOxD9Do7yIu4XFtvSJN4XcXDGYWZ03RM54k3WsucMbyr26",
        "target": target_user_id,
        "tz_name": "Asia/Baghdad",
        "user_is_login": "true",
        "verifyFp": "verify_m4tu4sgp_qiaJcXGj_gk1Q_4i7U_8MOv_SQCya2IAnem3",
        "webcast_language": "en",
        "msToken": "dpCzvYJOLen5KrQLHj4bM4-7FlqFsNUx4WRNHoph4WDDk42H7J2uuMmR8vjhI1FH2412k4FA37mO-OFAomZ3xrTIxw-ftRWeyuCTnhBx8dhwa-lzSvy7-sKfrqDJN0vPbz__GHzvRneovcWA9oMCIkNi",
        "X-Bogus": "DFSzswVubWJANyvNt86ghO1hKNgb",
        "_signature": "_02B4Z6wo00001txYJTQAAIDDPT8PAGMtcsbcWCGAANB088"
    }
    return payload

if __name__ == "__main__":
    print("Powered by Viper Droid \n Dont hate me , hate the code")
    print("====================================\n")

    try:
        reason_text = input("📋 Enter the reason for reporting (e.g., hate speech, inappropriate content, etc.): ")
        reason_code = get_reason_code(reason_text)

        # Optionally, prompt user for the username
        target_user_name = input("\n🔍 Enter the username of the target to report: ")
        
        # Get the user ID based on the username or allow manual input
        target_user_id = input(f"🔍 Enter the user ID of {target_user_name} (you can get this from their profile URL): ")

        payload = get_dynamic_payload(target_user_id, target_user_name)
        payload["reason"] = reason_code

        count = int(input("\n📊 Enter the number of reports to send: "))
        if count <= 0:
            print("❌ Please enter a positive number.")
        else:
            send_tiktok_report(payload, count)
    except ValueError:
        print("❌ Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
