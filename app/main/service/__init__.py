from ..model.currency import Currency

c1 = Currency("EUR", 1.18)
c2 = Currency("USD", 1.0)
c3 = Currency("JPY", 0.0091)
c4 = Currency("GBP", 1.38)
c5 = Currency("CHF", 1.09)
c6 = Currency("AUD", 0.74)
c7 = Currency("CAD", 0.80)
c8 = Currency("NZD", 0.70)

currencies = {
    'base': "USD",
    'rates': {
        'EUR': c1,
        'USD': c2,
        'JPY': c3,
        'GBP': c4,
        'CHF': c5,
        'AUD': c6,
        'CAD': c7,
        'NZD': c8
    },
}