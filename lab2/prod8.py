import argparse

parser = argparse.ArgumentParser(description='Calculate P&L for a given period')

parser.add_argument('--per-day', type=float, help='Income/Expense per day')
parser.add_argument('--per-week', type=float, help='Income/Expense per week')
parser.add_argument('--per-month', type=float, help='Income/Expense per month')
parser.add_argument('--per-year', type=float, help='Income/Expense per year')
parser.add_argument('--get-by', choices=['day', 'month', 'year'], default='day', help='Period to calculate P&L (day/month/year)')

args = parser.parse_args()


def calculate_profit_loss(args):
    total_profit_loss = 0

    if args.get_by == 'day':
        if args.per_day:
            total_profit_loss += args.per_day
        if args.per_week:
            total_profit_loss += args.per_week / 7
        if args.per_month:
            total_profit_loss += args.per_month / 30
        if args.per_year:
            total_profit_loss += args.per_year / 360
    elif args.get_by == 'month':
        if args.per_day:
            total_profit_loss += args.per_day * 30
        if args.per_week:
            total_profit_loss += (args.per_week / 7) * 30
        if args.per_month:
            total_profit_loss += args.per_month
        if args.per_year:
            total_profit_loss += args.per_year / 12
    elif args.get_by == 'year':
        if args.per_day:
            total_profit_loss += args.per_day * 360
        if args.per_week:
            total_profit_loss += (args.per_week / 7) * 360
        if args.per_month:
            total_profit_loss += args.per_month * 12
        if args.per_year:
            total_profit_loss += args.per_year

    return int(total_profit_loss)


result = calculate_profit_loss(args)
print("Profit/Loss for the specified period:", result)