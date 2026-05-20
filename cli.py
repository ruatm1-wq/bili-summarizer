import sys, json, subprocess, re, urllib.request
import os
from pathlib import Path

BASE = Path(__file__).parent
COOKIES = BASE / "cookies.txt"
OUTPUT = Path("D:/我的工作台/02-知识库/02-产出")
DS_KEY = os.getenv("DS_API_KEY", "")


def get_subs(url):
    result = subprocess.run(
        ["yt-dlp", "--cookies", str(COOKIES), "--skip-download",
         "--write-subs", "--sub-langs", "ai-zh", "--convert-subs", "srt",
         "-o", str(OUTPUT / "%(title)s.%(ext)s"), url],
        capture_output=True, text=True, timeout=120,
    )
    if result.returncode != 0:
        raise RuntimeError("下载字幕失败")
    srt_files = list(OUTPUT.glob("*.zh-Hans.srt")) or list(OUTPUT.glob("*.zh.srt")) or list(OUTPUT.glob("*.ai-zh.srt")) or list(OUTPUT.glob("*.srt"))
    if not srt_files:
        raise RuntimeError("没有字幕文件")
    text = srt_files[0].read_text("utf-8")
    parts = []
    for line in text.split("\n"):
        line = line.strip()
        if re.match(r"^\d+$", line) or re.match(r"^\d+:", line):
            continue
        if line:
            parts.append(line)
    return " ".join(parts), srt_files[0].stem.replace(".zh", "").replace(".ai-zh", "")


def summarize(text, title):
    prompt = f"为以下视频字幕做结构化总结。\n格式：\n## 一句话总结\n## 内容大纲\n## 关键观点\n## 行动建议\n\n标题：{title}\n字幕：{text[:8000]}"
    data = json.dumps({"model": "deepseek-chat", "messages": [{"role": "user", "content": prompt}], "stream": False}).encode()
    req = urllib.request.Request("https://api.deepseek.com/v1/chat/completions", data=data, headers={"Authorization": f"Bearer {DS_KEY}", "Content-Type": "application/json"})
    resp = urllib.request.urlopen(req, timeout=120)
    return json.loads(resp.read())["choices"][0]["message"]["content"]


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else ""
    if not url:
        print(json.dumps({"error": "no url"}))
        sys.exit(1)
    try:
        transcript, title = get_subs(url)
        summary = summarize(transcript, title)
        out = OUTPUT / "summary" / f"{title[:30]}.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(f"# {title}\n\n## 转录\n\n{transcript}\n\n## 总结\n\n{summary}", encoding="utf-8")
        print(json.dumps({"title": title, "transcript": transcript[:3000], "summary": summary, "chars": len(transcript)}))
    except Exception as e:
        print(json.dumps({"error": str(e)[:300]}))
