--
-- PostgreSQL database dump
--

-- Dumped from database version 9.5.23
-- Dumped by pg_dump version 9.5.23

SET statement_timeout = 0;
SET lock_timeout = 0;
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
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO postgres;

--
-- Name: checks; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.checks (
    id integer NOT NULL,
    course_id integer NOT NULL,
    name character varying(64) NOT NULL,
    language character varying(64) NOT NULL,
    start_date timestamp without time zone NOT NULL,
    end_date timestamp without time zone NOT NULL,
    "interval" integer,
    is_active boolean NOT NULL
);


ALTER TABLE public.checks OWNER TO postgres;

--
-- Name: checks_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.checks_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.checks_id_seq OWNER TO postgres;

--
-- Name: checks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.checks_id_seq OWNED BY public.checks.id;


--
-- Name: courses; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.courses (
    id integer NOT NULL,
    user_id integer NOT NULL,
    name character varying(64),
    active boolean
);


ALTER TABLE public.courses OWNER TO postgres;

--
-- Name: courses_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.courses_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.courses_id_seq OWNER TO postgres;

--
-- Name: courses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.courses_id_seq OWNED BY public.courses.id;


--
-- Name: paths; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.paths (
    id integer NOT NULL,
    check_id integer NOT NULL,
    path character varying(256) NOT NULL
);


ALTER TABLE public.paths OWNER TO postgres;

--
-- Name: paths_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.paths_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.paths_id_seq OWNER TO postgres;

--
-- Name: paths_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.paths_id_seq OWNED BY public.paths.id;


--
-- Name: reports; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.reports (
    id integer NOT NULL,
    check_id integer NOT NULL,
    check_date timestamp without time zone NOT NULL,
    status boolean NOT NULL,
    report_link character varying(100) NOT NULL
);


ALTER TABLE public.reports OWNER TO postgres;

--
-- Name: reports_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.reports_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reports_id_seq OWNER TO postgres;

--
-- Name: reports_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.reports_id_seq OWNED BY public.reports.id;


--
-- Name: submissions; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.submissions (
    id integer NOT NULL,
    check_id integer NOT NULL,
    name character varying(64) NOT NULL,
    github_url character varying(64) NOT NULL
);


ALTER TABLE public.submissions OWNER TO postgres;

--
-- Name: submissions_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.submissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.submissions_id_seq OWNER TO postgres;

--
-- Name: submissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.submissions_id_seq OWNED BY public.submissions.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying(64) NOT NULL,
    email character varying(64) NOT NULL,
    password character varying(128) NOT NULL,
    admin boolean
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO postgres;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.checks ALTER COLUMN id SET DEFAULT nextval('public.checks_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses ALTER COLUMN id SET DEFAULT nextval('public.courses_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paths ALTER COLUMN id SET DEFAULT nextval('public.paths_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reports ALTER COLUMN id SET DEFAULT nextval('public.reports_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.submissions ALTER COLUMN id SET DEFAULT nextval('public.submissions_id_seq'::regclass);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.alembic_version (version_num) FROM stdin;
61c65121c484
\.


--
-- Data for Name: checks; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.checks (id, course_id, name, language, start_date, end_date, "interval", is_active) FROM stdin;
1	1	Test1	python	2020-11-01 15:48:43.784797	2020-11-01 15:48:43.784797	1	t
2	1	Test2	java	2020-11-30 00:00:00	2020-12-02 00:00:00	2	t
3	1	test3	verilog	2020-11-30 00:00:00	2020-12-01 00:00:00	2	t
4	1	test4	scheme	2020-12-01 00:00:00	2020-12-03 00:00:00	2	t
5	2	Check1	python	2020-11-30 00:00:00	2020-12-09 00:00:00	2	t
6	2	Check2	python	2020-11-30 00:00:00	2020-12-09 00:00:00	2	t
7	2	check3	python	2020-11-30 00:00:00	2020-12-02 00:00:00	2	t
8	2	check4	python	2020-11-30 00:00:00	2020-12-02 00:00:00	2	t
9	2	check5	fortran	2020-11-30 00:00:00	2020-12-02 00:00:00	2	t
10	1	test5	pascal	2020-11-30 00:00:00	2020-12-02 00:00:00	2	t
11	2	Test_check	perl	2021-01-21 00:00:00	2021-01-23 00:00:00	1	t
12	1	test10	python	2021-02-19 00:00:00	2021-02-23 00:00:00	1	t
13	1	asdasfs	python	2021-02-19 00:00:00	2021-02-26 00:00:00	1	t
\.


--
-- Name: checks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.checks_id_seq', 13, true);


--
-- Data for Name: courses; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.courses (id, user_id, name, active) FROM stdin;
1	1	Test1	t
2	1	Test Course 2	t
3	1	test3	t
4	1	test 4	t
5	1	test5	t
6	1	sdgszdvdszg	t
\.


--
-- Name: courses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.courses_id_seq', 6, true);


--
-- Data for Name: paths; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.paths (id, check_id, path) FROM stdin;
2	1	/app/models/
4	1	/app/controllers/
\.


--
-- Name: paths_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.paths_id_seq', 5, true);


--
-- Data for Name: reports; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.reports (id, check_id, check_date, status, report_link) FROM stdin;
1	1	2020-11-29 22:21:17.57352	t	http://moss.stanford.edu/results/6/5259761252413
2	1	2020-11-30 20:22:44.88767	t	http://moss.stanford.edu/results/6/4754717332284
3	11	2021-01-21 21:00:00.016102	t	Error: No files uploaded to compare.
4	1	2021-02-19 19:48:50.467134	t	http://moss.stanford.edu/results/9/4439209740111
\.


--
-- Name: reports_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.reports_id_seq', 4, true);


--
-- Data for Name: submissions; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.submissions (id, check_id, name, github_url) FROM stdin;
3	1	sahil	https://github.com/sppapalkar/store-management
4	1	ahrodia	https://github.com/SujalAhrodia/SMS
5	2	sahil	https://github.com/sppapalkar/store-management
6	2	ahrodia	https://github.com/SujalAhrodia/SMS
7	3	sahil	https://github.com/sppapalkar/store-management
8	3	ahrodia	https://github.com/SujalAhrodia/SMS
9	4	sahil	https://github.com/sppapalkar/store-management
10	4	ahrodia	https://github.com/SujalAhrodia/SMS
11	5	sahil	https://github.com/sppapalkar/store-management
12	5	ahrodia	https://github.com/SujalAhrodia/SMS
13	6	sahil	https://github.com/sppapalkar/store-management
14	6	ahrodia	https://github.com/SujalAhrodia/SMS
15	7	sahil	https://github.com/sppapalkar/store-management
16	7	ahrodia	https://github.com/SujalAhrodia/SMS
17	8	sahil	https://github.com/sppapalkar/store-management
18	8	ahrodia	https://github.com/SujalAhrodia/SMS
19	9	sahil	https://github.com/sppapalkar/store-management
20	9	ahrodia	https://github.com/SujalAhrodia/SMS
21	10	sahil	https://github.com/sppapalkar/store-management
22	10	ahrodia	https://github.com/SujalAhrodia/SMS
23	11	sahil	https://github.com/sppapalkar/store-management
24	11	ahrodia	https://github.com/SujalAhrodia/SMS
25	12	sahil	https://github.com/sppapalkar/store-management
26	12	ahrodia	https://github.com/SujalAhrodia/SMS
27	13	sahil	https://github.com/sppapalkar/store-management
28	13	ahrodia	https://github.com/SujalAhrodia/SMS
\.


--
-- Name: submissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.submissions_id_seq', 28, true);


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (id, name, email, password, admin) FROM stdin;
1	admin	admin@gmail.com	password	t
\.


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.users_id_seq', 1, true);


--
-- Name: alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: checks_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.checks
    ADD CONSTRAINT checks_pkey PRIMARY KEY (id);


--
-- Name: courses_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses
    ADD CONSTRAINT courses_pkey PRIMARY KEY (id);


--
-- Name: paths_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paths
    ADD CONSTRAINT paths_pkey PRIMARY KEY (id);


--
-- Name: reports_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reports
    ADD CONSTRAINT reports_pkey PRIMARY KEY (id);


--
-- Name: submissions_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.submissions
    ADD CONSTRAINT submissions_pkey PRIMARY KEY (id);


--
-- Name: users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: ix_courses_user_id; Type: INDEX; Schema: public; Owner: postgres
--

CREATE INDEX ix_courses_user_id ON public.courses USING btree (user_id);


--
-- Name: ix_users_email; Type: INDEX; Schema: public; Owner: postgres
--

CREATE UNIQUE INDEX ix_users_email ON public.users USING btree (email);


--
-- Name: checks_course_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.checks
    ADD CONSTRAINT checks_course_id_fkey FOREIGN KEY (course_id) REFERENCES public.courses(id) ON DELETE CASCADE;


--
-- Name: courses_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.courses
    ADD CONSTRAINT courses_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- Name: paths_check_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.paths
    ADD CONSTRAINT paths_check_id_fkey FOREIGN KEY (check_id) REFERENCES public.checks(id) ON DELETE CASCADE;


--
-- Name: reports_check_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.reports
    ADD CONSTRAINT reports_check_id_fkey FOREIGN KEY (check_id) REFERENCES public.checks(id) ON DELETE CASCADE;


--
-- Name: submissions_check_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.submissions
    ADD CONSTRAINT submissions_check_id_fkey FOREIGN KEY (check_id) REFERENCES public.checks(id) ON DELETE CASCADE;


--
-- Name: SCHEMA public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

