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
        
        # 嘗試使用兩種可能的名稱格式 (方案 A)
        model_id = "gemini-1.5-flash" 
        
        print(f"正在嘗試連線模型: {model_id}...")
        
        response = client.models.generate_content(
            model=model_id,
            contents="測試連線，請回答 OK。"
        )
        
        print(f"✅ 成功！AI 回應: {response.text}")

    except Exception as e:
        print(f"❌ 發生異常: {str(e)}")
        print("\n--- 正在為您查詢目前 API Key 支援的所有模型清單 ---")
        try:
            # 這段會列出你這把 Key 真正能用的模型名稱
            for m in client.models.list():
                print(f"可用模型: {m.name} (支援方法: {m.supported_methods})")
        except:
            print("無法取得模型清單。")
        sys.exit(1)

if __name__ == "__main__":
    run_automation()
