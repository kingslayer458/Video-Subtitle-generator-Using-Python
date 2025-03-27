import os
import sys
import glob
import traceback

class VideoPathResolver:
    @staticmethod
    def resolve_video_path(input_path):
        """
        Comprehensive video file path resolution
        
        Args:
            input_path (str): User-provided file path
        
        Returns:
            str: Validated full path to video file or None
        """
        # Expand user path and normalize
        expanded_path = os.path.abspath(os.path.expanduser(input_path))
        
        # Case 1: Direct file path provided
        if os.path.isfile(expanded_path):
            return expanded_path
        
        # Case 2: Directory path - search for video files
        if os.path.isdir(expanded_path):
            # Common video file extensions
            video_extensions = ['*.mp4', '*.avi', '*.mkv', '*.mov', '*.wmv']
            
            # Search for video files in the directory
            video_files = []
            for ext in video_extensions:
                video_files.extend(glob.glob(os.path.join(expanded_path, ext)))
                video_files.extend(glob.glob(os.path.join(expanded_path, ext.upper())))
            
            if video_files:
                print("\n🎬 Multiple video files found:")
                for i, file in enumerate(video_files, 1):
                    print(f"{i}. {os.path.basename(file)}")
                
                while True:
                    try:
                        choice = input("\nEnter the number of the video file you want to use: ").strip()
                        index = int(choice) - 1
                        if 0 <= index < len(video_files):
                            return video_files[index]
                    except ValueError:
                        pass
                    print("❌ Invalid selection. Please try again.")
        
        # Case 3: Partial filename - search in current directory and D: drive
        search_paths = [
            os.getcwd(),  # Current directory
            r'D:\\'  # Root of D: drive
        ]
        
        partial_matches = []
        for search_path in search_paths:
            for root, _, files in os.walk(search_path):
                matches = [
                    os.path.join(root, file) 
                    for file in files 
                    if input_path.lower() in file.lower() and 
                    any(file.lower().endswith(ext) for ext in ['mp4', 'avi', 'mkv', 'mov', 'wmv'])
                ]
                partial_matches.extend(matches)
        
        if partial_matches:
            print("\n🔍 Partial matches found:")
            for i, match in enumerate(partial_matches, 1):
                print(f"{i}. {match}")
            
            while True:
                try:
                    choice = input("\nEnter the number of the file you want to use: ").strip()
                    index = int(choice) - 1
                    if 0 <= index < len(partial_matches):
                        return partial_matches[index]
                except ValueError:
                    pass
                print("❌ Invalid selection. Please try again.")
        
        # No valid path found
        print("\n❌ ERROR: Could not find a valid video file.")
        print("Suggestions:")
        print("1. Provide full path to the video file")
        print("2. Ensure the file exists")
        print("3. Check file extension (mp4, avi, mkv, etc.)")
        return None

def main():
    while True:
        # Prompt for video path
        video_path = input("\nEnter full path to video file (or 'quit' to exit): ").strip()
        
        # Exit condition
        if video_path.lower() in ['quit', 'exit', 'q']:
            print("👋 Exiting application...")
            break
        
        # Resolve video path
        resolved_path = VideoPathResolver.resolve_video_path(video_path)
        
        # If a valid path is found, proceed with subtitle generation
        if resolved_path:
            print(f"\n✅ Selected video file: {resolved_path}")
            
            # Here you would call your subtitle generation function
            # For now, just a placeholder
            print("Proceeding with subtitle generation...")
            
            try:
                # Your existing subtitle generation code would go here
                print("✅ Subtitle generation completed!")
            except Exception as e:
                print(f"❌ Subtitle generation error: {e}")
        else:
            print("❌ Invalid video file. Please try again.")

if __name__ == "__main__":
    main()