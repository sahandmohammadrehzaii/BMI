# Constant Variable
cm_to_m_conversion_factor = 100


def calculate_bmi(height_cm: float or int, weight_kg: float or int) -> float:


    # Check parameter's datatypes
    if not isinstance(height_cm, (float, int)) or not isinstance(weight_kg, (float, int)):
        raise TypeError("لطفا اطلاعات را درست وارد کنید")

    if height_cm <= 0 or weight_kg <= 0:
        return 0

    # Calculate BMI using the formula: weight / (height^2)
    bmi = weight_kg / ((height_cm / cm_to_m_conversion_factor) ** 2)

    return bmi


def get_bmi_category(bmi: float or int) -> str:


    # Check parameter datatype
    if not isinstance(bmi, (float, int)):
        raise TypeError('اطلاعات را لطفا درست وارد کنید')

    if bmi == 0:
        return 'غیر طبیعی'
    elif bmi < 18.5:
        return 'کمبود وزنکمبود وزن'
    elif 18.5 <= bmi < 24.9:
        return 'وزن نرمال'
    elif 25 <= bmi < 29.9:
        return 'اضافه وزن'
    else:
        return 'چاقی'
