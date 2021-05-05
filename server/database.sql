--
-- PostgreSQL database dump
--

-- Dumped from database version 13.2
-- Dumped by pg_dump version 13.2

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
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: spawar2
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO spawar2;

--
-- Name: checks; Type: TABLE; Schema: public; Owner: spawar2
--

CREATE TABLE public.checks (
    id integer NOT NULL,
    course_id integer NOT NULL,
    name character varying(64) NOT NULL,
    language character varying(64) NOT NULL,
    start_date timestamp without time zone NOT NULL,
    end_date timestamp without time zone NOT NULL,
    "interval" integer,
    is_active boolean NOT NULL,
    visibility character varying(10)
);


ALTER TABLE public.checks OWNER TO spawar2;

--
-- Name: checks_id_seq; Type: SEQUENCE; Schema: public; Owner: spawar2
--

CREATE SEQUENCE public.checks_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.checks_id_seq OWNER TO spawar2;

--
-- Name: checks_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: spawar2
--

ALTER SEQUENCE public.checks_id_seq OWNED BY public.checks.id;


--
-- Name: courses; Type: TABLE; Schema: public; Owner: spawar2
--

CREATE TABLE public.courses (
    id integer NOT NULL,
    user_id integer NOT NULL,
    name character varying(64),
    active boolean
);


ALTER TABLE public.courses OWNER TO spawar2;

--
-- Name: courses_id_seq; Type: SEQUENCE; Schema: public; Owner: spawar2
--

CREATE SEQUENCE public.courses_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.courses_id_seq OWNER TO spawar2;

--
-- Name: courses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: spawar2
--

ALTER SEQUENCE public.courses_id_seq OWNED BY public.courses.id;


--
-- Name: paths; Type: TABLE; Schema: public; Owner: spawar2
--

CREATE TABLE public.paths (
    id integer NOT NULL,
    check_id integer NOT NULL,
    path character varying(256) NOT NULL
);


ALTER TABLE public.paths OWNER TO spawar2;

--
-- Name: paths_id_seq; Type: SEQUENCE; Schema: public; Owner: spawar2
--

CREATE SEQUENCE public.paths_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.paths_id_seq OWNER TO spawar2;

--
-- Name: paths_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: spawar2
--

ALTER SEQUENCE public.paths_id_seq OWNED BY public.paths.id;


--
-- Name: reports; Type: TABLE; Schema: public; Owner: spawar2
--

CREATE TABLE public.reports (
    id integer NOT NULL,
    check_id integer NOT NULL,
    check_date timestamp without time zone NOT NULL,
    status boolean NOT NULL,
    report_link character varying(100) NOT NULL
);


ALTER TABLE public.reports OWNER TO spawar2;

--
-- Name: reports_id_seq; Type: SEQUENCE; Schema: public; Owner: spawar2
--

CREATE SEQUENCE public.reports_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.reports_id_seq OWNER TO spawar2;

--
-- Name: reports_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: spawar2
--

ALTER SEQUENCE public.reports_id_seq OWNED BY public.reports.id;


--
-- Name: similarities; Type: TABLE; Schema: public; Owner: spawar2
--

CREATE TABLE public.similarities (
    id integer NOT NULL,
    check_id integer,
    report_id integer,
    repo1 character varying(100) NOT NULL,
    dupl_code1 double precision DEFAULT 0,
    repo2 character varying(100) NOT NULL,
    dupl_code2 double precision DEFAULT 0
);


ALTER TABLE public.similarities OWNER TO spawar2;

--
-- Name: similarities_id_seq; Type: SEQUENCE; Schema: public; Owner: spawar2
--

CREATE SEQUENCE public.similarities_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.similarities_id_seq OWNER TO spawar2;

--
-- Name: similarities_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: spawar2
--

ALTER SEQUENCE public.similarities_id_seq OWNED BY public.similarities.id;


--
-- Name: submissions; Type: TABLE; Schema: public; Owner: spawar2
--

CREATE TABLE public.submissions (
    id integer NOT NULL,
    check_id integer NOT NULL,
    name character varying(64) NOT NULL,
    github_url character varying(256) NOT NULL
);


ALTER TABLE public.submissions OWNER TO spawar2;

--
-- Name: submissions_id_seq; Type: SEQUENCE; Schema: public; Owner: spawar2
--

CREATE SEQUENCE public.submissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.submissions_id_seq OWNER TO spawar2;

--
-- Name: submissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: spawar2
--

ALTER SEQUENCE public.submissions_id_seq OWNED BY public.submissions.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: spawar2
--

CREATE TABLE public.users (
    id integer NOT NULL,
    name character varying(64) NOT NULL,
    email character varying(64) NOT NULL,
    password character varying(128) NOT NULL,
    admin boolean
);


ALTER TABLE public.users OWNER TO spawar2;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: spawar2
--

CREATE SEQUENCE public.users_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO spawar2;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: spawar2
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: checks id; Type: DEFAULT; Schema: public; Owner: spawar2
--

ALTER TABLE ONLY public.checks ALTER COLUMN id SET DEFAULT nextval('public.checks_id_seq'::regclass);


--
-- Name: courses id; Type: DEFAULT; Schema: public; Owner: spawar2
--

ALTER TABLE ONLY public.courses ALTER COLUMN id SET DEFAULT nextval('public.courses_id_seq'::regclass);


--
-- Name: paths id; Type: DEFAULT; Schema: public; Owner: spawar2
--

ALTER TABLE ONLY public.paths ALTER COLUMN id SET DEFAULT nextval('public.paths_id_seq'::regclass);


--
-- Name: reports id; Type: DEFAULT; Schema: public; Owner: spawar2
--

ALTER TABLE ONLY public.reports ALTER COLUMN id SET DEFAULT nextval('public.reports_id_seq'::regclass);


--
-- Name: similarities id; Type: DEFAULT; Schema: public; Owner: spawar2
--

ALTER TABLE ONLY public.similarities ALTER COLUMN id SET DEFAULT nextval('public.similarities_id_seq'::regclass);


--
-- Name: submissions id; Type: DEFAULT; Schema: public; Owner: spawar2
--

ALTER TABLE ONLY public.submissions ALTER COLUMN id SET DEFAULT nextval('public.submissions_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: spawar2
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: spawar2
--

COPY public.alembic_version (version_num) FROM stdin;
61c65121c484
\.


--
-- Data for Name: checks; Type: TABLE DATA; Schema: public; Owner: spawar2
--

COPY public.checks (id, course_id, name, language, start_date, end_date, "interval", is_active, visibility) FROM stdin;
120	11	new2	python	2021-04-09 00:00:00	2021-04-09 00:00:00	1	t	yes
122	11	new4	python	2021-04-27 00:00:00	2021-04-27 00:00:00	1	t	yes
121	11	new3	python	2021-04-23 00:00:00	2021-04-24 00:00:00	1	t	no
119	11	new1	python	2021-04-09 00:00:00	2021-04-09 00:00:00	1	t	no
123	11	Final Assignment	python	2021-05-04 00:00:00	2021-05-04 00:00:00	1	t	yes
\.


--
-- Data for Name: courses; Type: TABLE DATA; Schema: public; Owner: spawar2
--

COPY public.courses (id, user_id, name, active) FROM stdin;
11	1	trial	t
\.


--
-- Data for Name: paths; Type: TABLE DATA; Schema: public; Owner: spawar2
--

COPY public.paths (id, check_id, path) FROM stdin;
108	119	/app/
109	120	/app/
110	121	/app/
111	122	/app/
112	123	/app/
\.


--
-- Data for Name: reports; Type: TABLE DATA; Schema: public; Owner: spawar2
--

COPY public.reports (id, check_id, check_date, status, report_link) FROM stdin;
112	119	2021-04-09 00:25:34.316154	t	http://moss.stanford.edu/results/8/76547270614
113	120	2021-04-09 00:28:54.425787	t	http://moss.stanford.edu/results/1/8143114376320
114	120	2021-04-23 22:18:12.861636	t	http://moss.stanford.edu/results/4/5370952543775
115	120	2021-04-27 16:18:22.800706	t	http://moss.stanford.edu/results/0/4889374711524
116	120	2021-05-04 16:18:25.869716	t	http://moss.stanford.edu/results/3/9860691389507
\.


--
-- Data for Name: similarities; Type: TABLE DATA; Schema: public; Owner: spawar2
--

COPY public.similarities (id, check_id, report_id, repo1, dupl_code1, repo2, dupl_code2) FROM stdin;
1	120	113	t6	17	t3	19
2	120	113	t5	30	t3	17
3	120	113	t5	24	t6	11
4	120	114	t6	17	t3	19
5	120	114	t5	30	t3	17
6	120	114	t5	24	t6	11
7	120	115	t6	74	t3	74
8	120	115	t5	24	t3	11
9	120	115	t5	24	t6	11
10	120	116	t6	19	t3	17
11	120	116	t5	30	t6	17
12	120	116	t5	24	t3	11
\.


--
-- Data for Name: submissions; Type: TABLE DATA; Schema: public; Owner: spawar2
--

COPY public.submissions (id, check_id, name, github_url) FROM stdin;
353	119	t5	https://spawar2@github.ncsu.edu/nsundar/divided-airlines-project
354	119	t6	https://spawar2@github.ncsu.edu/pmehta3/AirRails_CSC517
355	119	t3	https://spawar2@github.ncsu.edu/jwhostet/RubyAirlines
356	120	t5	https://spawar2@github.ncsu.edu/nsundar/divided-airlines-project
357	120	t6	https://spawar2@github.ncsu.edu/pmehta3/AirRails_CSC517
358	120	t3	https://spawar2@github.ncsu.edu/jwhostet/RubyAirlines
359	121	t5	https://spawar2@github.ncsu.edu/nsundar/divided-airlines-project
360	121	t6	https://spawar2@github.ncsu.edu/pmehta3/AirRails_CSC517
361	121	t3	https://spawar2@github.ncsu.edu/jwhostet/RubyAirlines
362	122	t5	https://spawar2@github.ncsu.edu/nsundar/divided-airlines-project
363	122	t6	https://spawar2@github.ncsu.edu/pmehta3/AirRails_CSC517
364	122	t3	https://spawar2@github.ncsu.edu/pmehta3/AirRails_CSC517
365	123	t5	https://spawar2@github.ncsu.edu/nsundar/divided-airlines-project
366	123	t6	https://spawar2@github.ncsu.edu/jwhostet/RubyAirlines
367	123	t3	https://spawar2@github.ncsu.edu/pmehta3/AirRails_CSC517
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: spawar2
--

COPY public.users (id, name, email, password, admin) FROM stdin;
1	admin	admin@gmail.com	password	t
\.


--
-- Name: checks_id_seq; Type: SEQUENCE SET; Schema: public; Owner: spawar2
--

SELECT pg_catalog.setval('public.checks_id_seq', 123, true);


--
-- Name: courses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: spawar2
--

SELECT pg_catalog.setval('public.courses_id_seq', 11, true);


--
-- Name: paths_id_seq; Type: SEQUENCE SET; Schema: public; Owner: spawar2
--

SELECT pg_catalog.setval('public.paths_id_seq', 112, true);


--
-- Name: reports_id_seq; Type: SEQUENCE SET; Schema: public; Owner: spawar2
--

SELECT pg_catalog.setval('public.reports_id_seq', 116, true);


--
-- Name: similarities_id_seq; Type: SEQUENCE SET; Schema: public; Owner: spawar2
--

SELECT pg_catalog.setval('public.similarities_id_seq', 12, true);


--
-- Name: submissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: spawar2
--

SELECT pg_catalog.setval('public.submissions_id_seq', 367, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: spawar2
--

SELECT pg_catalog.setval('public.users_id_seq', 1, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: spawar2
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: checks checks_pkey; Type: CONSTRAINT; Schema: public; Owner: spawar2
--

ALTER TABLE ONLY public.checks
    ADD CONSTRAINT checks_pkey PRIMARY KEY (id);


--
-- Name: courses courses_pkey; Type: CONSTRAINT; Schema: public; Owner: spawar2
--

ALTER TABLE ONLY public.courses
    ADD CONSTRAINT courses_pkey PRIMARY KEY (id);


--
-- Name: paths paths_pkey; Type: CONSTRAINT; Schema: public; Owner: spawar2
--

ALTER TABLE ONLY public.paths
    ADD CONSTRAINT paths_pkey PRIMARY KEY (id);


--
-- Name: reports reports_pkey; Type: CONSTRAINT; Schema: public; Owner: spawar2
--

ALTER TABLE ONLY public.reports
    ADD CONSTRAINT reports_pkey PRIMARY KEY (id);


--
-- Name: similarities similarities_pkey; Type: CONSTRAINT; Schema: public; Owner: spawar2
--

ALTER TABLE ONLY public.similarities
    ADD CONSTRAINT similarities_pkey PRIMARY KEY (id);


--
-- Name: submissions submissions_pkey; Type: CONSTRAINT; Schema: public; Owner: spawar2
--

ALTER TABLE ONLY public.submissions
    ADD CONSTRAINT submissions_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: spawar2
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: ix_courses_user_id; Type: INDEX; Schema: public; Owner: spawar2
--

CREATE INDEX ix_courses_user_id ON public.courses USING btree (user_id);


--
-- Name: ix_users_email; Type: INDEX; Schema: public; Owner: spawar2
--

CREATE UNIQUE INDEX ix_users_email ON public.users USING btree (email);


--
-- Name: checks checks_course_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: spawar2
--

ALTER TABLE ONLY public.checks
    ADD CONSTRAINT checks_course_id_fkey FOREIGN KEY (course_id) REFERENCES public.courses(id) ON DELETE CASCADE;


--
-- Name: courses courses_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: spawar2
--

ALTER TABLE ONLY public.courses
    ADD CONSTRAINT courses_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- Name: similarities fk_check_id; Type: FK CONSTRAINT; Schema: public; Owner: spawar2
--

ALTER TABLE ONLY public.similarities
    ADD CONSTRAINT fk_check_id FOREIGN KEY (check_id) REFERENCES public.checks(id) ON DELETE CASCADE;


--
-- Name: similarities fk_report_id; Type: FK CONSTRAINT; Schema: public; Owner: spawar2
--

ALTER TABLE ONLY public.similarities
    ADD CONSTRAINT fk_report_id FOREIGN KEY (report_id) REFERENCES public.reports(id) ON DELETE CASCADE;


--
-- Name: paths paths_check_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: spawar2
--

ALTER TABLE ONLY public.paths
    ADD CONSTRAINT paths_check_id_fkey FOREIGN KEY (check_id) REFERENCES public.checks(id) ON DELETE CASCADE;


--
-- Name: reports reports_check_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: spawar2
--

ALTER TABLE ONLY public.reports
    ADD CONSTRAINT reports_check_id_fkey FOREIGN KEY (check_id) REFERENCES public.checks(id) ON DELETE CASCADE;


--
-- Name: submissions submissions_check_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: spawar2
--

ALTER TABLE ONLY public.submissions
    ADD CONSTRAINT submissions_check_id_fkey FOREIGN KEY (check_id) REFERENCES public.checks(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

