from openai import OpenAI
from zhconv import convert

prompt = '''
您是個專業的研究員，可幫忙整理學術文獻的重要內容。
1. 請你務必**用中文回答**，除人名與專有名詞外，不要使用英文。
2. 整理學術文獻，會使用正式的學術用語。
3. 提供清晰、客觀的文獻總結時，會使用正式的學術用語。
4. 歸納文獻的主要重點，包括主題、觀念、原因、解決方案、結論和建議。
5. 提供清楚的、目標性的、正確的重點總結。
6. 避免個人意見和推浮，是一個可信賴的工具，用于整理各個領域的複雜學術內容，非常適於研究人員、學生和學術人士。
'''

# MODEL = 'deepseek-r1:14b'
MODEL = 'gemma3:27b'

def get_summary(text):
    client = OpenAI(
        api_key='ollama',
        base_url='http://solarsuna.com:34567/v1'
    )
    
    try:
        content = f'''
===== 文章開始 =====

{text}

===== 文章結束 =====

提供清楚的、客觀的重點整理。
使用正式的用語，並以小節作歸納，以條列格式整理。
'''
# 歸納重點，包括但不限於，核心議題、問題原因、各界看法、主要影響、處理方案、未來發展、結論等小節，依實際內容可作增減。
        
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": prompt
                },
                {
                    "role": "user",
                    "content": content
                }
            ],
            max_tokens=15000,
            temperature=0.7
        )
        
        summary = response.choices[0].message.content.strip()
        
        # 處理 </think> tag
        if '</think>' in summary:
            # 找到最後一個 </think> 的位置
            last_think_pos = summary.rindex('</think>')
            # 只保留 tag 之後的內容，並去除開頭的空白
            summary = summary[last_think_pos + 8:].lstrip()
            summary = to_tranditional_chinese(summary)
            
        return summary
        
    except Exception as e:
        return f"Error generating summary: {str(e)}"

def to_tranditional_chinese(text):
    """將簡體中文轉換為繁體中文"""
    return convert(text, 'zh-hant')
