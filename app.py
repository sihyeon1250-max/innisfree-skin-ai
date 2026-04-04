from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('survey.html')

@app.route('/survey')
def survey():
    return render_template('survey.html')

if __name__ == "__main__":
    import os
    # Render는 'PORT' 환경변수를 사용하므로 이를 읽어와야 합니다.
    port = int(os.environ.get("PORT", 10000)) 
    app.run(host='0.0.0.0', port=port)
