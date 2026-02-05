import os
import sys
from google import genai

def run_automation():
    # 這裡必須與 GitHub Secret 的名稱完全一致
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("❌ 錯誤: 找不到 GEMINI_API_KEY，請檢查 GitHub Secrets 設定。")
        sys.exit(1)

    # 初始化最新版本的 Google GenAI Client
    client = genai.Client(api_key=api_key)

    # 模擬任務：分析一段市場文字
    task_type = "deep_analysis" 
    market_data = "比特幣今日突破 10 萬美元，技術指標顯示強勢，但需注意回檔風險。"

    # 邏輯分流：判斷任務類型
    if "analysis" in task_type:
        # 使用 Paid Tier 的 Pro 模型 (若已綁定信用卡)
        model_name = "gemini-3-pro"
        prompt = f"你是一個專業投資分析師，請評論此數據：{market_data}"
    else:
        # 簡單任務使用 Flash 模型
        model_name = "gemini-3-flash"
        prompt = f"請摘要此數據：{market_data}"

    print(f"🚀 啟動任務: 使用 {model_name}")

    try:
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        print("✅ Gemini 分析完成：")
        print(response.text)
    except Exception as e:
        print(f"❌ API 呼叫失敗: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_automation()
