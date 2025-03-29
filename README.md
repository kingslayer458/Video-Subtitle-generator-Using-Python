# Video-Subtitle-generator-Using-Python

A Python tool that automatically generates subtitles (SRT files) from video files using OpenAI's Whisper speech recognition model.

# **Video Subtitle Generator**  

[![GitHub stars](https://img.shields.io/github/stars/kingslayer458/Video-Subtitle-generator-Using-Python?style=social)](https://github.com/kingslayer458/Video-Subtitle-generator-Using-Python/stargazers)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  

A **Python-based tool** that automatically generates **SRT subtitles** from video files using **OpenAI's Whisper** for accurate speech recognition.  

## **✨ Features**  
✅ Extracts audio from video files (MP4, MOV, AVI, etc.)  
✅ Supports **multiple Whisper model sizes** (tiny, base, small, medium, large)  
✅ Generates **timed SRT subtitles**  
✅ **Auto-installs dependencies** (if missing)  
✅ Works on **Windows, macOS, and Linux**  

---

## **🚀 Installation & Setup**  

### **Prerequisites**  
- **Python 3.7+**  
- **FFmpeg** (Required for audio extraction)  

### **1. Clone the Repository**  
```bash
git clone https://github.com/kingslayer458/Video-Subtitle-generator-Using-Python.git
cd Video-Subtitle-generator-Using-Python
```  

### **2. Create & Activate a Virtual Environment**  
```bash
# Create a virtual environment
python -m venv subtitle_env

# Activate it
# Windows:
subtitle_env\Scripts\activate
# macOS/Linux:
source subtitle_env/bin/activate
```  

### **3. Install Dependencies**  
```bash
pip install numpy==1.24.3 SpeechRecognition moviepy openai-whisper pysrt
```  

---

## **🛠 Usage**  

### **Option 1: Run Directly (Interactive Mode)**  
```bash
python subtitle.py
```  
➡️ **Enter the path to your video file** when prompted.  

### **Option 2: Use as a Python Module**  
```python
from subtitle_generator import VideoSubtitleGenerator

# Initialize with video path (optional: model_size="base")
generator = VideoSubtitleGenerator("your_video.mp4")

# Generate subtitles (returns audio_path, srt_path)
audio_path, subtitle_path = generator.generate_subtitles()
print(f"Subtitles saved at: {subtitle_path}")
```  

### **Optional: Specify Whisper Model Size**  
```python
# Available models: tiny, base, small, medium, large
generator = VideoSubtitleGenerator("video.mp4", model_size="medium")
```  

---

## **📂 Output Files**  
- **`extracted_audio.wav`** (Extracted audio from video)  
- **`subtitles.srt`** (Generated subtitles in SRT format)  

By default, files are saved in the **`output/`** folder.  

---

## **⚡ Performance Tips**  
- For **short videos**, use `model_size="base"` (faster).  
- For **high accuracy**, use `model_size="large"` (slower but more precise).  
- **First run** will download the Whisper model (~100MB–3GB depending on size).  

---

## **🔧 Troubleshooting**  
### **1. FFmpeg Not Found**  
Install FFmpeg based on your OS:  
- **Windows**: Download from [ffmpeg.org](https://ffmpeg.org/)  
- **macOS**: `brew install ffmpeg`  
- **Linux**: `sudo apt install ffmpeg`  

### **2. Whisper Model Download Issues**  
- Check internet connection.  
- Manually download models using:  
  ```bash
  whisper download-model base
  ```  

### **3. Dependencies Conflict**  
Use the provided `numpy==1.24.2` to avoid compatibility issues.  

---

## **🤝 Contributing**  
Contributions are welcome!  
1. **Fork** the repository  
2. Create a **new branch** (`git checkout -b feature`)  
3. **Commit** changes (`git commit -m 'Add feature'`)  
4. **Push** to the branch (`git push origin feature`)  
5. Open a **Pull Request**  

---

## **📜 License**  
This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.  

---
### **⭐ Star the Repo**  
If you find this useful, **star the repo** to show support!  
🔗 **[GitHub Link](https://github.com/kingslayer458/Video-Subtitle-generator-Using-Python)**  

---

  

Let me know if you'd like any modifications! 🚀
