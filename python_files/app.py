from flask import Flask, render_template, request

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():  # put application's code here
    return render_template('./index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    fn = secure_filename(file.filename)
    # sleep(3)
    file.save(os.path.join('../uploads', fn))
    return {
        "success": True,
        "message": fn
    }


if __name__ == '__main__':
    app.run()
