# check when sum(valueA) > sum(valueB)
def differnce():
    taxi_price = 0.5
    auto_price = 200
    auto_price_km = 0.499999999

    if taxi_price <= auto_price_km:
        return f"Taxi wird immer billiger sein oder gleich teuer"
    else:
        return int(auto_price / (taxi_price - auto_price_km))


print(differnce())