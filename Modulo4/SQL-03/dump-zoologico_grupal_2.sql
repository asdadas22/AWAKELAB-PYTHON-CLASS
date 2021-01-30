--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4
-- Dumped by pg_dump version 12.4

-- Started on 2021-01-21 22:06:15

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
-- TOC entry 3 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- TOC entry 2920 (class 0 OID 0)
-- Dependencies: 3
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 207 (class 1259 OID 25072)
-- Name: animales; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.animales (
    animal_id integer NOT NULL,
    animal_nombre character(50),
    area_fk_id integer NOT NULL,
    edad integer DEFAULT 2 NOT NULL,
    CONSTRAINT valid_range CHECK ((edad >= 2))
);


ALTER TABLE public.animales OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 25070)
-- Name: animales_animal_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.animales_animal_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.animales_animal_id_seq OWNER TO postgres;

--
-- TOC entry 2921 (class 0 OID 0)
-- Dependencies: 206
-- Name: animales_animal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.animales_animal_id_seq OWNED BY public.animales.animal_id;


--
-- TOC entry 203 (class 1259 OID 25051)
-- Name: area; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.area (
    area_id integer NOT NULL,
    nombre_area character(50)
);


ALTER TABLE public.area OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 25049)
-- Name: area_area_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.area_area_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.area_area_id_seq OWNER TO postgres;

--
-- TOC entry 2922 (class 0 OID 0)
-- Dependencies: 202
-- Name: area_area_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.area_area_id_seq OWNED BY public.area.area_id;


--
-- TOC entry 213 (class 1259 OID 25111)
-- Name: aves; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.aves (
    aves_id integer NOT NULL,
    animal_fk_id integer NOT NULL
);


ALTER TABLE public.aves OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 25109)
-- Name: aves_aves_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.aves_aves_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.aves_aves_id_seq OWNER TO postgres;

--
-- TOC entry 2923 (class 0 OID 0)
-- Dependencies: 212
-- Name: aves_aves_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.aves_aves_id_seq OWNED BY public.aves.aves_id;


--
-- TOC entry 211 (class 1259 OID 25098)
-- Name: insectos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.insectos (
    insectos_id integer NOT NULL,
    animal_fk_id integer NOT NULL
);


ALTER TABLE public.insectos OWNER TO postgres;

--
-- TOC entry 210 (class 1259 OID 25096)
-- Name: insectos_insectos_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.insectos_insectos_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.insectos_insectos_id_seq OWNER TO postgres;

--
-- TOC entry 2924 (class 0 OID 0)
-- Dependencies: 210
-- Name: insectos_insectos_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.insectos_insectos_id_seq OWNED BY public.insectos.insectos_id;


--
-- TOC entry 209 (class 1259 OID 25085)
-- Name: mamiferos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.mamiferos (
    mamifero_id integer NOT NULL,
    animal_fk_id integer NOT NULL
);


ALTER TABLE public.mamiferos OWNER TO postgres;

--
-- TOC entry 208 (class 1259 OID 25083)
-- Name: mamiferos_mamifero_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.mamiferos_mamifero_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mamiferos_mamifero_id_seq OWNER TO postgres;

--
-- TOC entry 2925 (class 0 OID 0)
-- Dependencies: 208
-- Name: mamiferos_mamifero_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.mamiferos_mamifero_id_seq OWNED BY public.mamiferos.mamifero_id;


--
-- TOC entry 219 (class 1259 OID 25150)
-- Name: novedades; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.novedades (
    novedades_id integer NOT NULL,
    detalle character(100) NOT NULL
);


ALTER TABLE public.novedades OWNER TO postgres;

--
-- TOC entry 218 (class 1259 OID 25148)
-- Name: novedades_novedades_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.novedades_novedades_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.novedades_novedades_id_seq OWNER TO postgres;

--
-- TOC entry 2926 (class 0 OID 0)
-- Dependencies: 218
-- Name: novedades_novedades_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.novedades_novedades_id_seq OWNED BY public.novedades.novedades_id;


--
-- TOC entry 217 (class 1259 OID 25137)
-- Name: peces; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.peces (
    peces_id integer NOT NULL,
    animal_fk_id integer NOT NULL
);


ALTER TABLE public.peces OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 25135)
-- Name: peces_peces_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.peces_peces_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.peces_peces_id_seq OWNER TO postgres;

--
-- TOC entry 2927 (class 0 OID 0)
-- Dependencies: 216
-- Name: peces_peces_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.peces_peces_id_seq OWNED BY public.peces.peces_id;


--
-- TOC entry 215 (class 1259 OID 25124)
-- Name: reptiles; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.reptiles (
    reptiles_id integer NOT NULL,
    animal_fk_id integer NOT NULL
);


ALTER TABLE public.reptiles OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 25122)
-- Name: reptiles_reptiles_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.reptiles_reptiles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reptiles_reptiles_id_seq OWNER TO postgres;

--
-- TOC entry 2928 (class 0 OID 0)
-- Dependencies: 214
-- Name: reptiles_reptiles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.reptiles_reptiles_id_seq OWNED BY public.reptiles.reptiles_id;


--
-- TOC entry 205 (class 1259 OID 25059)
-- Name: trabajador; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.trabajador (
    trabajador_id integer NOT NULL,
    area_fk_id integer NOT NULL,
    rol character(50) NOT NULL,
    telefono character(50) NOT NULL,
    nombre_trabajador character(50) NOT NULL
);


ALTER TABLE public.trabajador OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 25057)
-- Name: trabajador_trabajador_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.trabajador_trabajador_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.trabajador_trabajador_id_seq OWNER TO postgres;

--
-- TOC entry 2929 (class 0 OID 0)
-- Dependencies: 204
-- Name: trabajador_trabajador_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.trabajador_trabajador_id_seq OWNED BY public.trabajador.trabajador_id;


--
-- TOC entry 2737 (class 2604 OID 25075)
-- Name: animales animal_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.animales ALTER COLUMN animal_id SET DEFAULT nextval('public.animales_animal_id_seq'::regclass);


--
-- TOC entry 2735 (class 2604 OID 25054)
-- Name: area area_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.area ALTER COLUMN area_id SET DEFAULT nextval('public.area_area_id_seq'::regclass);


--
-- TOC entry 2742 (class 2604 OID 25114)
-- Name: aves aves_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aves ALTER COLUMN aves_id SET DEFAULT nextval('public.aves_aves_id_seq'::regclass);


--
-- TOC entry 2741 (class 2604 OID 25101)
-- Name: insectos insectos_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.insectos ALTER COLUMN insectos_id SET DEFAULT nextval('public.insectos_insectos_id_seq'::regclass);


--
-- TOC entry 2740 (class 2604 OID 25088)
-- Name: mamiferos mamifero_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mamiferos ALTER COLUMN mamifero_id SET DEFAULT nextval('public.mamiferos_mamifero_id_seq'::regclass);


--
-- TOC entry 2745 (class 2604 OID 25153)
-- Name: novedades novedades_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.novedades ALTER COLUMN novedades_id SET DEFAULT nextval('public.novedades_novedades_id_seq'::regclass);


--
-- TOC entry 2744 (class 2604 OID 25140)
-- Name: peces peces_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.peces ALTER COLUMN peces_id SET DEFAULT nextval('public.peces_peces_id_seq'::regclass);


--
-- TOC entry 2743 (class 2604 OID 25127)
-- Name: reptiles reptiles_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reptiles ALTER COLUMN reptiles_id SET DEFAULT nextval('public.reptiles_reptiles_id_seq'::regclass);


--
-- TOC entry 2736 (class 2604 OID 25062)
-- Name: trabajador trabajador_id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trabajador ALTER COLUMN trabajador_id SET DEFAULT nextval('public.trabajador_trabajador_id_seq'::regclass);


--
-- TOC entry 2902 (class 0 OID 25072)
-- Dependencies: 207
-- Data for Name: animales; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.animales (animal_id, animal_nombre, area_fk_id, edad) FROM stdin;
1	buho                                              	1	2
2	condor                                            	1	2
4	picaflor                                          	1	2
5	loro                                              	1	2
3	paloma                                            	1	30
6	lajartija                                         	2	10
7	tortuga                                           	2	5
8	iguana                                            	2	14
9	cocodrilo                                         	2	18
10	comodo                                            	2	6
\.


--
-- TOC entry 2898 (class 0 OID 25051)
-- Dependencies: 203
-- Data for Name: area; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.area (area_id, nombre_area) FROM stdin;
1	Area 1                                            
2	Area 2                                            
3	Area 3                                            
4	Area 4                                            
5	Area 5                                            
6	Area 0                                            
\.


--
-- TOC entry 2908 (class 0 OID 25111)
-- Dependencies: 213
-- Data for Name: aves; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.aves (aves_id, animal_fk_id) FROM stdin;
\.


--
-- TOC entry 2906 (class 0 OID 25098)
-- Dependencies: 211
-- Data for Name: insectos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.insectos (insectos_id, animal_fk_id) FROM stdin;
\.


--
-- TOC entry 2904 (class 0 OID 25085)
-- Dependencies: 209
-- Data for Name: mamiferos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.mamiferos (mamifero_id, animal_fk_id) FROM stdin;
\.


--
-- TOC entry 2914 (class 0 OID 25150)
-- Dependencies: 219
-- Data for Name: novedades; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.novedades (novedades_id, detalle) FROM stdin;
\.


--
-- TOC entry 2912 (class 0 OID 25137)
-- Dependencies: 217
-- Data for Name: peces; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.peces (peces_id, animal_fk_id) FROM stdin;
\.


--
-- TOC entry 2910 (class 0 OID 25124)
-- Dependencies: 215
-- Data for Name: reptiles; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.reptiles (reptiles_id, animal_fk_id) FROM stdin;
\.


--
-- TOC entry 2900 (class 0 OID 25059)
-- Dependencies: 205
-- Data for Name: trabajador; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.trabajador (trabajador_id, area_fk_id, rol, telefono, nombre_trabajador) FROM stdin;
2	2	supervisor                                        	98345692                                          	Felipe                                            
3	3	supervisor                                        	98345692                                          	Paulina                                           
4	4	supervisor                                        	98345692                                          	Juanita                                           
5	5	supervisor                                        	98345692                                          	Daniel                                            
1	1	supervisor                                        	234567891                                         	Raul                                              
\.


--
-- TOC entry 2930 (class 0 OID 0)
-- Dependencies: 206
-- Name: animales_animal_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.animales_animal_id_seq', 10, true);


--
-- TOC entry 2931 (class 0 OID 0)
-- Dependencies: 202
-- Name: area_area_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.area_area_id_seq', 6, true);


--
-- TOC entry 2932 (class 0 OID 0)
-- Dependencies: 212
-- Name: aves_aves_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.aves_aves_id_seq', 1, false);


--
-- TOC entry 2933 (class 0 OID 0)
-- Dependencies: 210
-- Name: insectos_insectos_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.insectos_insectos_id_seq', 1, false);


--
-- TOC entry 2934 (class 0 OID 0)
-- Dependencies: 208
-- Name: mamiferos_mamifero_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.mamiferos_mamifero_id_seq', 1, false);


--
-- TOC entry 2935 (class 0 OID 0)
-- Dependencies: 218
-- Name: novedades_novedades_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.novedades_novedades_id_seq', 1, false);


--
-- TOC entry 2936 (class 0 OID 0)
-- Dependencies: 216
-- Name: peces_peces_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.peces_peces_id_seq', 1, false);


--
-- TOC entry 2937 (class 0 OID 0)
-- Dependencies: 214
-- Name: reptiles_reptiles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reptiles_reptiles_id_seq', 1, false);


--
-- TOC entry 2938 (class 0 OID 0)
-- Dependencies: 204
-- Name: trabajador_trabajador_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.trabajador_trabajador_id_seq', 5, true);


--
-- TOC entry 2751 (class 2606 OID 25077)
-- Name: animales animales_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.animales
    ADD CONSTRAINT animales_pkey PRIMARY KEY (animal_id);


--
-- TOC entry 2747 (class 2606 OID 25056)
-- Name: area area_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.area
    ADD CONSTRAINT area_pkey PRIMARY KEY (area_id);


--
-- TOC entry 2757 (class 2606 OID 25116)
-- Name: aves aves_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aves
    ADD CONSTRAINT aves_pkey PRIMARY KEY (aves_id);


--
-- TOC entry 2755 (class 2606 OID 25103)
-- Name: insectos insectos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.insectos
    ADD CONSTRAINT insectos_pkey PRIMARY KEY (insectos_id);


--
-- TOC entry 2753 (class 2606 OID 25090)
-- Name: mamiferos mamiferos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mamiferos
    ADD CONSTRAINT mamiferos_pkey PRIMARY KEY (mamifero_id);


--
-- TOC entry 2763 (class 2606 OID 25155)
-- Name: novedades novedades_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.novedades
    ADD CONSTRAINT novedades_pkey PRIMARY KEY (novedades_id);


--
-- TOC entry 2761 (class 2606 OID 25142)
-- Name: peces peces_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.peces
    ADD CONSTRAINT peces_pkey PRIMARY KEY (peces_id);


--
-- TOC entry 2759 (class 2606 OID 25129)
-- Name: reptiles reptiles_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reptiles
    ADD CONSTRAINT reptiles_pkey PRIMARY KEY (reptiles_id);


--
-- TOC entry 2749 (class 2606 OID 25064)
-- Name: trabajador trabajador_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trabajador
    ADD CONSTRAINT trabajador_pkey PRIMARY KEY (trabajador_id);


--
-- TOC entry 2765 (class 2606 OID 25078)
-- Name: animales animales_area_fk_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.animales
    ADD CONSTRAINT animales_area_fk_id_fkey FOREIGN KEY (area_fk_id) REFERENCES public.area(area_id);


--
-- TOC entry 2768 (class 2606 OID 25117)
-- Name: aves aves_animal_fk_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.aves
    ADD CONSTRAINT aves_animal_fk_id_fkey FOREIGN KEY (animal_fk_id) REFERENCES public.animales(animal_id);


--
-- TOC entry 2767 (class 2606 OID 25104)
-- Name: insectos insectos_animal_fk_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.insectos
    ADD CONSTRAINT insectos_animal_fk_id_fkey FOREIGN KEY (animal_fk_id) REFERENCES public.animales(animal_id);


--
-- TOC entry 2766 (class 2606 OID 25091)
-- Name: mamiferos mamiferos_animal_fk_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.mamiferos
    ADD CONSTRAINT mamiferos_animal_fk_id_fkey FOREIGN KEY (animal_fk_id) REFERENCES public.animales(animal_id);


--
-- TOC entry 2770 (class 2606 OID 25143)
-- Name: peces peces_animal_fk_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.peces
    ADD CONSTRAINT peces_animal_fk_id_fkey FOREIGN KEY (animal_fk_id) REFERENCES public.animales(animal_id);


--
-- TOC entry 2769 (class 2606 OID 25130)
-- Name: reptiles reptiles_animal_fk_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reptiles
    ADD CONSTRAINT reptiles_animal_fk_id_fkey FOREIGN KEY (animal_fk_id) REFERENCES public.animales(animal_id);


--
-- TOC entry 2764 (class 2606 OID 25065)
-- Name: trabajador trabajador_area_fk_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.trabajador
    ADD CONSTRAINT trabajador_area_fk_id_fkey FOREIGN KEY (area_fk_id) REFERENCES public.area(area_id);


-- Completed on 2021-01-21 22:06:15

--
-- PostgreSQL database dump complete
--

