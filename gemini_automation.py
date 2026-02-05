import os
import requests
import json

def run_automation():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ 錯誤: GitHub Secrets 沒抓到金鑰")
        return

    # 測試方案 A: 1.5-flash (目前全球最穩定)
    model = "gemini-1.5-flash"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    
    payload = {"contents": [{"parts": [{"text": "測試連線"}]}]}
    headers = {'Content-Type': 'application/json'}

    print(f"📡 正在嘗試透過 REST API 呼叫 {model}...")

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        
        if response.status_code == 200:
            print("✅ [大成功] 系統連線完全正常！")
            print(f"🤖 AI 回應: {response.json()['candidates'][0]['content']['parts'][0]['text']}")
        elif response.status_code == 404:
            print(f"❌ 依舊報錯 404：這把 Key 找不到模型 {model}。")
            print("💡 解決方案：請嘗試將模型名稱改為 'gemini-1.5-pro' 再跑一次。")
        else:
            print(f"❌ 伺服器回傳錯誤 {response.status_code}:")
            print(response.text)
            
    except Exception as e:
        print(f"❌ 網路異常: {e}")

if __name__ == "__main__":
    run_automation()
