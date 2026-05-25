# 🎬 B站 AI 总结助手 / Bilibili Video AI Summarizer

<p align="center">
  <img src="https://img.shields.io/github/license/ruatm1-wq/bili-summarizer?style=flat-square" alt="License">
  <img src="https://img.shields.io/github/stars/ruatm1-wq/bili-summarizer?style=flat-square" alt="Stars">
  <img src="https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square" alt="PRs Welcome">
</p>

[中文](#中文) | [English](#english)

---

## 中文

> 输入 B站 视频链接 → 自动提取字幕 → AI 生成结构化总结

### 功能
- 📥 **字幕提取**：自动下载 B站 视频字幕（无需登录）
- 🤖 **AI 总结**：DeepSeek 生成结构化报告（一句话总结/大纲/观点/行动建议）
- 📝 **保存结果**：输出为 JSON / Markdown

### 使用
```bash
pip install yt-dlp

# cookies.txt：从浏览器导出B站登录cookies，放到项目根目录
python cli.py "https://www.bilibili.com/video/BVxxx"
```

### 环境变量
| 变量 | 说明 |
|:-----|:-----|
| `DS_API_KEY` | DeepSeek API Key |

### 输出
```json
{ "title": "...", "transcript": "...", "summary": "...", "chars": 1234 }
```

---

## English

> Paste a Bilibili video link → Auto-extract subtitles → AI-generated structured summary

### Features
- 📥 **Subtitle extraction**: Auto-download Bilibili subtitles (no login cookies needed for most)
- 🤖 **AI Summary**: DeepSeek-powered structured reports
- 📝 **Output**: JSON / Markdown

### Usage
```bash
pip install yt-dlp

# Place cookies.txt (B站 login cookies from browser) in project root
python cli.py "https://www.bilibili.com/video/BVxxx"
```

### Environment
| Variable | Description |
|:---------|:------------|
| `DS_API_KEY` | DeepSeek API Key |

### Output
```json
{ "title": "...", "transcript": "...", "summary": "...", "chars": 1234 }
```
