# Event Management System using Python and MySQL

**NOTE:** Use of an `conda` environment is highly advised

## Requirements (Advised)

- Python v3.8+
- MySQL Community Server v8+

## Setup

1. Open `MySQL` console and run the SQL code in `$PROJECTDIR/database/database.sql`
2. Rename `config.json.example` in `$PROJECTDIR/database/` to `config.json` and update your username and password  (update host if needed)
3. `cd` to `$PROJECTDIR` and run:
```bash
conda activate your-environment-name
pip install -r requirements.txt # Alternative: python -m pip install -r requirements.txt
python main.py
```
