"""Practice examples for Python's `re` module on a small block of conference data."""
import re

CONF = """
Conference1
Topic: Object Oriented Programming
Date: 09/20/2022
Location: USA
Web: conf.usa/09/2022
Cost: $1200
Conference2
Topic:    Python3
Date: 01/31/2022
Location: France
Web: conf.france/01/2022
Cost: $6
Conference3
Topic: Data Science
Date:        07/09/2022
Location: UK
Web: conf.org
Cost: $900
Conference4
Topic: Web Development
Date: 09/29/2022
Location: Canada
Web: conf.ca
Cost: $1100
Conference5
Topic: Python for Beginners
Date: 05/09/2022
Location: Turkey
Web: confr.com/03/2022
Cost: $900000
"""


def topics(text):
    return re.findall(r"Topic:\s*(.+)", text)


def dates(text):
    return re.findall(r"Date:\s*(\d\d/\d\d/\d\d\d\d)", text)


def date_months(text):
    return re.findall(r"Date:\s*(\d\d)/\d\d/\d\d\d\d", text)


def web_addresses_2022(text):
    return re.findall(r"Web:\s*(conf\.\w+/\d\d/2022)", text)


def topics_in_september(text):
    return re.findall(r"Topic:\s*(.+)\sDate:\s*09/\d{2}/\d{4}", text)


def replace_cost(text, new_cost="$555"):
    # only matches costs with 2-4 digits ($6 and $900000 are intentionally left alone)
    return re.sub(r"Cost:\s*\$\d{2,4}\s", f"Cost:{new_cost}\n", text)


if __name__ == "__main__":
    print("Topics:", topics(CONF))
    print("Dates:", dates(CONF))
    print("Months:", date_months(CONF))
    print("Web (2022):", web_addresses_2022(CONF))
    print("September topics:", topics_in_september(CONF))
    print(replace_cost(CONF))
