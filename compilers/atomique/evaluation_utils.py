def latex_format(value):
    my_str = "%.2e" % value
    my_str = my_str.split("e")
    sign = my_str[1][0]
    my_str[1] = my_str[1][1:]
    my_str[1] = my_str[1].lstrip("0")
    if sign == "+":
        return "$" + my_str[0] + "\\times10^{" + my_str[1] + "}$"
    else:
        return "$" + my_str[0] + "\\times10^{" + sign + my_str[1] + "}$"


def dict_average(dicts):
    result = {}
    for key in dicts[0]:
        if isinstance(dicts[0][key], dict):
            result[key] = dict_average([d[key] for d in dicts])
        else:
            result[key] = sum([d[key] for d in dicts]) / len(dicts)
    return result


def report_table1(my_dict, backend_config):
    print_latex(my_dict, 1, backend_config)


def report_table2(my_dict, backend_config):
    print_latex(my_dict, 2, backend_config)


def report_table3(my_dict, backend_config):
    print_latex(my_dict, 3, backend_config)


def report_table4(my_dict, backend_config):
    print_latex(my_dict, 4, backend_config)


def is_int(value):
    if value - int(value) == 0:
        return f"{int(value):d}"
    else:
        return f"{value:.1f}"


def print_latex(res, table_id, backend_config=None, precision="finite"):
    fid = res["fidelity"]
    time = res["time"]
    if precision == "finite":
        if table_id == 1:
            print(
                f"  {res['compilation time']:.2f}  & {is_int(res['1Q gate count'])}  &  {is_int(res['2Q gate count'])}  & {is_int(res['depth'])} &  {fid['total_fidelity']:.3f}&{time['total_time']/backend_config['T1']:.4f} "
            )
        elif table_id == 2:
            print(
                f"  {res['compilation time']:.2f}  & {is_int(res['1Q gate count'])}  &  {is_int(res['2Q gate count'])}  & {is_int(res['depth'])} &  {fid['total_fidelity']:.3f}&{time['total_time']/backend_config['T1']:.4f} "
            )
        elif table_id == 3:
            print(
                f"  {res['compilation time']:.2f}  & {is_int(res['depth'])} &  {fid['total_fidelity']:.3f}  &  {time['total_time']*1000:.2f} & {is_int(res['1Q gate count'])}  &  {is_int(res['2Q gate count'])}  &  {is_int(res['move count'])} &  {res['distance']*1000:.2f}  &  {is_int(res['transfer count'])}"
            )
        elif table_id == 4:
            print(
                f"  {fid['1q gate']:.3f}  &  {fid['2q gate']:.3f}  &  {fid['movement']:.3f}  &  {fid['transfer']:.3f}  &  {fid['decoherence']:.3f}  &  {time['1q gate']*1000:.2f}  &  {time['2q gate']*1000:.2f}  &  {time['movement']*1000:.2f}  &  {time['transfer']*1000:.2f}"
            )
    elif precision == "infinite":
        if table_id == 1:
            print(
                f"  {res['compilation time']}  & {is_int(res['1Q gate count'])}  &  {is_int(res['2Q gate count'])}  & {is_int(res['depth'])} &  {fid['total_fidelity']}&{time['total_time']/backend_config['T1']} "
            )
        elif table_id == 2:
            print(
                f"  {res['compilation time']}  & {is_int(res['1Q gate count'])}  &  {is_int(res['2Q gate count'])}  & {is_int(res['depth'])} &  {fid['total_fidelity']}&{time['total_time']/backend_config['T1']} "
            )
        elif table_id == 3:
            print(
                f"  {res['compilation time']}  & {is_int(res['depth'])} &  {fid['total_fidelity']}  &  {time['total_time']*1000} & {is_int(res['1Q gate count'])}  &  {is_int(res['2Q gate count'])}  &  {is_int(res['move count'])} &  {res['distance']*1000}  &  {is_int(res['transfer count'])}"
            )
        elif table_id == 4:
            print(
                f"  {fid['1q gate']}  &  {fid['2q gate']}  &  {fid['movement']}  &  {fid['transfer']}  &  {fid['decoherence']}  &  {time['1q gate']*1000}  &  {time['2q gate']*1000}  &  {time['movement']*1000}  &  {time['transfer']*1000}"
            )
