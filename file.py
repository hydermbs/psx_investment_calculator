import pandas as pd 
import requests
from bs4 import BeautifulSoup

class PSXInvestmentCalculator:
    def __init__(self, total_investment, num_companies, index_name):
        self.total_investment = total_investment
        self.num_companies = num_companies
        self.index_name = index_name
        self.url = f"https://dps.psx.com.pk/indices/{index_name}"

    def request_data(self):
        response = requests.get(self.url)
        return response.text

    def parse_data(self, response):
        soup = BeautifulSoup(response, "html.parser")
        return soup

    def extract_headers(self, table):
        header_row = table.find("tr")
        header_cells = header_row.find_all("th")
        header_names = [cell.text.strip() for cell in header_cells]
        return header_names

    def extract_table_data(self, table):
        rows = table.find_all("tr")
        data_rows = rows[1:]
        return data_rows

    def extract_table(self, soup):
        table = soup.find("table",{"class":"tbl"})
        header_names = self.extract_headers(table)
        data_rows = self.extract_table_data(table)
        data = []
        for row in data_rows:
            cells = row.find_all("td")
            row_data = [cell.text.strip() for cell in cells]
            data.append(row_data)
        return data, header_names

    def convert_df(self, data, header_names):
        df = pd.DataFrame(data, columns=header_names)
        return df

    def add_sector_names(self, df, df_company):
        df_merged = pd.merge(df, df_company[['symbol', 'sectorName']], left_on='SYMBOL', right_on='symbol', how='left')
        df_merged.drop(columns=['symbol'], inplace=True)
        return df_merged

    def get_top_companies(self, df, qty):
        top_5_companies = df.sort_values(by = "IDX WTG (%)",ascending = False).head(qty)
        return top_5_companies

    def investment_percentage(self, df):
        df["IDX WTG (%)"] = df["IDX WTG (%)"].str.strip('%').astype(float)
        investment_percentage = df["IDX WTG (%)"]*1.5
        return investment_percentage

    def get_total_investment(self, df): 
        total_investment = df["Investment percentage"].sum()
        return total_investment

    def investment_amount(self, df, total_investment):
        investment_amount = df["Normalized_percentage"]/100*total_investment
        return investment_amount

    def read_company_list(self):
        company_df = pd.read_csv("company_list.csv")
        return company_df

    def main(self):
        response = self.request_data()
        soup = self.parse_data(response)
        table_data, header_names = self.extract_table(soup)
        df_companies = self.convert_df(table_data, header_names)
        df_company_list = self.read_company_list()
        df = self.add_sector_names(df_companies, df_company_list)
        top_companies = self.get_top_companies(df, self.num_companies)
        inv_pct = self.investment_percentage(top_companies)
        top_companies["Investment percentage"] = inv_pct
        total_inv = self.get_total_investment(top_companies)
        top_companies["Normalized_percentage"] = (top_companies["Investment percentage"] / total_inv) * 100
        inv_amount = self.investment_amount(top_companies, self.total_investment)
        top_companies["Investment amount"] = inv_amount
        return top_companies

