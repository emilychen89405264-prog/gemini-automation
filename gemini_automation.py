import os
import sys
# 必須使用最新的 SDK
try:
    from google import genai
except ImportError:
    print("❌ 錯誤: 找不到 google-genai 模組，請確認 pip install 是否成功。")
    sys.exit(1)

def run_automation():
    # 這裡的名字必須與 GitHub Secret 名稱完全一致
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("❌ 錯誤: GitHub Secrets 中的 GEMINI_API_KEY 是空的。")
        sys.exit(1)

    try:
        # 初始化 Client
        client = genai.Client(api_key=api_key)
        
        # 這裡設定為 Pro 模型 (Paid Tier)
        # 如果您想省錢，可以改為 "gemini-3-flash"
        model_name = "gemini-3-pro"
        
        response = client.models.generate_content(
            model=model_name,
            contents="這是一則自動化測試。請回答：系統連線成功。"
        )
        
        print(f"✅ 使用模型: {model_name}")
        print(f"🤖 AI 回應: {response.text}")

    except Exception as e:
        print(f"❌ 執行發生異常: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    run_automation()
