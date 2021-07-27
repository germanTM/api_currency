from ...error_handler import InvalidExchangeData

from . import currencies

accummulated_fee = 0

fee_amount = 0.01

def exchange_info(data):
    base_currency = data["from_currency"]
    quote_currency = data["to_currency"]
    number_to_convert = data["evaluate_amount"]
    base_currency_object = currencies['rates'][base_currency] if base_currency in currencies['rates'] else None
    quote_currency_object = currencies['rates'][quote_currency] if quote_currency in currencies['rates'] else None
    if base_currency_object and quote_currency_object:
        if number_to_convert >= 0:
            evaluation = calculate_exchange_rate(base_currency_object, quote_currency_object, number_to_convert)
            return evaluation
        else:
            raise InvalidExchangeData("The converting value must me greater or equal than cero.", 400)
    else:
        raise InvalidExchangeData("Wrong values for the base and quote currencies.", 400)

"""Validate if the current credit of the currency is enough for the transaction and if so, make the adjustments"""
def make_transaction(data):
    global accummulated_fee
    base_currency = data["from_currency"]
    quote_currency = data["to_currency"]
    exchange_amount = data["exchange_amount"]
    if exchange_amount > 0:
        base_currency_object = currencies['rates'][base_currency] if base_currency in currencies['rates'] else None
        quote_currency_object = currencies['rates'][quote_currency] if quote_currency in currencies['rates'] else None
        if base_currency_object and quote_currency_object:
            evaluation = calculate_exchange_rate(base_currency_object, quote_currency_object, exchange_amount)
            if exchange_amount <= base_currency_object.credit:
                base_currency_object.credit -= exchange_amount
                quote_currency_object.credit += evaluation["exchange_rate"]
                accummulated_fee += round(evaluation['fee_amount'], 4)
                res = {
                    "exchange_rate": evaluation["exchange_rate"],
                    "fee_amount": evaluation["fee_amount"],
                    "accumulated_fee_over_base": accummulated_fee
                }
                return res, 201
            else:
                raise InvalidExchangeData("There are no enough credits of the requested currency to make the transaction.", 400)
        else:
                raise InvalidExchangeData("Wrong values for the base and quote currencies.", 400)
    else:
        raise InvalidExchangeData("Exchange amount must be greater than 0.", 400)

"""Calculate the exchange rate and fee amount"""
def calculate_exchange_rate(base_currency_object, quote_currency_object, number_to_convert):
    grand_price_of_currency = base_currency_object.exchange * number_to_convert
    total_fee = round(grand_price_of_currency * fee_amount, 4)
    base_currency_with_fee = grand_price_of_currency - total_fee
    exchange_rate = round(base_currency_with_fee /quote_currency_object.exchange, 4)
    return {
        "exchange_rate":exchange_rate, 
        "fee_amount": total_fee
    }