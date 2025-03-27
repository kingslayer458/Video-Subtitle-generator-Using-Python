import os
import sys

# Check and install dependencies
try:
    import speech_recognition as sr
    import moviepy.editor as mp
    import whisper
    import pysrt
except ImportError:
    print("Installing required dependencies...")
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
                            'SpeechRecognition', 
                            'moviepy', 
                            'openai-whisper', 
                            'pysrt', 
                            'numpy==1.24.3'])
    
    # Reimport after installation
    import speech_recognition as sr
    import moviepy.editor as mp
    import whisper
    import pysrt

from typing import List, Tuple

class VideoSubtitleGenerator:
    def __init__(self, video_path: str, output_dir: str = 'output', model_size: str = 'base'):
        """
        Initialize the subtitle generator with video path and output directory
        
        Args:
            video_path (str): Path to the input video file
            output_dir (str): Directory to save subtitle files
            model_size (str): Size of Whisper model (tiny, base, small, medium, large)
        """
        self.video_path = video_path
        self.output_dir = output_dir
        
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Initialize speech recognition and transcription models
        self.recognizer = sr.Recognizer()
        
        try:
            self.whisper_model = whisper.load_model(model_size)
        except Exception as e:
            print(f"Error loading Whisper model: {e}")
            print("Attempting to download the model...")
            try:
                # Force download of the model
                whisper.load_model(model_size, download_root=os.path.join(os.path.expanduser('~'), '.cache', 'whisper'))
                self.whisper_model = whisper.load_model(model_size)
            except Exception as download_error:
                print(f"Could not download Whisper model: {download_error}")
                raise
    
    def extract_audio(self) -> str:
        """
        Extract audio from video file
        
        Returns:
            str: Path to extracted audio file
        """
        try:
            video = mp.VideoFileClip(self.video_path)
            audio_path = os.path.join(self.output_dir, "extracted_audio.wav")
            video.audio.write_audiofile(audio_path)
            return audio_path
        except Exception as e:
            print(f"Error extracting audio: {e}")
            raise
    
    def transcribe_audio(self, audio_path: str) -> List[dict]:
        """
        Transcribe audio using Whisper
        
        Args:
            audio_path (str): Path to audio file
        
        Returns:
            List of dictionaries containing transcription results
        """
        try:
            result = self.whisper_model.transcribe(audio_path, verbose=True)
            return result['segments']
        except Exception as e:
            print(f"Transcription error: {e}")
            raise
    
    def generate_srt_subtitles(self, segments: List[dict]) -> str:
        """
        Generate SRT subtitle file from transcription segments
        
        Args:
            segments (List[dict]): Transcription segments
        
        Returns:
            str: Path to generated SRT file
        """
        try:
            subs = pysrt.SubRipFile()
            
            for i, segment in enumerate(segments, 1):
                start_time = segment['start']
                end_time = segment['end']
                text = segment['text'].strip()
                
                sub = pysrt.SubRipItem(
                    index=i,
                    start=pysrt.SubRipTime(seconds=start_time),
                    end=pysrt.SubRipTime(seconds=end_time),
                    text=text
                )
                subs.append(sub)
            
            srt_path = os.path.join(self.output_dir, "subtitles.srt")
            subs.save(srt_path, encoding='utf-8')
            return srt_path
        except Exception as e:
            print(f"Error generating SRT: {e}")
            raise
    
    def generate_subtitles(self) -> Tuple[str, str]:
        """
        Main method to generate subtitles
        
        Returns:
            Tuple of (audio_path, subtitle_path)
        """
        audio_path = self.extract_audio()
        segments = self.transcribe_audio(audio_path)
        subtitle_path = self.generate_srt_subtitles(segments)
        
        return audio_path, subtitle_path

def main():
    # Example usage with error handling
    video_path = input("Enter the path to your video file: ")
    
    if not os.path.exists(video_path):
        print("Video file not found. Please check the path.")
        return
    
    generator = VideoSubtitleGenerator(video_path)
    
    try:
        audio_path, subtitle_path = generator.generate_subtitles()
        print(f"Audio extracted to: {audio_path}")
        print(f"Subtitles generated at: {subtitle_path}")
    except Exception as e:
        print(f"Subtitle generation failed: {e}")

if __name__ == "__main__":
    main()