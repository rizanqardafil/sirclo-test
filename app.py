from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

weights = [
    {'tanggal': '2018-08-22', 'max': 50, 'min': 49},
    {'tanggal': '2018-08-21', 'max': 49, 'min': 49},
    {'tanggal': '2018-08-20', 'max': 52, 'min': 50},
    {'tanggal': '2018-08-19', 'max': 51, 'min': 50},
    {'tanggal': '2018-08-18', 'max': 50, 'min': 48},
]


@app.route('/')
def index():
    sorted_weights = sorted(weights, key=lambda w: w['tanggal'], reverse=True)
    perbedaan = max(w['max'] - w['min'] for w in weights)
    rata_rata_max = sum(w['max'] for w in weights) / len(weights)
    rata_rata_min = sum(w['min'] for w in weights) / len(weights)
    rata_rata_perbedaan = sum(w['max'] - w['min'] for w in weights) / len(weights)

    return render_template(
        'index.html',
        weights=sorted_weights,
        perbedaan=perbedaan,
        rata_rata_max=rata_rata_max,
        rata_rata_min=rata_rata_min,
        rata_rata_perbedaan = rata_rata_perbedaan
    )


@app.route('/weight/<tanggal>')
def show(tanggal):
    weight = next((w for w in weights if w['tanggal'] == tanggal), None)
    return render_template('show.html', weight=weight)


@app.route('/weight/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        tanggal = request.form['tanggal']
        max_weight = int(request.form['max_weight'])
        min_weight = int(request.form['min_weight'])
        weight = {'tanggal': tanggal, 'max': max_weight, 'min': min_weight}
        weights.append(weight)
        return redirect(url_for('index'))
    return render_template('create.html')


@app.route('/weight/edit/<tanggal>', methods=['GET', 'POST'])
def edit(tanggal):
    weight = next((w for w in weights if w['tanggal'] == tanggal), None)
    if weight:
        if request.method == 'POST':
            weight['max'] = int(request.form['max_weight'])
            weight['min'] = int(request.form['min_weight'])
            return redirect(url_for('index'))
        return render_template('edit.html', weight=weight)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
