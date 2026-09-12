import os
import sys
import time
import shutil
import subprocess
import threading
from collections import deque

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

def smart_import(name, pip_name=None):
    pip_name = pip_name or name
    try:
        return __import__(name)
    except ImportError:
        print(f"[+] Installing {pip_name}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name])
        return __import__(name)

pygame = smart_import("pygame")
yt_dlp = smart_import("yt_dlp", "yt-dlp")

pygame.mixer.init()

music_queue = deque()
current_song = None
is_running = True
is_paused = False

def is_bad_version(title):
    bad_words = ["remix", "edit", "slowed", "reverb", "8d", "nightcore", "lofi", "cover", "karaoke", "instrumental", "tiktok", "sped up"]
    title_lower = title.lower()
    for w in bad_words:
        if w in title_lower:
            return True
    return False

def download_track(song_query):
    if not shutil.which("ffmpeg"):
        print("\n[Error] FFmpeg not found. Please add FFmpeg to your system PATH.")
        return None

    try:
        print(f"\n[System] Searching for: '{song_query}'...\n")

        # 1. Search 5 results first, without downloading
        ydl_opts_search = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': False,
            'skip_download': True,
        }
        with yt_dlp.YoutubeDL(ydl_opts_search) as ydl:
            result = ydl.extract_info(f"ytsearch5:{song_query} official audio", download=False)
            entries = result.get('entries', [])
            if not entries:
                print("[System] No results found")
                return None

            # 2. Score and pick best (avoid remix)
            best_entry = None
            for e in entries:
                if not is_bad_version(e.get('title','')):
                    best_entry = e
                    break

            # If all 5 are remixes, just take the first one as fallback
            if not best_entry:
                best_entry = entries[0]
                print(f"This is what best was found according to your Query: {best_entry['title']}")
            else:
                print(f"[System] Selected: {best_entry['title']}")
                time.sleep(0.2)
                print("This may take a while")

            video_url = best_entry['webpage_url']

        # 3. Now download the SELECTED url only
        cmd = [
            sys.executable, "-m", "yt_dlp",
            "--quiet",
            "--no-warnings",
            "--extract-audio",
            "--audio-format", "mp3",
            "--audio-quality", "0",
            video_url,
            "-o", "%(title)s.%(ext)s"
        ]

        result_dl = subprocess.run(cmd)

        if result_dl.returncode!= 0:
            print("\n[System Error]: Download failed")
            return None

        audio_files = [f for f in os.listdir('.') if f.endswith('.mp3')]
        if audio_files:
            return max(audio_files, key=os.path.getmtime)
        return None
    except Exception as e:
        print(f"\n[System Exception]: {e}")
        return None

def audio_player_worker():
    global current_song, is_running
    while is_running:
        if not pygame.mixer.music.get_busy() and not is_paused and music_queue:
            if current_song:
                safe_delete_file(current_song)
                current_song = None

            next_query = music_queue.popleft()
            file_path = download_track(next_query)

            if file_path and os.path.exists(file_path):
                current_song = file_path
                print(f"\n[Musik Player] Now Playing 🎵: {current_song}\n\nMusicShell> ", end="")
                try:
                    pygame.mixer.music.load(file_path)
                    pygame.mixer.music.play()
                except Exception as e:
                    print(f"\n[Player Error] Could not open file: {e}\nMusicShell> ", end="")
            else:
                print(f"\n[Player] Failed to load track for: '{next_query}'\nMusicShell> ", end="")

        elif current_song and not pygame.mixer.music.get_busy() and not is_paused and not music_queue:
            safe_delete_file(current_song)
            current_song = None
            print("\nMusicShell> ", end="")

        time.sleep(1)

def safe_delete_file(file_path):
    if file_path and os.path.exists(file_path):
        try:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            time.sleep(0.5)
            os.remove(file_path)
            print(f"\n[System Cleaning] Deleted temporary file: {file_path}")
        except Exception:
            pass

def main():
    global is_running, is_paused, current_song

    player_thread = threading.Thread(target=audio_player_worker, daemon=True)
    player_thread.start()

    os.system('cls' if os.name == 'nt' else 'clear')
    print("=== Welcome to the Free Open Music Queue Engine ===")
    print("Commands: 'add <song title>', 'pause', 'resume', 'skip', 'exit'\n")

    try:
        while True:
            user_input = input("MusicShell> ").strip()
            if not user_input:
                continue

            cmd_parts = user_input.split(" ", 1)
            cmd = cmd_parts[0].lower()

            if cmd == "exit":
                print("Shutting down...")
                is_running = False
                safe_delete_file(current_song)
                pygame.mixer.quit()
                break

            elif cmd == "add":
                if len(cmd_parts) < 2:
                    print(f"Error: Please provide a song name.")
                    continue
                query = cmd_parts[1]
                music_queue.append(query)
                print(f"Added to queue: '{query}'")

            elif cmd == "pause":
                if pygame.mixer.music.get_busy() and not is_paused:
                    pygame.mixer.music.pause()
                    is_paused = True
                    print("Paused.")
                else:
                    print("No music playing.")

            elif cmd == "resume":
                if is_paused:
                    pygame.mixer.music.unpause()
                    is_paused = False
                    print("Resumed.")

            elif cmd == "skip":
                print("Skipping track...")
                safe_delete_file(current_song)
                current_song = None
                is_paused = False

            elif cmd == "queue":
                if not music_queue and not pygame.mixer.music.get_busy():
                    print("Queue is empty.")
                else:
                    if current_song:
                        print(f"Playing: {current_song}")
                    print("Up Next:")
                    for idx, item in enumerate(music_queue, 1):
                        print(f" {idx}. {item}")
            else:
                print("Unknown command. Use: add, pause, resume, skip, queue, or exit.")

    except KeyboardInterrupt:
        is_running = False
        safe_delete_file(current_song)
        pygame.mixer.quit()

if __name__ == "__main__":
    main()