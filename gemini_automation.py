import os
import sys
from google import genai

def run_automation():
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("❌ 錯誤: 找不到 GEMINI_API_KEY")
        sys.exit(1)

    try:
        client = genai.Client(api_key=api_key)
        
        # 改用 Flash 模型，這是目前 v1beta 最穩定的模型代號
        # 如果 1.5-flash 還不行，這代表您的 API Key 可能需要重新產生
        model_name = "gemini-1.5-flash"
        
        response = client.models.generate_content(
            model=model_name,
            contents="連線測試，請回覆：OK"
        )
        
        print(f"✅ 成功連線！使用模型: {model_name}")
        print(f"🤖 AI 回應: {response.text}")

    except Exception as e:
        print(f"❌ 執行發生異常: {str(e)}")
        # 如果還是 404，印出目前的模型清單供除錯
        sys.exit(1)

if __name__ == "__main__":
    run_automation()
