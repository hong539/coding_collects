import argparse
import subprocess
import os

def download_exercise(track: str, exercise: str):
    """執行 exercism download 指令，下載指定的練習題。"""
    command = [
        "exercism", "download",
        "--exercise", exercise,
        "--track", track
    ]
    
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✅ 成功下載 {exercise} 到 Exercism 目錄！")
        print(result.stdout)
    else:
        print(f"❌ 下載失敗: {result.stderr}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="下載 Exercism 練習題")
    parser.add_argument("--exercise", required=True, help="練習題的 slug，如 hello-world")
    parser.add_argument("--track", required=True, help="語言的 slug，如 python, rust, go")
    
    args = parser.parse_args()
    
    download_exercise(args.track, args.exercise)