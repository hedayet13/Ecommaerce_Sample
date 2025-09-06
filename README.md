# Woodmart Clone (Django)

A clean-room, education-focused clone of the *layout and features* of Woodmart's **Marketplace 2** demo, built with Django 5 and PostgreSQL. It includes:
- Home banners, category menu, product grid, product details
- Session cart and simple checkout (no payments)
- Blog, static pages (About/Contact)
- Vendor pages (multi-vendor capable)
- Admin to manage all content

> **Legal**: This project does not copy proprietary theme code or assets. Replace all demo images and text with your own.

## Quickstart (Windows, no Docker)

1. Install Python 3.11+ and PostgreSQL 14+ (ensure `psql` is on PATH).
2. Create DB:
   ```sql
   CREATE DATABASE woodmart_clone;
   CREATE USER postgres WITH PASSWORD 'postgres';  -- or your own user/password
   GRANT ALL PRIVILEGES ON DATABASE woodmart_clone TO postgres;
   ```
3. In PowerShell:
   ```powershell
   cd woodmart_clone
   python -m venv .venv
   .\.venv\Scripts\activate
   pip install -r requirements.txt
   copy .env.example .env
   # edit .env with your DB creds
   python manage.py migrate
   python manage.py loaddata fixtures/demo.json
   python manage.py createsuperuser  # to access /admin
   python manage.py runserver
   ```
4. Visit http://127.0.0.1:8000 and http://127.0.0.1:8000/admin

## Admin-managed content

- **Catalog**: Categories, Products, Images, Variations, Reviews
- **Marketing**: Banners (hero carousel)
- **Blog**: Posts
- **Pages**: CMS-like simple pages
- **Vendors**: Vendor profiles
- **Orders**: View orders placed via checkout
- **Users**: Custom `accounts.User` with vendor flag

## Notes

- Payments, shipping rates, taxes, wishlist/compare, and advanced filters are out of scope in this starter but can be added.
- Styling uses Bootstrap 5 for speed; feel free to swap for Tailwind and custom theme work to better match the reference.
