from datetime import datetime
from dateutil import parser


format_wikicpf = "%b %d, %Y"
format_conf_date = "%B %d, %Y"
datetime_format = "%Y-%m-%d %H:%M"  # output format
date_format = "%Y-%m-%d"  # output format


def get_datetime(datetime_string: str):
    date = None
    for format in ["%y/%d/%m %h:%m", "%m/%d/%Y %H:%M", "%m/%d/%Y"]:
        try:
            date = datetime.strptime(datetime_string.strip(), format)
            break
        except Exception as e:
            # print(f"{e}          [for {format}]")
            pass
    if date is None:
        try:
            date = parser.parse(datetime_string)
        except Exception as e:
            pass
    return date


def datetime_to_string(dt, format):
    return dt.strftime(format).lstrip("0").replace(" 0", " ").replace("/0", "/")


def get_date_format_from_start_and_end(start: datetime, end: datetime):
    date = (
        f"{datetime_to_string(start, '%B %d')} - {datetime_to_string(end, '%d, %Y')}"
        if start.month == end.month
        else f"{datetime_to_string(start, '%B %d')} - {datetime_to_string(end, '%B %d, %Y')}"
    )
    return date


def parse_date_range(date_range_str):
    if "-" in date_range_str:
        # Split the string into start and end date parts
        start_date_str, end_date_str = date_range_str.split("-")
        # Extract the year from the end date string
        year = int(end_date_str.split(",")[-1])
        # Use dateutil's parser to parse the start date string
        start_date = parser.parse(start_date_str + ", " + str(year))
        if end_date_str.split(",")[0].strip().isnumeric():  # if it doesn't contain a month
            # Extract the month from the start date string
            month = start_date.strftime("%B")
            end_date_str = month + " " + end_date_str
        # Use dateutil's parser to parse the end date string
        end_date = parser.parse(end_date_str)
    else:
        if date_range_str != "":
            start_date = parser.parse(date_range_str)
            end_date = start_date
        else:
            start_date, end_date = None, None
    return start_date, end_date
