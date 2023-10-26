import speech_recognition as sr #Nhận dạng giọng nói
from gtts import gTTS #Chuyển văn bản âm thanh của google
import playsound #Phát âm thanh từ file mp3
import datetime as dt #Xử lý thời gian
import webbrowser as wb #Hiển thị các tài liệu tìm kiếm trên wed cho người dùng
import pywhatkit #Tự động mở yêu cầu tìm kiếm trong google
import os #Truy cập xử lý file hệ thống

# Chuyển từ giọng nói thành văn bản
def speak(text):
    tts = gTTS(text=text, lang='vi')
    filename='voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

# chuyển từ văn bản thành giọng nói
# khởi tạo trình nhận dạng
while(True):
    r=sr.Recognizer()
    now=dt.datetime.now()
    with sr.Microphone() as source:
        print("Listen....")
        # đọc dữ liệu âm thanh từ microphone
        audio_data = r.record(source, duration=5)
        try:
            text=r.recognize_google(audio_data,language='vi')
        except:
            text=""
        print(text)
        # PHẦN HIỂU
        # sau khi nói vào mic thì chuyển thành dạng text
        # ta xử lý cái text huấn luyện để cho trợ lý ảo có thể hiểu được và trả lời mình
        if text=="":
            robot_hd="Tôi đang lắng nghe bạn đây"
            speak(robot_hd)
        elif "Xin chào" in text:
            # robot_brain nói lại với bạn
            robot_hd="Xin chào bạn khỏe không, bạn cần gì"
            # hiển thị robot_brain trên màn hình terminal
            print(robot_hd)
            # nói ra robot_brain
            speak(robot_hd)
        elif "tôi là ai" in text:
            robot_hd="Bạn là Nguyễn Hữu Đang, sinh viên trường bkap"
            print(robot_hd)
            speak(robot_hd)
        elif "Hôm nay là ngày bao nhiêu" in text:
             # trả về một chuỗi biểu diễn giá trị ngày, giờ và thời gian
            robot_hd=now.strftime("Hôm nay là ngày: %d/%m/%Y")
            print(robot_hd)
            speak(robot_hd)
        elif "Bây giờ là mấy giờ" in text:
            # trả về một chuỗi biểu diễn ngày, giờ và thời gian
            robot_hd=now.strftime("%H:%M:%S")
            print(robot_hd)
            speak(robot_hd)
        elif "Google" in text:
            speak("Bạn muốn tìm gì ?")
            # đọc dữ liệu âm thanh từ micro
            audio_data = r.record(source, duration=5)
            # chuyển lời nói thành văn bản
            search = r.recognize_google(audio_data, language='vi')
            # copy đường link google
            url = f"https://www.google.com/search=?q={search}"
            # hiển thị đường dẫn url bằng cách sử dụng trình duyệt mặc định
            wb.open(url, new=0, autoraise=True)
            speak(f"Đây là {search} của bạn tìm kiếm trên google")
        elif "YouTube" in text:
            speak("Bạn muốn tìm kiếm gì ?")
            # đọc dữ liệu âm thanh từ micro
            audio_data = r.record(source, duration=5)
             # chuyển lời nói thành văn bản
            search=r.recognize_google(audio_data,language='vi')
            # reaplace() phương thức thay thế một cụm từ được chỉ định bằng một cụm từ được chỉ định
            video = search.replace('mở','')
            speak('Video của bạn đã được mở, hãy thưởng thức nó' + video)
            # tự động mở Youtube
            pywhatkit.playonyt(video)
        elif "Mở Zalo" in text:
            speak("Mở file Zalo")
            # 'r' trước một chuỗi yêu cầu trình thông dịch Python coi các dấu gạch chéo ngược là ký tự chữ thô
            zalo = r"C:\Users\nhd11\AppData\Local\Programs\Zalo\Zalo.exe"
            os.startfile(zalo)
        elif "tắt máy tính" in text:
            speak("tắt máy tính")
            # pc = r"C:\Users\nhd11\OneDrive\Desktop\shutdown.lnk"
            os.system("shutdown /p")
        elif "tạm biệt" in text:
            robot_hd="Chào tạm biệt bạn"
            print(robot_hd)
            speak(robot_hd)
            break
        else:
            robot_hd="Tôi chưa nghe rõ hãy thử lại"
            speak(robot_hd)