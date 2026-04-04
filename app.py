import os
from flask import Flask, render_template

# 상위 폴더 경로를 명확히 지정
base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, 
            template_folder=os.path.join(base_dir, 'templates'),
            static_folder=os.path.join(base_dir, 'static'))

@app.route('/')
def index():
    # 여기서 확장자 .html이 붙어있는지 꼭 확인!
    return render_template('survey.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
