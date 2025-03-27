import os
import sys
import traceback
import subprocess

def diagnose_file_access(file_path):
    """
    Comprehensive file access diagnostics
    """
    print("\n🕵️ FILE ACCESS DIAGNOSTICS 🕵️")
    
    # Normalize path
    normalized_path = os.path.abspath(os.path.normpath(file_path))
    
    # Print diagnostic information
    print(f"Attempted Path: {normalized_path}")
    print(f"Current User: {os.getlogin()}")
    print(f"Current Working Directory: {os.getcwd()}")
    
    # Check file existence
    if not os.path.exists(normalized_path):
        print("❌ ERROR: File does not exist")
        
        # Suggest possible paths
        possible_paths = [
            f"{normalized_path}.mp4",
            f"{normalized_path}.avi",
            f"{normalized_path}.mkv",
            f"D:\\{os.path.basename(normalized_path)}.mp4",
            f"D:\\{os.path.basename(normalized_path)}.avi",
            f"D:\\{os.path.basename(normalized_path)}.mkv"
        ]
        
        print("\nPossible corrections:")
        for path in possible_paths:
            if os.path.exists(path):
                print(f"✅ Found: {path}")
        
        return False
    
    # Check file readability
    try:
        with open(normalized_path, 'rb') as f:
            # Try to read first few bytes
            f.read(10)
        print("✅ File is readable")
    except PermissionError:
        print("❌ PERMISSION ERROR: Cannot read file")
        
        # Windows-specific permission check
        try:
            import win32security
            import ntsecuritycon as con
            
            # Get file security information
            sd = win32security.GetFileSecurity(
                normalized_path, 
                win32security.OWNER_SECURITY_INFORMATION | 
                win32security.GROUP_SECURITY_INFORMATION | 
                win32security.DACL_SECURITY_INFORMATION
            )
            
            # Get current user
            user, domain, _ = win32security.LookupAccountName("", os.getlogin())
            
            # Check user permissions
            print("\nDetailed Permission Check:")
            try:
                win32security.AccessCheck(sd, user, con.FILE_GENERIC_READ)
                print("✅ Theoretical read permission exists")
            except Exception as e:
                print(f"❌ Explicit read permission denied: {e}")
        
        except ImportError:
            print("🔍 Install pywin32 for detailed Windows permission analysis")
            print("Run: pip install pywin32")
        
        return False
    
    # Check file type
    try:
        import magic
        file_type = magic.from_file(normalized_path)
        print(f"📄 File Type: {file_type}")
    except ImportError:
        print("🔍 Install python-magic for file type detection")
        print("Run: pip install python-magic")
    
    # FFprobe video information
    try:
        result = subprocess.run([
            'ffprobe', 
            '-v', 'quiet', 
            '-print_format', 'json', 
            '-show_format', 
            '-show_streams', 
            normalized_path
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ FFprobe successfully read file metadata")
        else:
            print("❌ FFprobe could not read file metadata")
            print(result.stderr)
    except FileNotFoundError:
        print("❌ FFprobe not found. Install FFmpeg.")
    
    return True

def main():
    while True:
        # Prompt for video path
        video_path = input("\nEnter full path to video file (or 'quit' to exit): ").strip()
        
        # Exit condition
        if video_path.lower() in ['quit', 'exit', 'q']:
            print("👋 Exiting application...")
            break
        
        # Diagnose file access
        diagnose_file_access(video_path)

if __name__ == "__main__":
    main()