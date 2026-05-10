def show_dict(data):
    print(f"{'key':<6} {'value':<8} {'item':<6}")
    for key, value in data.items():
        print(f"{key:<6} {value:<8} {key:<6}")

dict_manual = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
show_dict(dict_manual)
