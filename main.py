# Ignore warnings
import warnings
warnings.filterwarnings('ignore')

import os
from crew import FinancialAnalystCrew

os.environ['OPENAI_API_KEY'] = "REPLACE_THIS_WITH_YOUR_OPENAI_API_KEY"
os.environ['SEC_API_API_KEY'] = "REPLACE_THIS_WITH_YOUR_SEC_API_API_KEY"

def run():
    inputs = {
        'company_stock_symbol': 'MSFT',
    }
    FinancialAnalystCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
