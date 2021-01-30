--
-- PostgreSQL database dump
--

-- Dumped from database version 10.15 (Ubuntu 10.15-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.15 (Ubuntu 10.15-0ubuntu0.18.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: asignatura; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.asignatura (
    asignatura_id bigint NOT NULL,
    departamento_id bigint NOT NULL,
    nombre character varying(100) NOT NULL,
    descripcion character varying(1000)
);


ALTER TABLE public.asignatura OWNER TO postgres;

--
-- Name: asignatura_asignatura_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.asignatura_asignatura_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.asignatura_asignatura_id_seq OWNER TO postgres;

--
-- Name: asignatura_asignatura_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.asignatura_asignatura_id_seq OWNED BY public.asignatura.asignatura_id;


--
-- Name: asignatura_departamento_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.asignatura_departamento_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.asignatura_departamento_id_seq OWNER TO postgres;

--
-- Name: asignatura_departamento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.asignatura_departamento_id_seq OWNED BY public.asignatura.departamento_id;


--
-- Name: departamento; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.departamento (
    departamento_id bigint NOT NULL,
    nombre character varying(100),
    descripcion character varying(1000)
);


ALTER TABLE public.departamento OWNER TO postgres;

--
-- Name: departamento_departamento_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.departamento_departamento_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.departamento_departamento_id_seq OWNER TO postgres;

--
-- Name: departamento_departamento_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.departamento_departamento_id_seq OWNED BY public.departamento.departamento_id;


--
-- Name: profesor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.profesor (
    id bigint NOT NULL,
    nombre character varying(25),
    apellido character varying(50),
    escuela character varying(50),
    fecha_de_contratacion date,
    sueldo numeric
);


ALTER TABLE public.profesor OWNER TO postgres;

--
-- Name: profesor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.profesor_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.profesor_id_seq OWNER TO postgres;

--
-- Name: profesor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.profesor_id_seq OWNED BY public.profesor.id;


--
-- Name: asignatura asignatura_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.asignatura ALTER COLUMN asignatura_id SET DEFAULT nextval('public.asignatura_asignatura_id_seq'::regclass);


--
-- Name: asignatura departamento_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.asignatura ALTER COLUMN departamento_id SET DEFAULT nextval('public.asignatura_departamento_id_seq'::regclass);


--
-- Name: departamento departamento_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.departamento ALTER COLUMN departamento_id SET DEFAULT nextval('public.departamento_departamento_id_seq'::regclass);


--
-- Name: profesor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.profesor ALTER COLUMN id SET DEFAULT nextval('public.profesor_id_seq'::regclass);


--
-- Data for Name: asignatura; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.asignatura (asignatura_id, departamento_id, nombre, descripcion) FROM stdin;
3	2	Matemáticas	Ciencia formal que, partiendo de axiomas y siguiendo el razonamiento lógico, estudia las propiedades y relaciones entre entidades abstractas como números, figuras geométricas, iconos, glifos, o símbolos en general
4	2	Trigonometría	Rama de la matemática, cuyo significado etimológico es la medición de los triángulos
5	3	Biología	Rama de la ciencia que estudia los procesos naturales de los organismos vivos, considerando su anatomía, fisiología, evolución, desarrollo, distribución y relaciones
6	3	Ecosistema	Sistema biológico constituido por una comunidad de organismos vivos (biocenosis) y el medio físico donde se relacionan (biotopo)
1	1	Literatura	Arte de la expresión verbal
2	1	Castellano	Lengua romance procedente del latín hablado
\.


--
-- Data for Name: departamento; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.departamento (departamento_id, nombre, descripcion) FROM stdin;
2	Ciencias Exactas	Disciplinas que se basan en la observación y experimentación para crear conocimientos y cuyos contenidos pueden sistematizarse a partir del lenguaje matemático.
3	Ciencias Naturales	Ciencias que tienen por objeto el estudio de la naturaleza, siguiendo la modalidad del método científico conocida como método empírico-analítico.
1	Ciencias Sociales	Ramas de la ciencia relacionadas con la sociedad y el comportamiento humano.
\.


--
-- Data for Name: profesor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.profesor (id, nombre, apellido, escuela, fecha_de_contratacion, sueldo) FROM stdin;
1	Juanita	Perez	Gabriela Mistral	2011-10-30	234000
2	Bruce	Lee	Republica Popular China	1993-05-22	780945
3	Juan Alberto	Valdivieso	Sagrada Concepcion	2005-08-01	3400000
4	Pablo	Rojas	E-34	2011-10-30	300000
5	Nicolas	Echenique	Bendito Corazón de María	2005-08-30	8900000
6	Jericho	Jorquera	A-18 Abrazo de Maipu	2010-10-22	67500
7	Caupolicán	Catrileo	Santiago de la extremadura	2000-10-26	780000
8	José	Guerra	Santa María de la Dignidad	2021-01-14	300000
9	Jonathan	Oliva	Escuela E-491	2021-01-14	400000
10	Wong	Lee	Santiago de la extremadura	2000-10-26	780000
\.


--
-- Name: asignatura_asignatura_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.asignatura_asignatura_id_seq', 1, false);


--
-- Name: asignatura_departamento_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.asignatura_departamento_id_seq', 1, false);


--
-- Name: departamento_departamento_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.departamento_departamento_id_seq', 1, false);


--
-- Name: profesor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.profesor_id_seq', 10, true);


--
-- Name: asignatura asignatura_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.asignatura
    ADD CONSTRAINT asignatura_pkey PRIMARY KEY (asignatura_id);


--
-- Name: departamento departamento_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.departamento
    ADD CONSTRAINT departamento_pkey PRIMARY KEY (departamento_id);


--
-- Name: profesor profesor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.profesor
    ADD CONSTRAINT profesor_pkey PRIMARY KEY (id);


--
-- Name: asignatura fk_departamento; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.asignatura
    ADD CONSTRAINT fk_departamento FOREIGN KEY (departamento_id) REFERENCES public.departamento(departamento_id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

