import pandas as pd 
import requests
from bs4 import BeautifulSoup

def request_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_data(response):
    soup = BeautifulSoup(response, "html.parser")
    return soup

def extract_headers(table):
    header_row = table.find("tr")
    header_cells = header_row.find_all("th")
    header_names = [cell.text.strip() for cell in header_cells]
    return header_names

def extract_table_data(table):
    rows = table.find_all("tr")
    data_rows = rows[1:]
    return data_rows

def extract_table(soup):
    table = soup.find("table",{"class":"tbl"})
    header_names = extract_headers(table)
    data_rows = extract_table_data(table)
    data = []
    for row in data_rows:
        cells = row.find_all("td")
        row_data = [cell.text.strip() for cell in cells]
        data.append(row_data)
    return data, header_names

def convert_df(data,header_names):
    df = pd.DataFrame(data, columns=header_names)
    return df

def get_top_companies(df, qty):
    top_5_companies = df.sort_values(by = "IDX WTG (%)",ascending = False).head(qty)
    return top_5_companies

def investment_percentage(df):
    df["IDX WTG (%)"] = df["IDX WTG (%)"].str.strip('%').astype(float)
    investment_percentage = df["IDX WTG (%)"]*1.5
    return investment_percentage

def get_total_investment(df):
    total_investment = df["Investment percentage"].sum()
    return total_investment

def investment_amount(df,total_investment):
    investment_amount = df["Normalized_percentage"]/100*total_investment
    return investment_amount

def main(total_investment,num_companies):
    response = request_data("https://dps.psx.com.pk/indices/KSE100")
    soup = parse_data(response)
    table_data,header_names = extract_table(soup)
    df = convert_df(table_data,header_names)
    top_companies = get_top_companies(df,num_companies)
    inv_pct = investment_percentage(top_companies)
    top_companies["Investment percentage"] = inv_pct
    total_inv = get_total_investment(top_companies)
    top_companies["Normalized_percentage"] = (top_companies["Investment percentage"] / total_inv) * 100
    inv_amount = investment_amount(top_companies, total_investment)
    top_companies["Investment amount"] = inv_amount
    return top_companies
