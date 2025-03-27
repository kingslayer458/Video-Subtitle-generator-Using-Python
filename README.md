# Video-Subtitle-generator-Using-Python


# Video Subtitle Generator

A Python tool that automatically generates subtitles (SRT files) from video files using OpenAI's Whisper speech recognition model.

## Features

- Extracts audio from video files (MP4, MOV, AVI, etc.)
- Transcribes speech to text using Whisper AI
- Generates properly timed SRT subtitle files
- Supports multiple Whisper model sizes (tiny, base, small, medium, large)
- Automatic dependency installation

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/kingslayer458/Video-Subtitle-generator-Using-Python.git
  
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   Or let the script install them automatically on first run.

## Usage

Run the script with Python:
```bash
python subtitle.py
```

When prompted, enter the path to your video file.

Alternatively, you can use the class directly in your Python code:
```python
from subtitle_generator import VideoSubtitleGenerator

generator = VideoSubtitleGenerator("path/to/your/video.mp4", model_size="base")
audio_path, subtitle_path = generator.generate_subtitles()
```

### Parameters
- `video_path`: Path to the input video file (required)
- `output_dir`: Directory to save output files (default: 'output')
- `model_size`: Whisper model size (default: 'base', options: tiny, base, small, medium, large)

## Output

The script will create:
1. An extracted audio file (`extracted_audio.wav`)
2. A subtitle file (`subtitles.srt`) in the specified output directory

## Requirements

- Python 3.7+
- FFmpeg (must be installed and in your system PATH)

### Python Dependencies
- SpeechRecognition
- moviepy
- openai-whisper
- pysrt
- numpy

These will be automatically installed if missing when you run the script.

## Troubleshooting

1. **FFmpeg not found**:
   - Install FFmpeg on your system
   - On Windows: Download from https://ffmpeg.org/ and add to PATH
   - On macOS: `brew install ffmpeg`
   - On Linux: `sudo apt install ffmpeg`

2. **Whisper model download issues**:
   - The script will attempt to download the model automatically
   - For manual download, see Whisper documentation

3. **Large video files**:
   - For very long videos, consider using a smaller model first
   - Processing may take significant time and memory

## Contributing

Contributions are welcome! Please open an issue or pull request for any improvements.

## License

MIT License - see LICENSE file for details
