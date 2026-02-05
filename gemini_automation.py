import os
import sys
from google import genai

def run_automation():
    # 1. 從 GitHub Secrets 讀取 API Key
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("❌ 錯誤: 找不到 GEMINI_API_KEY，請檢查 GitHub Secrets 設定。")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    # 2. 定義任務內容 (這裡可以改成讀取檔案、爬蟲結果或 TradingView 訊號)
    # 範例：假設我們要分析一段市場新聞並更新到 Notion
    task_type = "deep_analysis"  # 這裡可以根據邏輯動態改變
    market_data = "比特幣今日突破 10 萬美元大關，市場情緒極度樂觀，但 RSI 顯示超買。"

    # 3. 模型分流邏輯
    if task_type == "deep_analysis":
        model_name = "gemini-3-pro"
        prompt = f"你是一個專業分析師，請針對以下數據提供深度評論與操作建議：{market_data}"
    else:
        model_name = "gemini-3-flash"
        prompt = f"請將這段文字整理成簡短的 JSON 格式：{market_data}"

    print(f"🚀 啟動任務: 使用 {model_name}")

    try:
        # 4. 呼叫 Gemini API
        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        
        analysis_result = response.text
        print("✅ Gemini 分析完成：")
        print(analysis_result)

        # 5. (這裡可以加入您原本更新 Notion 的程式碼)
        # update_notion(analysis_result)
        
    except Exception as e:
        print(f"❌ 執行過程中發生錯誤: {e}")
        sys.exit(1)

if __name__ == "__main__":
    run_automation()