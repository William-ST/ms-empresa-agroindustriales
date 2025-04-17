CREATE TABLE IF NOT EXISTS empresas (
    id_anonimo_emp VARCHAR PRIMARY KEY,
    anio INT,
    ciiu VARCHAR,
    descciiu TEXT,
    sector TEXT,
    ubigeo VARCHAR,
    departamento TEXT,
    provincia TEXT,
    distrito TEXT,
    tamanio_emp TEXT,
    valor_estimado_minimo_venta NUMERIC,
    valor_estimado_maximo_venta NUMERIC,
    exporta TEXT,
    valor_estimado_minimo_fob_dolar NUMERIC,
    valor_estimado_maximo_fob_dolar NUMERIC,
    fec_creacion VARCHAR
);

-- Importar CSV
COPY empresas FROM '/docker-entrypoint-initdb.d/empresas_agroindustriales_ica_2023.csv' 
WITH (FORMAT csv, HEADER, DELIMITER ';');
