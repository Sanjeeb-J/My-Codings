def main():
    spacecraft = {"name":"James Webb Space Telescope"}
    # You can also use update to add anything
    spacecraft.update({"distance": "0.01", "orbit": "Sun"})
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get("name", "Unknown")}
    Distance: {spacecraft.get("distance", "Unknown")} Au
    Orbit: {spacecraft.get("orbit", "unknown")}

    ==========================
    """

main()