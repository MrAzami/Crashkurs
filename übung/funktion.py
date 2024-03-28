def gehalt(hour, per_hour):
    if hour >= 7:
        return "error! too much work"
    else:
        einkommen = hour* per_hour
        return einkommen

print (gehalt(7, 3))
