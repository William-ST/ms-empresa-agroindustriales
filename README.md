### 1. Ejecutar con Docker Compose

```bash
docker-compose up --build
```

Levantará PostgreSQL y cargará automáticamente los datos del CSV. También expondrá el microservicio en:

```
http://localhost:5000
```

### 2. Endpoints disponibles

#### `GET /buscar-empresa/<id_anonimo_emp>`

Consulta una empresa por su ID:

```
GET http://localhost:5000/buscar-empresa/75115C6CA19EB6B9D13AA9D4DC73042E
```

#### `POST /registrar-empresa`

Registra una nueva empresa en la base de datos.

```
POST http://localhost:5000/registrar-empresa
Content-Type: application/json

{
"id_anonimo_emp": "TEST123",
"anio": 2023,
"ciiu": "1000",
"descciiu": "EMPRESA DE PRUEBA",
"sector": "MANUFACTURA",
"ubigeo": "110101",
"departamento": "ICA",
"provincia": "ICA",
"distrito": "ICA",
"tamanio_emp": "PEQUEÑA",
"valor_estimado_minimo_venta": 10000,
"valor_estimado_maximo_venta": 50000,
"exporta": "NO",
"valor_estimado_minimo_fob_dolar": 0,
"valor_estimado_maximo_fob_dolar": 0,
"fec_creacion": "20240401"
}
```
