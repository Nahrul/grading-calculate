from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def grading():
    final_grade = None
    status = None
    if request.method == 'POST':
        try:
            tugas = float(request.form['tugas'])
            uts = float(request.form['uts'])
            uas = float(request.form['uas'])
            final_grade = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
            if final_grade >= 60:
                status = 'LULUS'
            else:
                status = 'TIDAK LULUS'
        except Exception as e:
            final_grade = 'invalid input'

    return render_template('index.html', final_grade=final_grade, status=status)

if __name__ == '__main__':
    app.run(debug=True)

