import os
import sys
from google import genai

def run_automation():
    # 1. 讀取金鑰
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("❌ 錯誤: 找不到 GEMINI_API_KEY")
        sys.exit(1)

    try:
        # 2. 初始化 Client
        client = genai.Client(api_key=api_key)
        
        # 3. 設定模型 (修正為 API 支援的正確名稱)
        model_name = "gemini-1.5-pro"
        
        # 4. 發送請求
        response = client.models.generate_content(
            model=model_name,
            contents="這是一則自動化測試。請回答：系統連線成功。"
        )
        
        print(f"✅ 使用模型: {model_name}")
        print(f"🤖 AI 回應: {response.text}")

    except Exception as e:
        # 這裡的縮排必須與 try 完全對齊
        print(f"❌ 執行發生異常: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    run_automation()
