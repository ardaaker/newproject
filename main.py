from flask import Flask, render_template, request

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/')
def hello():
    return render_template('anasayfa.html')

@app.route('/iletisim')
def iletisim():
    return render_template('iletisim.html')

@app.route('/mesajkaydet', methods=['POST'])
def mesajkaydet():
    adsoyad = request.form.get('adsoyad')
    mail = request.form.get('email')
    mesaj = request.form.get('mesaj')
    cumle = adsoyad + mail + ' = ' + mesaj + '\n'
    f = open('musteri.txt' , 'a')
    f.write(cumle)
    f.close()
    return adsoyad + '' + 'thanks!'


if __name__ == "__main__":
    app.run()