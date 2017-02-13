/* Create links table */
CREATE TABLE links(
  id INTEGER PRIMARY KEY,
  url TEXT(255) NOT NULL UNIQUE,
  title TEXT(100),
  description TEXT(255),
  media_type TEXT(20),
  short_url TEXT(30),
  created_at NUMERIC NOT NULL,
  updated_at NUMERIC NOT NULL
);

/* Create settings table and fill with defaults */
CREATE TABLE settings(
  id INTEGER PRIMARY KEY,
  listen_clipboard NUMERIC(1) NOT NULL DEFAULT 1,
  start_at_login NUMERIC(1) NOT NULL DEFAULT 0,
  short_all_links NUMERIC(1) NOT NULL DEFAULT 0,
  api_provider TEXT(20) NOT NULL DEFAULT 'google'
);
