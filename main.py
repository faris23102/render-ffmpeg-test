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
    print("Starting FFmpeg test script on Render...")

    # 1) Download a short 1MB MP4 (Big Buck Bunny sample)
    ret = run_command("curl -k -L https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4 -o test_input.mp4")

    if ret != 0:
        print("Download failed. Exiting.")
        sys.exit(1)

    # 2) Re-encode with FFmpeg
    ret = run_command("ffmpeg -y -i test_input.mp4 -c:v libx264 -c:a aac output.mp4")
    if ret != 0:
        print("FFmpeg re-encode failed. Exiting.")
        sys.exit(1)

    print("FFmpeg re-encode succeeded! Check 'output.mp4' if needed.")
    print("Now sleeping forever so you can see logs...")

    # Sleep forever so the service doesn't exit.
    while True:
        time.sleep(600)

if __name__ == "__main__":
    main()
