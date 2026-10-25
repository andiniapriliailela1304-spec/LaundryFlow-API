
# LaundryFlow API

Backend pengelolaan pesanan laundry menggunakan Python dan FastAPI.

## Fitur

- Membuat pesanan laundry.
- Melihat semua pesanan.
- Melihat detail pesanan.
- Memperbarui status pesanan.
- Menghapus pesanan.
- Menghitung biaya laundry otomatis.
- Validasi request menggunakan Pydantic.
- Unit test menggunakan Pytest.

## Teknologi

- Python 3.13
- FastAPI
- Pydantic
- Pytest
- HTTPX
- GitHub Actions

## Instalasi

Buat virtual environment:

```bash
python -m venv .venv
```

Aktifkan pada Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Instal dependensi:

```bash
pip install -r requirements.txt
```

## Menjalankan aplikasi

```bash
uvicorn app.main:app --reload
```

Buka dokumentasi API:

http://127.0.0.1:8000/docs

## Daftar Endpoint

| Method | Endpoint | Fungsi |
|---|---|---|
| GET | / | Memeriksa status API |
| POST | /api/orders | Membuat pesanan |
| GET | /api/orders | Melihat semua pesanan |
| GET | /api/orders/{order_id} | Melihat detail pesanan |
| PATCH | /api/orders/{order_id}/status | Memperbarui status |
| DELETE | /api/orders/{order_id} | Menghapus pesanan |

## Jenis layanan

- Regular: Rp7.000/kg
- Express: Rp12.000/kg

## Status pesanan

pending, washing, drying, ironing, ready, completed.

## Menjalankan unit test

```bash
python -m pytest -v
```

## Penyimpanan data

Versi awal menggunakan penyimpanan dalam memori.
Data akan hilang ketika aplikasi dimulai ulang.

## Struktur arsitektur

- API: menerima dan memproses request HTTP.
- Schemas: memvalidasi contract request dan response.
- Services: menjalankan aturan bisnis.
- Repositories: mengelola penyimpanan data.
- Models: mendefinisikan struktur data pesanan.
- Core: menyimpan konfigurasi aplikasi.
- Tests: menguji perilaku aplikasi.
