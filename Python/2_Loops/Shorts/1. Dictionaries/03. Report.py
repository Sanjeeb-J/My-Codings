def main():
    spacecraft = {"name":"James Webb Space Telescope"}
    print(create_report(spacecraft))

# You can use get
# If there is the distance value in the table it will show, other wise it will show unknown
def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} Au

    ==========================
    """

main()