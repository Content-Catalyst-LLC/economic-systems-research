PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS domains (
    domain_key TEXT PRIMARY KEY,
    domain_name TEXT NOT NULL,
    description TEXT,
    priority INTEGER DEFAULT 3
);

CREATE TABLE IF NOT EXISTS articles (
    slug TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    status TEXT NOT NULL CHECK (status IN ('published','planned','drafting','archived')),
    domain_key TEXT NOT NULL,
    priority INTEGER DEFAULT 3,
    source_focus TEXT,
    FOREIGN KEY (domain_key) REFERENCES domains(domain_key)
);

CREATE TABLE IF NOT EXISTS concepts (
    concept_key TEXT PRIMARY KEY,
    concept_name TEXT NOT NULL,
    concept_family TEXT,
    definition_note TEXT
);

CREATE TABLE IF NOT EXISTS traditions (
    tradition_key TEXT PRIMARY KEY,
    tradition_name TEXT NOT NULL,
    core_focus TEXT,
    priority INTEGER DEFAULT 3
);

CREATE TABLE IF NOT EXISTS indicators (
    indicator_key TEXT PRIMARY KEY,
    indicator_name TEXT NOT NULL,
    indicator_family TEXT,
    measurement_note TEXT,
    warning TEXT
);

CREATE TABLE IF NOT EXISTS sources (
    source_key TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    institution_or_author TEXT,
    year TEXT,
    source_type TEXT,
    url TEXT
);
