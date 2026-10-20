from flask import Flask, render_template, request, jsonify
import platform
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.expanduser('~/cloud_server/uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/command', methods=['POST'])
def handle_command():
    command = request.get_json().get('command', '').strip().lower()

    if command == 'info':
        hostname = platform.node()
        os_name = platform.system()
        arch = platform.machine()
        try:
            with open('/proc/meminfo', 'r') as f:
                mem_total = f.readline().split()[1]
                mem_gb = round(int(mem_total) / 1024 / 1024, 1)
        except:
            mem_gb = "Unknown"

        return jsonify({"output": 
            "=== GIOI THIEU TRANG WEB ===\n"
            "- Chu so huu: Phong (Kovak)\n"
            "- Email: [Dien email cua ban]\n"
            "- Ly do: Tu xay dung may chu cloud ca nhan.\n"
            "- Muc dich: Luu tru du an, test code, va AI noi bo.\n\n"
            "=== THONG TIN MAY CHU ===\n"
            f"- Hostname: {hostname}\n"
            f"- OS: {os_name} ({arch})\n"
            f"- RAM: {mem_gb} GB\n"
            "- Hardware: Samsung Galaxy A6+ (Snapdragon 450)\n"
            "- PC Client: ASRock B760M PG Lightning D5\n\n"
            "=== KY NANG & DU AN ===\n"
            "- He dieu hanh: Linux\n"
            "- Lap trinh: Discord Bot\n"
            "- Thiet ke: CSS Themes"
        })
        
    elif command == 'cloud':
        files = os.listdir(UPLOAD_FOLDER)
        if not files:
            return jsonify({"output": "Cloud Storage is online.\nFolder is empty."})
        else:
            file_list = "\n".join([f"- {f}" for f in files])
            return jsonify({"output": f"Cloud Storage is online.\nFiles:\n{file_list}"})
    
    elif command == 'secret bakhi@gnohp':
        return jsonify({"output": "ACCESS GRANTED.\nLoading DumbBot Project...", "action": "open_secret"})
    
    elif command.startswith('secret'):
        return jsonify({"output": "ACCESS DENIED: Invalid key."})
    
    elif command == 'help':
        return jsonify({"output": "Commands:\n- info\n- cloud\n- secret <key>\n- clear"})
    
    elif command == 'clear':
        return jsonify({"output": "", "action": "clear"})
        
    else:
        return jsonify({"output": f"Command not found: {command}. Type 'help'."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
