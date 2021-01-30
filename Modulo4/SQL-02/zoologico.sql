--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4
-- Dumped by pg_dump version 12.4

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: animal; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.animal (
    animal_id integer NOT NULL,
    animal_nombre character(50) NOT NULL
);


ALTER TABLE public.animal OWNER TO postgres;

--
-- Name: animal_animal_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.animal_animal_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.animal_animal_id_seq OWNER TO postgres;

--
-- Name: animal_animal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.animal_animal_id_seq OWNED BY public.animal.animal_id;


--
-- Name: categoria; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categoria (
    categoria_id integer NOT NULL,
    categoria_nombre character(50) NOT NULL
);


ALTER TABLE public.categoria OWNER TO postgres;

--
-- Name: categoria_categoria_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.categoria_categoria_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.categoria_categoria_id_seq OWNER TO postgres;

--
-- Name: categoria_categoria_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.categoria_categoria_id_seq OWNED BY public.categoria.categoria_id;


--
-- Name: detalle; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.detalle (
    categoria_fk_id integer NOT NULL,
    animal_fk_id integer NOT NULL,
    detalle_id integer NOT NULL
);


ALTER TABLE public.detalle OWNER TO postgres;

--
-- Name: detalle_detalle_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.detalle_detalle_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.detalle_detalle_id_seq OWNER TO postgres;

--
-- Name: detalle_detalle_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.detalle_detalle_id_seq OWNED BY public.detalle.detalle_id;


--
-- Name: animal animal_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.animal ALTER COLUMN animal_id SET DEFAULT nextval('public.animal_animal_id_seq'::regclass);


--
-- Name: categoria categoria_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categoria ALTER COLUMN categoria_id SET DEFAULT nextval('public.categoria_categoria_id_seq'::regclass);


--
-- Name: detalle detalle_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detalle ALTER COLUMN detalle_id SET DEFAULT nextval('public.detalle_detalle_id_seq'::regclass);


--
-- Data for Name: animal; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.animal (animal_id, animal_nombre) FROM stdin;
\.


--
-- Data for Name: categoria; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.categoria (categoria_id, categoria_nombre) FROM stdin;
\.


--
-- Data for Name: detalle; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.detalle (categoria_fk_id, animal_fk_id, detalle_id) FROM stdin;
\.


--
-- Name: animal_animal_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.animal_animal_id_seq', 1, false);


--
-- Name: categoria_categoria_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.categoria_categoria_id_seq', 1, false);


--
-- Name: detalle_detalle_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.detalle_detalle_id_seq', 1, false);


--
-- Name: animal animal_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.animal
    ADD CONSTRAINT animal_pkey PRIMARY KEY (animal_id);


--
-- Name: categoria categoria_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categoria
    ADD CONSTRAINT categoria_pkey PRIMARY KEY (categoria_id);


--
-- Name: detalle detalle_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detalle
    ADD CONSTRAINT detalle_pkey PRIMARY KEY (detalle_id);


--
-- Name: detalle detalle_animal_fk_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detalle
    ADD CONSTRAINT detalle_animal_fk_id_fkey FOREIGN KEY (animal_fk_id) REFERENCES public.animal(animal_id);


--
-- Name: detalle detalle_categoria_fk_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.detalle
    ADD CONSTRAINT detalle_categoria_fk_id_fkey FOREIGN KEY (categoria_fk_id) REFERENCES public.categoria(categoria_id);


--
-- PostgreSQL database dump complete
--

