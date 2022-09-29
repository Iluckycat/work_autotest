import string

def get_names(items:list) -> list:
    names = []
    for item in items:
        if item.get_attribute('class') == 'sh-product__name':
            name = item.text
            names.append(name)
    return names

def is_light(items:list) -> bool:
    light_dev = ['лампочки', 'светильники', 'выключатели', 'лампы', 'ленты', 'освещения', 'контроллеры для светодиодных лент']
    flag_light = True
    for item in items:
        if flag_light == False:
            return flag_light
        is_light_dev = False
        for device in light_dev:
            if device in item.lower():
                is_light_dev = True
        if not is_light_dev:
            flag_light = False
    return flag_light