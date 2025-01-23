import subprocess
import time
import sys

def run_command(cmd):
    """Helper to run a shell command, print stdout/stderr, and return code."""
    print(f"\n[Running command]: {cmd}")
    proc = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print("[STDOUT]:", proc.stdout)
    print("[STDERR]:", proc.stderr)
    print("[Return code]:", proc.returncode)
    return proc.returncode

def main():
    print("Starting local test with a file I already have...")

    # No download step needed!
    # So we skip or remove the run_command("curl -k -L ....")

    # 1) Just re-encode the local file.
    ret = run_command("ffmpeg -y -i sample_960x400_ocean_with_audio.mp4 -c:v libx264 -c:a aac output.mp4")
    if ret != 0:
        print("FFmpeg re-encode failed. Exiting.")
        sys.exit(1)

    print("FFmpeg re-encode succeeded with your local MP4!")
    print("Now sleeping forever so you can see logs...")

    while True:
        time.sleep(600)


if __name__ == "__main__":
    main()
