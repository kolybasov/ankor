# Ankor

## General

## Core

### Database

#### Tables

* **links**:
  * id (int, primary key)
  * url (text 255)
  * title (text 100)
  * description (text 255)
  * media_type (text 20)
  * short_url (text 30)
  * created_at (numeric)
  * updated_at (numeric)

* **settings:**
  * id (int, primary key)
  * listen_clipboard (numeric 1)
  * start_at_login (numeric 1)
  * short_all_links (numeric 1)
  * api_provider (text 20)

## Client
