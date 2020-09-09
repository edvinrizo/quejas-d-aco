CREATE TABLE tbl_region
(
    id_region_PK integer NOT NULL,
    nombre_region character varying(25)NOT NULL,
    CONSTRAINT tbl_region_pkey PRIMARY KEY (id_region_PK),
    CONSTRAINT nombre_region_key UNIQUE (nombre_region)
)


CREATE TABLE tbl_depto
(
    id_depto_PK integer NOT NULL,
    nombre_depto character varying(50) NOT NULL,
    id_region_FK integer NOT NULL,
    CONSTRAINT tbl_depto_pkey PRIMARY KEY (id_depto_PK),
    CONSTRAINT nombre_depto_key UNIQUE (nombre_depto),
    CONSTRAINT tbl_depto_tbl_region_PK FOREIGN KEY (id_region_FK)
        REFERENCES tbl_region (id_region_PK)
)

CREATE TABLE tbl_muni
(
    id_muni_PK integer NOT NULL,
    nombre_muni character varying(50) NOT NULL,
    "id_depto_FK" integer NOT NULL,
    CONSTRAINT tbl_muni_pkey PRIMARY KEY (id_muni_PK),
    CONSTRAINT tbl_muni_depto_FK FOREIGN KEY (id_depto_FK)
        REFERENCES tbl_depto (id_depto_PK)
)

CREATE TABLE tbl_comercio
(
    id_comercio_PK integer NOT NULL,
    razon_social character varying(100),
    razon_comercial character varying(100)NOT NULL,
    nit integer NOT NULL,
    pbx character varying(10),
    CONSTRAINT tbl_comercio_pkey PRIMARY KEY (id_comercio_PK),
    CONSTRAINT nit_key UNIQUE (nit)
)


CREATE TABLE tbl_sucursal
(
    id_sucursal_PK integer NOT NULL,
    nombre_sucursal character varying(200) NOT NULL,
    zona integer NOT NULL,
    direccion character varying(250) NOT NULL,
    referencia character varying(400),
    telefono character varying(10),
    id_comercio_FK integer NOT NULL,
    id_muni_FK integer NOT NULL,
    CONSTRAINT tbl_sucursal_pkey PRIMARY KEY (id_sucursal_PK),
    CONSTRAINT tbl_sucursal_uniq UNIQUE (id_comercio_FK, nombre_sucursal),
    CONSTRAINT zona_key UNIQUE (zona),
    CONSTRAINT tbl_sucursal_comercio_fkey FOREIGN KEY (id_comercio_FK)
        REFERENCES tbl_comercio (id_comercio_PK)
    CONSTRAINT tbl_sucursal_muni_FK FOREIGN KEY (id_muni_FK)
        REFERENCES tbl_muni (id_muni_PK)
)


CREATE TABLE tbl_formulario
(
    id_frmqueja_PK integer NOT NULL,
    fecha_registro date NOT NULL,
    nombre character varying(50),
    apellido character varying(50),
    fecha_incidente date NOT NULL,
    factura character varying(50) NOT NULL,
    detalle_queja text NOT NULL,
    solcitud text NOT NULL,
    id_sucursal_FK integer NOT NULL,
    CONSTRAINT tbl_formulario_pkey PRIMARY KEY (id_frmqueja_PK),
    CONSTRAINT tbl_formulario_fkey FOREIGN KEY (id_sucursal_FK)
        REFERENCES tbl_sucursal (id_sucursal_PK)
)


