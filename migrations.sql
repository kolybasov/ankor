/* Create links table */
CREATE TABLE links(
  id INTEGER PRIMARY KEY,
  url TEXT(255) NOT NULL UNIQUE,
  title TEXT(100),
  description TEXT(255),
  media_type TEXT(20),
  short_url TEXT(30)
);

/* Create settings table and fill with defaults */
CREATE TABLE settings(
  id INTEGER PRIMARY KEY,
  short_all_links NUMERIC(1) NOT NULL DEFAULT 0,
  api_provider TEXT(20) NOT NULL DEFAULT google
);
