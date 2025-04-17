from flask import Flask, jsonify, request
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables del .env

app = Flask(__name__)

# Configuración de la base de datos
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS
    )

@app.route("/buscar-empresa/<id_anonimo_emp>", methods=["GET"])
def buscar_empresa(id_anonimo_emp):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM empresas WHERE id_anonimo_emp = %s", (id_anonimo_emp,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if row:
        keys = [
            "id_anonimo_emp", "anio", "ciiu", "descciiu", "sector", "ubigeo",
            "departamento", "provincia", "distrito", "tamanio_emp",
            "valor_estimado_minimo_venta", "valor_estimado_maximo_venta",
            "exporta", "valor_estimado_minimo_fob_dolar", "valor_estimado_maximo_fob_dolar",
            "fec_creacion"
        ]
        return jsonify(dict(zip(keys, row)))
    else:
        return jsonify({"mensaje": "Empresa no encontrada"}), 404

@app.route("/registrar-empresa", methods=["POST"])
def registrar_empresa():
    data = request.get_json()

    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO empresas (
            id_anonimo_emp, anio, ciiu, descciiu, sector, ubigeo,
            departamento, provincia, distrito, tamanio_emp,
            valor_estimado_minimo_venta, valor_estimado_maximo_venta,
            exporta, valor_estimado_minimo_fob_dolar, valor_estimado_maximo_fob_dolar,
            fec_creacion
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        data["id_anonimo_emp"],
        data["anio"],
        data["ciiu"],
        data["descciiu"],
        data["sector"],
        data["ubigeo"],
        data["departamento"],
        data["provincia"],
        data["distrito"],
        data["tamanio_emp"],
        data["valor_estimado_minimo_venta"],
        data["valor_estimado_maximo_venta"],
        data["exporta"],
        data["valor_estimado_minimo_fob_dolar"],
        data["valor_estimado_maximo_fob_dolar"],
        data["fec_creacion"]
    ))

    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"mensaje": "Empresa registrada exitosamente"}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
