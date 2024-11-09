import pyautogui
import time
import webbrowser


def auto_refresh(url, interval):
    # Mở trình duyệt đến URL đã cho
    webbrowser.open(url)
    time.sleep(5)  # Đợi một lúc để trang load xong

    try:
        while True:
            # Refresh trang bằng phím F5
            pyautogui.press("f5")
            print("Trang web đã được refresh.")
            time.sleep(interval)  # Đợi trước khi refresh lại
    except KeyboardInterrupt:
        print("Dừng refresh")


# Thay URL và khoảng thời gian refresh mong muốn (tính bằng giây)
url = "https://www.youtube.com/watch?v=iAqyuJ5rxvY"  # URL của trang bạn muốn reload
interval = 15  # khoảng thời gian giữa mỗi lần reload, tính bằng giây

auto_refresh(url, interval)
