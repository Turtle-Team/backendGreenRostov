from fastapi import FastAPI, HTTPException, Query
import pandas as pd
from typing import List, Dict, Any, Optional

app = FastAPI()


def read_excel(file_path: str):
    try:
        df = pd.read_excel(file_path)

        df = df.fillna(0)  # Заменяем NaN на 0
        df = df.replace([float('inf'), -float('inf')], 0)  # Заменяем бесконечные значения на 0

        return df
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading Excel file: {e}")

@app.get("/operations/filter")
def filter_operations(
    date: Optional[int] = Query(None, description="Start date in Unix timestamp"),
    date_to: Optional[int] = Query(None, description="End date in Unix timestamp"),
    user_inn: Optional[str] = None
):
    file_path = "r.xlsx"

    df = pd.read_excel(file_path)

    df['dateTime'] = pd.to_datetime(df['dateTime'], unit='s', errors='coerce')

    if user_inn:
        df = df[df['userInn'] == int(user_inn)]

    if date and not date_to:
        start_date = pd.to_datetime(date, unit='s')
        end_date = start_date + pd.Timedelta(days=1)
        df = df[(df['dateTime'] >= start_date) & (df['dateTime'] < end_date)]

    if date and date_to:
        start_date = pd.to_datetime(date, unit='s')
        end_date = pd.to_datetime(date_to, unit='s')
        df = df[(df['dateTime'] >= start_date) & (df['dateTime'] <= end_date)]

    df = df.replace({float('inf'): None, -float('inf'): None})
    df = df.fillna(value="")

    filtered_operations = df.to_dict(orient="records")

    return {"filtered_operations": filtered_operations}


@app.get("/operations")
def get_operations():
    file_path = "r.xlsx"

    df = read_excel(file_path)

    operations = df.to_dict(orient="records")

    return {"operations": operations}
