import os
import pandas as pd
from yt_dlp import YoutubeDL

# === 設定頻道網址 ===
channel_url = 'https://www.youtube.com/@HungyiLeeNTU/videos'

# === 設定 CSV 檔案名稱 ===
csv_file = 'video_list.csv'

# === yt-dlp 參數 ===
ydl_opts = {
    'quiet': True,
    'extract_flat': True,
    'skip_download': True,
    'dump_single_json': True,
}

# === 取得頻道影片清單 ===
with YoutubeDL(ydl_opts) as ydl:
    channel_info = ydl.extract_info(channel_url, download=False)

videos = channel_info.get('entries', [])

# === 建立 DataFrame ===
video_list = []
for video in videos:
    video_id = video.get('id')
    video_list.append({
        'id': video_id,
        'title': video.get('title'),
        'url': f"https://www.youtube.com/watch?v={video_id}",
        'date': video.get('upload_date', 'unknown')
    })

df = pd.DataFrame(video_list)

# === 若日期存在，轉換格式 ===
def format_date(date):
    return f"{date[:4]}-{date[4:6]}-{date[6:]}" if date != 'unknown' else date

df['date'] = df['date'].apply(format_date)
df = df.iloc[::-1].reset_index(drop=True)

# === 加入從1開始的 idx 欄位 ===
df.insert(0, 'idx', df.index + 1)

# === 儲存到 CSV 檔案 ===
df.to_csv(csv_file, index=False)
print(f"📌 已建立 {csv_file}，共儲存 {len(df)} 部影片。")
