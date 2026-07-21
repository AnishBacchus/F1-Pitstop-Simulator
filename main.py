def lap_time(base_time, degradation_rate, tire_age):
    return base_time + (degradation_rate * tire_age)


print(lap_time(90, 0.3, 5))