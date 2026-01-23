import os, requests, json, shutil
query = "sad"
PEXELS_KEY = "YOUR_PEXELS_KEY"  # ← 去 https://www.pexels.com/api/ 免费申请

def download(url, name):
    shutil.copyfileobj(requests.get(url, stream=True).raw, open(name, "wb"))

# 6 张图
r = requests.get(f"https://api.pexels.com/v1/search?query={query}&per_page=6",
                 headers={"Authorization": PEXELS_KEY}).json()
for i, p in enumerate(r["photos"], 1):
    download(p["src"]["medium"], f"img{i}.jpg")

# 1 段 30 s 视频
r = requests.get(f"https://api.pexels.com/videos/search?query={query}&per_page=1",
                 headers={"Authorization": PEXELS_KEY}).json()
video_url = r["videos"][0]["video_files"][0]["link"]
download(video_url, "bgm.mp4")  # 当背景音乐/素材
print("✅ 素材拉取完成！")
