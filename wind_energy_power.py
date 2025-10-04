def is_positive_number(s):
    """
    function checking if variants positive float
    """
    # if variant is positive float > true; else F
    try:
        if float(s) > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def input_validation(ws,p_rated,ws_cin,ws_rated,ws_cout,mode="linear"):
    """
    function for checking input data format
    """

    # variant counting the correct numbers
    chk_count = 0

    # check each variants
    if is_positive_number(ws):
        chk_count += 1
    else:
        printf(f"Wind speed value: {ws} is invalid format.\n")
    
    if is_positive_number(p_rated):
        chk_count += 1
    else:
        printf(f"Rated power value: {p_rated} is invalid format.\n")
    
    if is_positive_number(ws_cin):
        chk_count += 1
    else:
        printf(f"Cut-in wind speed value: {ws_cin} is invalid format.\n")
    
    if is_positive_number(ws_rated):
        chk_count += 1
    else:
        printf(f"Rated wind speed value: {ws_rated} is invalid format.\n")
    
    if is_positive_number(ws_cout):
        chk_count += 1
    else:
        printf(f"Cut-out wind speed value: {ws_cout} is invalid format.\n")
    
    if mode == "linear" or mode == "l" or mode == "L" or mode == "cubic" or mode == "c" or mode == "C":
        chk_count += 1
    else:
        printf(f"Interpolation option:{mode} is invalid format.\n")

    # chk_count must be as same as the input counts (.__code__.co_argcount for check parameters counts)
    if chk_count == input_validation.__code__.co_argcount:
        return True
    else:
        return False

def P_linear_mode(ws,p_rated,ws_cin,ws_rated,ws_cout):
    # linear mode power output equation
    return ( ws - ws_cin / ws_rated - ws_cin ) * p_rated

def P_cubic_mode(ws,p_rated,ws_cin,ws_rated,ws_cout):
    # cubic mode power output equation
    return ( pow(ws,3) / pow(ws_rated,3) ) * p_rated

def Power_Output(ws,p_rated,ws_cin,ws_rated,ws_cout,mode="linear"):
    """
    Power Output main function
    """
    #detect the mode first; then if ws less than ws_rated output =0; greater >> output = p_rated; within >> call mode_output function
    if mode == "linear" or mode == "l" or mode == "L":
        if ws < ws_cin:
            return 0
        elif ws >=ws_rated:
            return p_rated
        else:
            return P_linear_mode(ws,p_rated,ws_cin,ws_rated,ws_cout)
    elif mode == "cubic" or mode == "c" or mode == "C":
        if ws < ws_cin:
            return 0
        elif ws >=ws_rated:
            return p_rated
        else:
            return P_cubic_mode(ws,p_rated,ws_cin,ws_rated,ws_cout)
    else:
        print("Hum... I'm not sure how you bypassed the data validation... My bad...")


